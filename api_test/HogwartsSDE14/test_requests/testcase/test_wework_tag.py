#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/20 16:45
import pytest

from HogwartsSDE14.test_requests.api.wework_tag import WeworkTag


class TestWeworkTag:

    @pytest.mark.parametrize(("id", "name"),[("5", "人力资源"),("6", "QA")])
    def test_create_tag(self, id, name):
        print(WeworkTag().test_create_tag(id, name))

    def test_update_tag(self):
        assert "updated" == WeworkTag().test_update_tag("4", "产品")["errmsg"]

    def test_get_taglist(self):
        tag_list = WeworkTag().test_get_taglist()["taglist"]
        print("tag_list:", tag_list)
        assert "ok" == WeworkTag().test_get_taglist()["errmsg"]

    def test_delete_tag(self):
        assert "deleted" == WeworkTag().test_delete_tag("6")["errmsg"]

    # 未成功，一直报missing tagid，待解决
    def test_add_tagmember(self):
        print(WeworkTag().test_add_tagmember("4"))

    def test_get_tagmember(self):
        tag_member = WeworkTag().test_get_tagmember(1)["userlist"]
        print("tag_member: ", tag_member)
        assert "ok" == WeworkTag().test_get_tagmember(1)["errmsg"]

