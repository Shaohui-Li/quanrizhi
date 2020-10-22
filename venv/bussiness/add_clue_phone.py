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
        rows = self.he.get_rows(8)
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4, 8)
                if is_run == "yes":
                    action_ways = self.he.get_value(i, 5, 8)
                    input_data = self.he.get_value(i, 6, 8)
                    # print(input_data)
                    page = self.he.get_value(i, 7, 8)
                    element = self.he.get_value(i, 8, 8)
                    Expect_page = self.he.get_value(i, 9, 8)
                    Expect_element = self.he.get_value(i, 10, 8)
                    EXpect_result = self.he.get_value(i, 11, 8)
                    element_number = self.he.get_value(i, 13, 8)
                    pre_condition = self.he.get_value(i, 14, 8)
                    if action_ways == "open_browser":
                        self.ha.open_url(input_data)
                        self.driver.maximize_window()  # 最大化屏幕
                    elif action_ways == "input_action":
                        if pre_condition == "日期":  # 输入日期判断
                            self.ha.data_input(page, element, element_number)
                            input_data = input_data.strftime("%Y-%m-%d")
                        if input_data == "姓名":
                            input_data = self.ha.create_name()
                            name = input_data
                        elif input_data == "手机号码":
                            input_data = self.ha.createPhone()
                        elif input_data == "证件号码":
                            input_data = self.ha.ident_generator()
                        elif input_data == "学籍号":
                            input_data = self.ha.registration_number()
                        self.ha.input_action(page, element, input_data, element_number)
                    elif action_ways == "click_action":
                        if pre_condition == "日期":  # 输入日期判断
                            self.ha.scroll_page(page, element, element_number)
                        else:
                            self.ha.click_action(page, element, element_number)
                    elif action_ways == "clear_action":
                        self.ha.clear_action(page, element, element_number)
                    elif action_ways == "wait":
                        self.ha.wait_action(int(input_data))
                    elif action_ways == "wait_element":
                        self.ha.wait_element_show(page, element)
                    elif action_ways == "wait_elemnt_click":
                        self.ha.wait_element_click(page, element)
                    elif action_ways == "page_scroll":
                        self.ha.page_scroll(page, element, element_number)
                    elif action_ways == "scroll_page":
                        self.ha.scroll_page(page, element, element_number)
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        print(result)
                        if result == EXpect_result:
                            flag = True
                            self.he.write_cell_value(i, 12, "Success", "add_clue_phone")
                        else:
                            flag = False
                            self.ha.save_screenshot_action("../screenshot/login.png")
                            self.he.write_cell_value(i, 12, "Fail", "add_clue_phone")

                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            flag = True
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success", "add_clue_phone")
                        except Exception as e:
                            flag = False
                            self.ha.save_screenshot_action("../screenshot/" + Expect_element + ".png")
                            self.he.write_cell_value(i, 12, "Fail", "add_clue_phone")
        except Exception as e:
            flag = False
            self.he.write_cell_value(i, 12, "Fail","add_clue_phone")
            self.ha.save_screenshot_action("../screenshot/"+element+".png")
        return flag

if __name__=="__main__":
    option = webdriver.ChromeOptions()
    mobileEmulation = {'deviceName': 'iPhone X'}
    option.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(chrome_options=option)
    Clue_action(driver).add_clue()