#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
"""移动端添加线索"""
class Clue_action:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def add_clue(self):
        rows = self.he.get_rows(1)
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4, 1)
                if is_run == "yes":
                    action_ways = self.he.get_value(i, 5, 1)
                    input_data = self.he.get_value(i, 6, 1)
                    # print(input_data)
                    page = self.he.get_value(i, 7, 1)
                    element = self.he.get_value(i, 8, 1)
                    Expect_page = self.he.get_value(i, 9, 1)
                    Expect_element = self.he.get_value(i, 10, 1)
                    EXpect_result = self.he.get_value(i, 11, 1)
                    element_number = self.he.get_value(i, 13, 1)
                    if action_ways == "open_browser":
                        self.ha.open_url(input_data)
                    elif action_ways == "input_action":
                        if input_data=="姓名":
                            input_data=self.ha.create_name()
                            name=input_data
                        elif input_data=="手机号码":
                            input_data=self.ha.createPhone()
                        self.ha.input_action(page, element, input_data, element_number)
                    elif action_ways == "click_action":
                        self.ha.click_action(page, element, element_number)
                    elif action_ways == "clear_action":
                        self.ha.clear_action(page, element, element_number)
                    elif action_ways == "wait":
                        self.ha.wait_action(int(input_data))
                    elif action_ways == "wait_element":
                        self.ha.wait_element_show(page, element)
                    elif action_ways == "wait_elemnt_click":
                        self.ha.wait_element_click(page, element)
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        print(result)
                        if result == name:
                            flag = True
                            self.he.write_cell_value(i, 12, "Success","add_clue")
                            return flag
                        else:
                            flag = False
                            self.ha.save_screenshot_action("../screenshot/login.png")
                            self.he.write_cell_value(i, 12, "Fail","add_clue")
                            return flag
                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            flag = True
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success","add_clue")
                        except Exception as e:
                            flag = False
                            self.ha.save_screenshot_action("../screenshot/"+Expect_element+".png")
                            self.he.write_cell_value(i, 12, "Fail","add_clue")
                        time.sleep(1)
                self.driver.maximize_window()#最大化屏幕
        except Exception as e:
            print(e)
            self.he.write_cell_value(i, 12, "Fail","add_clue")
            self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Clue_action(driver).add_clue()
