import allure
from selenium import webdriver


class Test_001(object):

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    @allure.step("第一步，这是一个普通方法")
    def zxc(self):
        print("普通")

    @allure.step("第二步，这是一个测试方法")
    def test_01(self):
        self.zxc()
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(), "截图百度首页", allure.attachment_type.PNG)
        print("\n  --------我是test_01-------")
