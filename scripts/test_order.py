# 导包
import unittest
from time import sleep

from page.page_login import PageLogin
from page.page_order import PageOrder
from parameterized import parameterized
from tool.read_json import read_json
from base.get_logger import GetLogger
from base.get_driver import GetDriver
from page.page_order import PageOrder

#　使用单例
log = GetLogger().get_logger()

def get_data():
    arrs = []
    for data in read_json("user_order.json").values():
        arrs.append((data.get("start"),
                     data.get("end"),
                     data.get("day")))
    return arrs  # 注意：必须进行return 返回

class TestOrder(unittest.TestCase):
    login = None
    # setUp

    @classmethod
    def setUpClass(cls):
        try:
            # 实例化 获取页面对象 PageLogin
            cls.login = PageLogin(GetDriver().get_driver())
            cls.order = PageOrder(GetDriver().get_driver())
            # 点击登录连接
            cls.login.page_login_link()
        except Exception as e:
            log.error(e)

    # tearDown
    @classmethod
    def tearDownClass(cls):
        sleep(3)
        # 关闭 driver驱动对象
        GetDriver().quit_driver()

    # 登录、购票测试方法
    @parameterized.expand(get_data())
    def test_order(self, start, end, day):
        # 调用登录方法
        self.login.page_login("19132056083", "zljroy99")
        # 调用购票方法
        self.order.page_order(start, end, day)