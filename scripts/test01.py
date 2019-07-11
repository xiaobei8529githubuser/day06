import allure
import pytest


class Test01():
    @allure.step(title="正在执行登录操作")
    def test001(self):
        print('test0001被执行')

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="正在执行退出操作")
    def test002(self):
        print('test0002被执行')

    #紧要级别
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test003(self):
        #添加描述
        allure.attach("描述","正在打印test003被执行")
        print('test003被执行')

    #崩溃级别
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test004(self):
        #添加描述
        allure.attach("描述","")
        #模拟失败，目的：查看图表优先级颜色
        # assert 0
        print('test003被执行')

    def test005(self):
        #失败截图，将突破写入报告
        with open('./image/fail.png','rb')as f:
            #参数：（描述：文件流，图片类型）
            allure.attach("失败原因：",f.read(),allure.attach_type.PNG)
