import logging
from .defaults import *


class Ssl(object):
    def __init__(self, session):
        self.session = session
    def delete_ssl_certchain(self):
        raise RuntimeError('not implemented')
    def download_csr(self):
        raise RuntimeError('not implemented')
    def generate_csr(self):
        raise RuntimeError('not implemented')
    def show_cert(self):
        raise RuntimeError('not implemented')
    def upload_signed_cert(self):
        raise RuntimeError('not implemented')
    def upload_cert_chain(self):
        raise RuntimeError('not implemented')


LOGGER = logging.getLogger(__name__)
