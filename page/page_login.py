from base.base import Base
import page
import time

class PageLogin(Base):
    # 点击登录连接
    def page_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, user):
        self.base_input(page.login_username, user)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击同意和登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_yes)
        time.sleep(0.5)
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err)

    # 截图
    def page_get_img(self):
        self.base_get_img()

    # 点击 安全退出 --》退出使用
    def page_click_logout(self):
        self.base_mouse_move(page.login_out_ele)
        time.sleep(1)
        self.base_click(page.login_out_sure)
        time.sleep(5)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page.login_out_sure)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page.login_link)

    # 清空错误登录数据
    def page_clear_err_msg(self):
        self.base_find_element(page.login_username).clear()
        time.sleep(1)
        self.base_find_element(page.login_pwd).clear()
        time.sleep(1)
        self.base_find_element(page.login_yes).click()
        time.sleep(1)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        time.sleep(0.5)
        self.page_input_password(pwd)
        time.sleep(0.5)
        self.page_click_login_btn()
