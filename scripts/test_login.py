# 导包
import unittest
from time import sleep

from page.page_login import PageLogin
from parameterized import parameterized
from tool.read_json import read_json
from base.get_logger import GetLogger
from base.get_driver import GetDriver

#　使用单例
log = GetLogger().get_logger()

def get_data():
    arrs = []
    for data in read_json("user_login.json").values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("expect_result"),
                     data.get("success")))
    return arrs  # 注意：必须进行return 返回

class TestLogin(unittest.TestCase):
    login = None
    # setUp

    @classmethod
    def setUpClass(cls):
        try:
            # 实例化 获取页面对象 PageLogin
            cls.login = PageLogin(GetDriver().get_driver())
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

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, expect_result, success):
        # 调用登录方法
        self.login.page_login(username, password)
        if success:
            try:
                # 点击退出
                self.login.page_click_logout()
                # 判断安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                try:
                    self.assertTrue(self.login.page_is_logout_success)
                except Exception as e:
                    # 截图
                    self.login.page_get_img()
                    log.error(e)
                # 点击登录连接
                self.login.page_login_link()
            except:
                # 截图
                self.login.page_get_img()
        else:
            # 获取登录提示信息
            msg = self.login.page_get_error_info()
            try:
                # 断言
                self.assertEqual(msg, expect_result)

            except AssertionError:
                # 截图
                self.login.page_get_img()
            # 错误登录数据清空
            self.login.page_clear_err_msg()