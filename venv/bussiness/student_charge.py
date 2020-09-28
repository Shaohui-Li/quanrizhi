#coding=utf-8
#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
"""收费"""
class Charge:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def charge(self):
        rows = self.he.get_rows(7)
        # try:
        student_phone = None
        result=None
        for i in range(1, int(rows) + 1):
            is_run = self.he.get_value(i, 4, 7)
            module_name = self.he.get_value(i, 2, 7)
            if is_run == "yes":
                action_ways = self.he.get_value(i, 5, 7)  # 操作方法
                input_data = self.he.get_value(i, 6, 7)  # 输入内容
                page = self.he.get_value(i, 7, 7)  # 当前页面
                element = self.he.get_value(i, 8, 7)  # 元素
                Expect_page = self.he.get_value(i, 9, 7)  # 期望页面
                Expect_element = self.he.get_value(i, 10, 7)  # 期望元素
                EXpect_result = self.he.get_value(i, 11, 7)  # 期望结果
                element_number = self.he.get_value(i, 13, 7)  # 元素位置
                pre_page = self.he.get_value(i, 14, 7)  # 前置页面
                pre_element = self.he.get_value(i, 15, 7)  # 前置元素
                pre_element_number = self.he.get_value(i, 16, 7)  # 前置元素位置
                son_page=self.he.get_value(i, 17, 7)
                son_element=self.he.get_value(i, 18, 7)
                son_number=self.he.get_value(i, 19, 7)
                pre_flag = True
                if action_ways == "open_browser":
                    self.ha.open_url(input_data)
                    self.driver.maximize_window()
                elif action_ways == "input_action":
                    if input_data == "姓名":
                        input_data = self.ha.create_name()
                        name = input_data
                    elif input_data == "手机号码":
                        input_data = self.ha.createPhone()
                        staff_phone=input_data
                    self.ha.input_action(page, element, str(input_data), element_number)
                elif action_ways == "search_action":
                    self.ha.input_action(page, element, student_phone, element_number)
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
                elif action_ways == "mouse_menu":
                    self.ha.mouse_menu(page, element, element_number)
                elif action_ways == "father_son_mouseaction":
                    self.ha.father_son_mouseaction(page, element, pre_page, pre_element, number1=element_number,
                                             number2=pre_element_number)
                elif action_ways == "switch_action":
                    handles = self.ha.switch_page(1)
                elif action_ways == "father_son_click":
                    self.ha.father_son_click(page, element, pre_page, pre_element, number1=element_number,
                                             number2=pre_element_number)
                elif action_ways == "father_son_input":
                    self.ha.father_son_input(page, element, pre_page, pre_element, result, element_number,
                                             pre_element_number)
                elif action_ways == "father_son_text":
                    result2=self.ha.father_son_text(page, element, pre_page, pre_element, element_number,
                                             pre_element_number)
                    self.he.write_cell_value(i, 12, result2, "Charge")
                elif action_ways == "element_text":
                    result = self.ha.element_text(page, element, element_number)
                    print(result)
                    if result == EXpect_result:
                        self.he.write_cell_value(i, 12, "Success", "Charge")
                    else:
                        self.he.write_cell_value(i, 12, "Fail", "Charge")
                    # self.he.write_cell_value(i, 12, result, "Charge")
                elif action_ways == "isElementExist":
                    result = self.ha.isElementExist(page, element)
                    if result:
                        # self.he.write_cell_value(i, 12, "Success", "Charge")
                        self.ha.click_action(Expect_page, Expect_element, element_number)
                if Expect_element != None:  # 如果期待元素为空，则不执行
                    try:
                        self.ha.wait_element_show(Expect_page, Expect_element)
                        self.he.write_cell_value(i, 12, "Success", "Charge")
                    except Exception as e:
                        self.he.write_cell_value(i, 12, "Fail", "Charge")
                        self.ha.save_screenshot_action("../screenshot/" + Expect_element + ".png")
                    time.sleep(1)
        # except Exception as e:
        #     print(e)
        #     self.he.write_cell_value(i, 12, "Fail","Charge")
        #     self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Charge(driver).charge()