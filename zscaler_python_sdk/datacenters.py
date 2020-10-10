import logging
from .defaults import *


class Datacenters(object):
    def __init__(self, session):
        self.session = session
    def get_all_vips(self):
        method = 'vips?include=all'
        return self.session._perform_get_request(method)
    def get_all_public_vips(self):
        method = 'vips?include=public'
        return self.session._perform_get_request(method)
    def get_all_private_vips(self):
        method = 'vips?include=private'
        return self.session._perform_get_request(method)


LOGGER = logging.getLogger(__name__)
