
import logging
from .defaults import *


class User(object):
    def __init__(self, session):
        self.session = session
    def get_departments(self):
        raise RuntimeError('not implemented')
    def get_departments_by_id(self, department_id):
        raise RuntimeError('not implemented')
    def get_groups(self):
        raise RuntimeError('not implemented')
    def get_group_by_id(self, group_id):
        raise RuntimeError('not implemented')
    def get_users(self):
        raise RuntimeError('not implemented')
    def get_user_by_id(self, user_id):
        raise RuntimeError('not implemented')
    def create_user(self, user):
        raise RuntimeError('not implemented')
    def delete_users(self, users):
        raise RuntimeError('not implemented')
    def update_user(self, user):
        raise RuntimeError('not implemented')
    def delete_user_by_id(self, user):
        raise RuntimeError('not implemented')


LOGGER = logging.getLogger(__name__)
