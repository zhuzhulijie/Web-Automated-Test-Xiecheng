from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from base.get_logger import GetLogger
import time

# 正确写法 使用单例
log = GetLogger().get_logger()

class Base:
    # 初始化方法
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组
        :param timeout: 默认超时时间为30
        :param poll: 默认访问频率为0.5s
        :return: 返回查到的元素
        """
        # 显式等待
        log.info('正在查找元素:{}'.format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        # 调用查找元素 进行点击
        log.info('正在执行点击元素:{}'.format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        log.info('正在给元素{}输入内容:{}'.format(loc, value))
        ele = self.base_find_element(loc)
        ele.clear()
        log.info('正在给元素:{}清空'.format(loc))
        ele.send_keys(value)
        log.info('正在给元素:{}输入内容'.format(value))

    # frame页面切换
    def base_frame_change(self, loc):
        log.info('正在切换frame页面:{}'.format(loc))
        self.driver.switch_to.frame(self.base_find_element(loc))

    def base_mouse_move(self, loc):
        ac = ActionChains(self.driver)
        log.info('正在移动鼠标悬浮:{}'.format(loc))
        ac.move_to_element(self.base_find_element(loc)).perform()

    # 获取文本方法
    def base_get_text(self, loc):
        log.info('正在获取元素:{}文本'.format(loc))
        return self.base_find_element(loc).text

    # 截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file('./image/{}_fail.png'.format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info('判断元素:{}存在！'.format(loc))
            # 找到元素  assertTrue
            return True
        except:
            # 没找到元素
            log.info('判断元素:{}不存在！'.format(loc))
            return False