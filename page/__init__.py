"""以下为计算器配置数据"""
from selenium.webdriver.common.by import By
import time
import random

"""以下为服务器域名配置地址"""
url = "https://www.ctrip.com/"

"""以下为协程登录配置数据"""
# 登录链接
login_link = By.CSS_SELECTOR, ".tl_nfes_home_header_login_title_5neWJ"
# 用户名
login_username = By.XPATH, "//*[@id='bbz_accounts_pc_lg_box']/div/div/div[1]/div[1]/form/dl[1]/dd/input"
# 密码
login_pwd = By.XPATH, "//*[@id='bbz_accounts_pc_lg_box']/div/div/div[1]/div[1]/form/dl[2]/dd/input"
# 已同意按钮
login_yes = By.XPATH, "//*[@id='bbz_accounts_pc_lg_box']/div/div/div[1]/div[4]/div/div[1]/label"
# 登录按钮
login_btn = By.XPATH, "//*[@id='bbz_accounts_pc_lg_box']/div/div/div[1]/div[1]/form/dl[3]/dd/input"
# 异常提示信息
login_err = By.XPATH, "//*[@id='bbz_accounts_pc_lg_box']/div/div/div[1]/div[1]/form/div"

"""以下为协程购票配置数据"""
# 火车票
ticket_train = By.XPATH, "//*[@id='leftSideNavLayer']/div/div/div[2]/div/div[1]/div/div[3]/button/span[2]"
# 起始站
ticket_start = By.CSS_SELECTOR, "#label-departStation"
# 达到城市
ticket_end = By.CSS_SELECTOR, "#label-arriveStation"
# 出发日期
ticket_end_ok = By.CSS_SELECTOR, ".cont"
ticket_end_click = By.CSS_SELECTOR, ".assist-hidden-dom"

# 搜索
ticket_search = By.XPATH, "//*[@id='app']/div[2]/div[1]/div[2]/button"
# 仅显示有票车次
ticket_exist = By.XPATH, "//*[@id='__next']/div/div[3]/div[2]/div[1]/div[2]/div[1]/ul/li/i"
# 预定
ticket_order = By.XPATH, "//*[@id='trainlistitem0']/div/button"
ticket_order2 = By.XPATH, "//*[@id='__next']/div/div[3]/div[1]/section/div[2]/ul/li[3]/button"
# 新增乘客
ticket_add_delete_passenger = By.CSS_SELECTOR, "#__next > div > div.train-wrapper.train-flex.pb120 > div.train-content > div.card-white.addpasg-online.assist-hidden-dom.padding8 > div.addpasg-online-bd > ul > li > i"
ticket_add_passenger = By.CSS_SELECTOR, "#__next > div > div.train-wrapper.train-flex.pb120 > div.train-content > div.card-white.addpasg-online.assist-hidden-dom.padding8 > div.addpasg-online-blank > button"
ticket_switch_frame = By.CSS_SELECTOR, "#picker-iframe"
ticket_passenger = By.CSS_SELECTOR, "#xt-flatlist_0 > div > div > div.xt-xview.PassengerCell_itemFlexLast__5DXXd > span"
ticket_passenger_click = By.CSS_SELECTOR, "#__next > div:nth-child(1) > div > div.passengerList_bottomButtonWrap__IM5IB > div.passengerList_buttonLinear__3JUho > div > span"
# 选择靠窗位置
ticket_window = By.XPATH, "//*[@id='__next']/div/div[2]/div[1]/div[6]/dl/dd[5]"
# 立即预定
ticket_schedule = By.CSS_SELECTOR, "#__next > div > div.train-wrapper.train-flex.pb120 > div.train-content > div.online-btn.h5hide > button.btn-orange"
# 取消订单
ticket_cancle_order = By.CSS_SELECTOR, ".btn-line-grey"
ticket_cancle_ensure = By.XPATH, "//div[@class='pop-modal-btn']//button[2]"

"""以下为协程退出登录数据"""
# 退出登录
# 回到主页
login_back = By.CSS_SELECTOR, "#__next > div:nth-child(2) > div.train-header > div.train-header.fixed.new-header-absolute > div > div.ctriplogo > a"
login_out_ele = By.XPATH, "//*[@id='hp_nfes_accountbar']/li[1]/div/button/div/span"
login_out_sure = By.XPATH, "//*[@id='hp_nfes_accountbar']/li[1]/div/div/div/div[2]/div[2]/a[7]/div"


