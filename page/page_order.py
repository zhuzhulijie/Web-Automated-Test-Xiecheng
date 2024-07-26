from base.base import Base
import page
import time
from selenium.webdriver.common.by import By

class PageOrder(Base):
    # 选择班次方法
    def page_search_train(self, start, end, day):
        # 点击火车购买页面
        self.base_click(page.ticket_train)
        # 输入起始站和终点站
        train_start = self.base_find_element(page.ticket_start)
        self.base_click(page.ticket_start)
        train_start.clear()
        time.sleep(1)
        train_start.send_keys(start)
        time.sleep(1)
        train_end = self.base_find_element(page.ticket_end)
        self.base_click(page.ticket_end)
        train_end.clear()
        time.sleep(1)
        train_end.send_keys(end)
        time.sleep(1)
        # 选择日期
        self.base_click(page.ticket_end_ok)
        self.base_click(page.ticket_end_click)
        time.sleep(1)
        # 添加出发日期断言
        cur_day = time.gmtime(time.time()).tm_mday
        assert cur_day <= int(day) <= (cur_day + 14), f"({int(day)}) 不在 ({cur_day}) 和 ({cur_day + 14}) 之间"
        ticket_day = By.XPATH, f"//ul/li[{day}]"
        self.base_click(ticket_day)
        time.sleep(1)
        # 点击搜索
        self.base_click(page.ticket_search)

    # 购票信息方法
    def page_choose_train(self):
        time.sleep(1)
        # 仅显示有票车次
        self.base_click(page.ticket_exist)
        time.sleep(1)
        # 选择火车
        self.base_click(page.ticket_order)
        time.sleep(1)
        self.base_click(page.ticket_order2)

    # 新增乘客
    def page_choose_passenger(self):
        # 新增乘客
        time.sleep(1)
        self.base_click(page.ticket_add_passenger)
        time.sleep(1)
        self.base_frame_change(page.ticket_switch_frame)
        self.base_click(page.ticket_passenger)
        time.sleep(1)
        self.base_click(page.ticket_passenger_click)
        time.sleep(1)
        self.driver.switch_to.default_content()
        # # 选择靠窗位置
        # self.base_click(page.ticket_window)
        # time.sleep(1)
        # 立即预定
        self.base_click(page.ticket_schedule)

    # 取消订单
    def page_cancle_order(self):
        time.sleep(1)
        self.base_click(page.ticket_cancle_order)
        time.sleep(1)
        self.base_click(page.ticket_cancle_ensure)
        time.sleep(1)
        # 回到主页
        self.base_click(page.login_back)

    # 退出登录
    def page_login_out(self):
        self.base_mouse_move(page.login_out_ele)
        time.sleep(1)
        self.base_click(page.login_out_sure)
        time.sleep(5)

    # 点击 安全退出 --》退出使用
    def page_click_logout(self):
        self.base_click(page.login_out_sure)

    # 判断是否登录成功
    def page_is_login_success(self):
        return self.base_if_exist(page.login_out_sure)

    # 判断是否退出成功
    def page_is_logout_success(self):
        return self.base_if_exist(page.login_link)

    # 截图
    def page_get_img(self):
        self.base_get_img()

    def page_order(self, start, end, day):
        # 选择班次
        self.page_search_train(start, end, day)
        # 购票信息
        self.page_choose_train()
        # 新增乘客
        self.page_choose_passenger()
        # 取消订单
        self.page_cancle_order()
        # 退出登录
        self.page_login_out()


