from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):

    def on_start(self):
        # 设置user和group参数下标初始值
        self.users_index = 0
        self.groups_index = 0

    @task
    def test_users(self):
        # 读取参数
        users_id = self.locust.id[self.users_index]
        url = '/users/' + str(users_id) + '/'
        self.client.get(url, auth=('guonian','gxl10230701'))
        # 取余运算循环遍历参数
        self.users_index = (self.users_index + 1) % len(self.locust.id)
        # for i in(range(3)):
        #     self.users_index = i

    @task
    def test_groups(self):
        # 读取参数
        groups_id = self.locust.id[self.groups_index]
        url = '/groups/' + str(groups_id) + '/'
        self.client.get(url, auth=('guonian', 'gxl10230701'))
        # 取余运算循环遍历参数
        self.groups_index = (self.groups_index + 1) % len(self.locust.id)



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # 参数设置
    id = [1,2,3]
    min_wait = 3000
    max_wait = 6000
    host = 'http://127.0.0.1:8000'

