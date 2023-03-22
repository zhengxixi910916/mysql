# -*- coding: utf-8 -*-
# @Time  : 2021/5/19 17:21
# @File  : webTools.py
# @Author: guo

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# import logging.config
from erdcloud.erdLog import Log

# 法1：
log = Log()


# # 法2
# # 拿到配置文件
# logging.config.fileConfig('./config/log.ini')
# # 拿到日志器
# log = logging.getLogger()


class webTools:

    def __init__(self, driver):
        # log1.info('初始化浏览器{}'.format(driver))
        log.info('初始化浏览器{}'.format(driver))
        self.driver = driver

    def open(self, url):
        log.info('正在访问网址{}'.format(url))
        self.driver.get(url)

    # 定位元素关键字
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入关键字
    def input(self, loc, value):
        try:
            log.info('正在定位{}元素，元素值为{}'.format(loc, value))
            self.locator(loc).clear()
            self.locator(loc).send_keys(value)
        except Exception as e:
            log.error('输入内容失败%s' % e)

    # 点击关键字
    def click(self, loc):
        try:
            log.info('正在定位{}元素,进行点击'.format(loc))
            self.locator(loc).click()
        except Exception as e:
            log.error('点击按钮失败%s' % e)

    def quit(self):
        self.driver.quit()

    # 刷新整个页面
    def refresh(self):
        self.refresh()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 执行js
    def execute_js(self, js):
        self.driver.execute_script(js)

    # 模拟回车键
    def enter(self, selector):
        e1 = self.locator(selector)
        e1.send_keys(Keys.ENTER)

    # 模拟鼠标左击
    def left_click(self, loc):
        ActionChains(self.driver).click(loc).perform()

    # 进入框架关键字
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 退出框架关键字
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 显示等待
    def until_wait(self, seconds, loc):
        WebDriverWait(self.driver, seconds).until(lambda driver: self.locator(loc))
