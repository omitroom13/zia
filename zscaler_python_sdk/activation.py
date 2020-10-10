import logging

class Activation(object):
    def __init__(self, session):
        self.session = session
    def get_status(self):
        method = 'status'
        return self._perform_get_request(method)
    def activate(self):
        method = 'status/activate'
        body = {}
        return self._perform_post_request(method, body)


LOGGER = logging.getLogger(__name__)
