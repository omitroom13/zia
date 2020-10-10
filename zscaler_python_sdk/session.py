
import json
import time
import platform
import re
import logging

import requests

from .defaults import *


class Session(object):
    API_VERSION  = 'api/v1'
    USER_AGENT = 'zia api sdk'
    def __init__(self, url, username, password, api_key):
        self.url = url
        if url[-1] == '/':
            raise RuntimeError('url {} must not be end with "/".'.format(url))
        self.username = username
        self.password = password
        (self.timestamp, self.obfuscated_api_key) = self._obfuscate_api_key(api_key)
        self.session = requests.Session()
    def _set_header(self, cookie=None):
        header = {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'User-Agent': self.USER_AGENT
        }
        if cookie:
            header['cookie'] = cookie
        LOGGER.debug("HTTP Header: {}".format(header))
        return header
    def _parse_jsessionid(self, cookie):
        jsessionid = re.sub(r';.*$', "", cookie)
        LOGGER.debug("JSESSION ID: {}".format(jsessionid))
        return jsessionid
    def _obfuscate_api_key(self, api_key):
        now = str(int(time.time() * 1000))
        n = now[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(n), 1):
            key += api_key[int(n[i])]
        for j in range(0, len(r), 1):
            key += api_key[int(r[j])+2]
        LOGGER.debug(
            "OBFUSCATED APY KEY / Time: ***** / {}".format(now))
        return (now, key)
    def authenticate(self):
        method = 'authenticatedSession'
        body = {
            'username': self.username,
            'password': self.password,
            'apiKey': self.obfuscated_api_key,
            'timestamp': self.timestamp
        }
        LOGGER.debug("HTTP BODY: {}".format(body))
        res = self._perform_post_request(
            method,
            body
        )
        LOGGER.debug(res)
        if not res['authType']:
            raise RuntimeError('not authenticated')
        LOGGER.info('authenticated')
    def _perform_get_request(self, method, header=None):
        if header == None:
            header = self._set_header()
        uri = "/".join([self.url, self.API_VERSION, method])
        res = self.session.get(
            uri,
            headers=header,
            timeout=REQUEST_TIMEOUTS
        )
        res.raise_for_status()
        if len(res.text) == 0:
            return None
        try:
            j = res.json()
            return j
        except json.decoder.JSONDecodeError:
            pass
        return res.text
    def _perform_post_request(self, method, body, header=None):
        if header == None:
            header = self._set_header()
        uri = "/".join([self.url, self.API_VERSION, method])
        attempt = json.dumps(body, sort_keys=True,
                             indent=4, separators=(',', ': '))
        LOGGER.debug("ATTEMPTING POST (URI): {}\nPOST BODY: {}".format(
            uri,
            attempt
        ))
        res = self.session.post(
            uri,
            json=body,
            headers=header,
            timeout=REQUEST_TIMEOUTS
        )
        res.raise_for_status()
        if len(res.text) == 0:
            return None
        return res.json()
    def _perform_put_request(self, method, body, header=None):
        if header == None:
            header = self._set_header()
        uri = "/".join([self.url, self.API_VERSION, method])
        attempt = json.dumps(body, sort_keys=True,
                             indent=4, separators=(',', ': '))
        LOGGER.debug("ATTEMPTING PUT (URI): {}\nPUT BODY: {}".format(
            uri,
            attempt)
        )
        res = self.session.put(
            uri,
            json=body,
            headers=header,
            timeout=REQUEST_TIMEOUTS
        )
        res.raise_for_status()
        if len(res.text) == 0:
            return None
        return res.json()
    def _perform_delete_request(self, method, header=None):
        if header == None:
            header = self._set_header()
        uri = "/".join([self.url, self.API_VERSION, method])
        res = self.session.delete(
            uri,
            headers=header,
            timeout=REQUEST_TIMEOUTS
        )
        res.raise_for_status()
        if len(res.text) == 0:
            return None
        return res.json()


LOGGER = logging.getLogger(__name__)
