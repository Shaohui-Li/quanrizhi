#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
class Login:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def login(self):
        rows = self.he.get_rows()
        # try:
        for i in range(1, int(rows) + 1):
            is_run = self.he.get_value(i, 4)
            if is_run == "yes":
                action_ways = self.he.get_value(i, 5)#获取页面操作方法
                input_data = self.he.get_value(i, 6)#获取输入内容
                # print(input_data)
                page = self.he.get_value(i, 7)#定位页面
                element = self.he.get_value(i, 8)#定位页面元素
                Expect_page = self.he.get_value(i, 9)#定位预期页面
                Expect_element = self.he.get_value(i, 10)#定位预期元素
                element_number = self.he.get_value(i, 13)#定位页面元素位置
                if action_ways == "open_browser":#打开浏览器
                    self.ha.open_url(input_data)
                elif action_ways == "input_action":#输入内容
                    self.ha.input_action(page, element, input_data, element_number)
                elif action_ways == "click_action":#点击
                    self.ha.click_action(page, element, element_number)
                elif action_ways == "clear_action":#清空输入框
                    self.ha.clear_action(page, element, element_number)
                elif action_ways == "wait":#强制等待
                    self.ha.wait_action(int(input_data))
                elif action_ways == "wait_element":#等待元素出现爱页面
                    self.ha.wait_element_show(page, element)
                elif action_ways == "wait_elemnt_click":#等待元素可以点击
                    self.ha.wait_element_click(page, element)
                elif action_ways == "element_text":#点击元素的文本内容
                    self.ha.element_text(page, element, element_number)
                if Expect_element != None:  # 如果期待元素为空，则不执行
                    try:
                        flag=True
                        self.ha.wait_element_show(Expect_page, Expect_element)
                        self.he.write_cell_value(i, 12, "Success")
                        return flag
                    except Exception as e:
                        flag=False
                        self.ha.save_screenshot_action("../screenshot/login.png")
                        self.he.write_cell_value(i, 12, "Fail")
                        return flag
                    time.sleep(1)
                self.driver.maximize_window()#最大化屏幕
                    # self.assertTrue(flag, "用例执行成功")

        # except Exception as e:
        #     print(e)
        #     self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Login(driver).login()