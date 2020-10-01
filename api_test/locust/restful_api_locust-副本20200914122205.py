from locust import HttpLocust,TaskSet,task

# 描述用户行为
class UserBehavior(TaskSet):

    @task(2)
    def test_users(self):
        self.client.get('/users/', auth=('guonian','gxl10230701'))

    @task(1)
    def test_groups(self):
        self.client.get('/groups/', auth=('guonian','gxl10230701'))


# WebsiteUser类用于设置性能测试
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000