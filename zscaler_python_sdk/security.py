
import json
import logging


class Security(object):
    def __init__(self, session):
        self.session = session
    def get_whitelist_urls(self):
        method = 'security'
        return self._perform_get_request(method)
    def update_whitelist_urls(self):
        raise RuntimeError('not implemented')
    def get_blacklist_urls(self):
        method = 'security/advanced'
        return self._perform_get_request(method)
    def update_blacklist_urls(self):
        raise RuntimeError('not implemented')
    def add_blacklist_urls(self, black_list_urls):
        method = 'security/advanced/blacklistUrls?action=ADD_TO_LIST'
        body = {
            "blacklistUrls": [
            ]
        }
        for url in black_list_urls:
            body['blacklistUrls'].append(str(url))
        return self._perform_post_request(method, body)
    def remove_blacklist_urls(self):
        raise RuntimeError('not implemented')


LOGGER = logging.getLogger(__name__)
