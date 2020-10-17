import logging

from .defaults import load_config, get_config, RequestError, SessionTimeoutError, ZiaApiBase
from .session import Session

class Activation(ZiaApiBase):
    def get_status(self):
        path = 'status'
        return self._output(self._session.get(path))
    def activate(self):
        path = 'status/activate'
        body = {}
        return self._output(self._session.post(path, body))

LOGGER = logging.getLogger(__name__)
