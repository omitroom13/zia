
import logging
from .defaults import *


class Gre(object):
    def __init__(self, session):
        self.session = session
    def get_gre_tunnel_details(self):
        method = 'orgProvisioning/ipGreTunnelInfo'
        return self._perform_get_request(method)


LOGGER = logging.getLogger(__name__)
