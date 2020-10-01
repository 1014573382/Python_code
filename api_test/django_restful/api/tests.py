from django.test import TestCase
import requests

# Create your tests here.
# django本身自带的测试模块，使用命令行执行测试：
# D:\Python\Code\api_test\django_restful>python manage.py test api.tests
class UserTest(TestCase):

    def setUp(self) -> None:
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('guonian','gxl10230701')

    def test_get_users(self):
        r = requests.get(self.base_url + '/1/', auth = self.auth)
        result = r.json()
        # print(result)

        self.assertEqual(result['username'],'guonian')
        self.assertEqual(result['email'],'guoxiaoli1512@163.com')

    # @unittest.skip('skip add user')
    # def test_add_user(self):
    #     from_data = {'username':'Jone','email':'Jone@163.com','groups':'http://127.0.0.1:8000/groups/2/'}
    #     r = requests.post(self.base_url + '/', data=from_data, auth=self.auth)
    #     result = r.json()
    #
    #     self.assertEqual(result['username'],'Jone')

    # @unittest.skip('skip test_delete_user')
    # def test_delete_user(self):
    #     r = requests.delete(self.base_url +'/5/', auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    def test_update_users(self):
        from_data = {'email':'guoguo@163.com'}
        r = requests.patch(self.base_url + '/3/', data=from_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['email'],'guoguo@163.com')

    def test_user_already_exits(self):
        from_data = {'username':'guoxl', 'email':'guoxl@163.com'}
        r = requests.post(self.base_url + '/', data=from_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result['username'][0], 'A user with that username already exists.')


    def test_no_auth(self):
        r = requests.get(self.base_url)
        result = r.json()

        self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(TestCase):

    def setUp(self) -> None:
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('guonian','gxl10230701')

    def test_group_Tester1(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        self.assertEqual(result['name'],'Tester1')

    # @unittest.skip('skip test_add_group')
    # def test_add_group(self):
    #     from_data = {'name':'guoxiaoli'}
    #     r = requests.post(self.base_url + '/', data=from_data, auth=self.auth)
    #     result = r.json()
    #
    #     self.assertEqual(result['name'],'guoxiaoli')

    def test_update_group(self):
        from_data = {'name':'guoxiao'}
        r = requests.patch(self.base_url + '/4/', auth=self.auth, data=from_data)
        result = r.json()

        self.assertEqual(result['name'],'guoxiao')

    # @unittest.skip('skip test_delete_group')
    # def test_delete_group(self):
    #     r = requests.delete(self.base_url + '/6/', auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)
