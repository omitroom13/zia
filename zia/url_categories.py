import datetime
import logging
import json
import sys

from .defaults import load_config, get_config, RequestError, SessionTimeoutError, ZiaApiBase

class UrlCategories(ZiaApiBase):
    def list(self, custom_only=False):
        path = 'urlCategories'
        if custom_only:
            path += '?customOnly=true'
        return self._output(self._session.get(path))
    def create(self, category):
        path = 'urlCategories'
        return self._output(self._session.post(path, category))
    def list_lite(self):
        path = 'urlCategories/lite'
        return self._output(self._session.get(path))
    def get_quota(self):
        path = 'urlCategories/urlQuota'
        return self._output(self._session.get(path))
    def get(self, category_id):
        path = 'urlCategories/{}'.format(category_id)
        return self._output(self._session.get(path))
    def update(self, category_id, category):
        path = 'urlCategories/{}'.format(category_id)
        return self._output(self._session.put(path, category))
    def delete(self, category_id):
        path = 'urlCategories/{}'.format(category_id)
        return self._output(self._session.delete(path))
    def lookup(self, urls):
        path = 'urlLookup'
        return self._output(self._session.post(path, urls))

LOGGER = logging.getLogger(__name__)
