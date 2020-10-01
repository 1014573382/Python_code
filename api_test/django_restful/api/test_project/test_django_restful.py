import unittest
import requests
from test_project.mysql_action import DB
import yaml
import logging


class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('guonian','gxl10230701')

    def test_001_get_user(self):
        logging.info('test_001_get_user')
        r = requests.get(self.base_url + '/1/', auth = self.auth)
        result = r.json()

        self.assertEqual(result['username'], 'guoxl')
        self.assertEqual(result['email'], 'guoxl@163.com')

    def test_002_add_user(self):
        logging.info('test_002_add_user')
        from_data = {'id':3, 'username':'guoguo', 'email':'guoguo@163.com',
                     'groups': 'http://127.0.0.1:8000/groups/2/'}
        r = requests.post(self.base_url + '/', data=from_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['username'], 'guoguo')

    def test_003_delete_user(self):
        logging.info('test_003_delete_user')
        r = requests.delete(self.base_url + '/2/', auth=self.auth)

        self.assertEqual(r.status_code, 204)

    def test_004_update_user(self):
        logging.info('test_004_update_user')
        from_data = {'email':'guoxl@126.com'}
        r = requests.patch(self.base_url + '/1/', auth=self.auth, data=from_data)
        result = r.json()

        self.assertEqual(result['email'], 'guoxl@126.com')

    def test_005_no_auth(self):
        logging.info('test_005_no_auth')
        r = requests.get(self.base_url)
        result = r.json()

        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('guonian', 'gxl10230701')

    def test_001_group_developer(self):
        logging.info('test_001_group_developer')
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'], 'Developer')

    def test_002_add_group(self):
        logging.info('test_002_add_group')
        from_data = {'name': 'pm'}
        r = requests.post(self.base_url + '/', auth=self.auth, data = from_data)
        result = r.json()

        self.assertEqual(result['name'], 'pm')

    def test_003_update_group(self):
        logging.info('test_003_update_group')
        from_data = {'name': 'guoxiao'}
        r = requests.patch(self.base_url + '/2/', auth=self.auth, data=from_data)
        result = r.json()

        self.assertEqual(result['name'], 'guoxiao')

    # @unittest.skip('skip test_delete_group')
    def test_delete_group(self):
        logging.info('test_delete_group')
        r = requests.delete(self.base_url + '/1/', auth=self.auth)

        self.assertEqual(r.status_code,204)


if __name__ == '__main__':
    db = DB()
    with open('datas.yaml', 'r')as f:
        datas = yaml.load(f)
        db.init_data(datas)
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(UserTest('test_001_get_user'))

