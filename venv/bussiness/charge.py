#coding=utf-8
#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
class Student_charge:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def charge_student(self):
        rows = self.he.get_rows(4)
        # try:
        for i in range(1, int(rows) + 1):
            is_run = self.he.get_value(i, 4, 4)
            module_name = self.he.get_value(i, 2, 4)
            if is_run == "yes":
                action_ways = self.he.get_value(i, 5, 4)  # 操作方法
                input_data = self.he.get_value(i, 6, 4)  # 输入内容
                page = self.he.get_value(i, 7, 4)  # 当前页面
                element = self.he.get_value(i, 8, 4)  # 元素
                Expect_page = self.he.get_value(i, 9, 4)  # 期望页面
                Expect_element = self.he.get_value(i, 10, 4)  # 期望元素
                EXpect_result = self.he.get_value(i, 11, 4)  # 期望结果
                element_number = self.he.get_value(i, 13, 4)  # 元素位置
                pre_page = self.he.get_value(i, 14, 4)  # 前置页面
                pre_element = self.he.get_value(i, 15, 4)  # 前置元素
                pre_element_number = self.he.get_value(i, 16, 4)  # 前置元素位置
                son_page=self.he.get_value(i, 17, 4)
                son_element=self.he.get_value(i, 18, 4)
                son_number=self.he.get_value(i, 19, 4)
                pre_flag = True
                if pre_element != None:
                    try:
                        self.ha.isElementExist(pre_page, pre_element)
                        pre_flag = True
                    except Exception as e:
                        pre_flag = False
                        self.ha.save_screenshot_action("../screenshot/" + pre_element + ".png")
                if pre_flag == True and pre_element == None:
                    if action_ways == "open_browser":
                        self.ha.open_url(input_data)
                    elif action_ways == "input_action":
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
                    elif action_ways == "mouse_menu":
                        self.ha.mouse_menu(page, element, element_number)
                    elif action_ways == "father_son_click":
                        print(son_number)
                        self.ha.father_son_click(page, element, son_page, son_element, number1=element_number,number2=son_number)
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        if result == EXpect_result:
                            self.he.write_cell_value(i, 12, "Success", "charge")
                        else:
                            self.he.write_cell_value(i, 12, "Fail", "charge")
                        # self.he.write_cell_value(i, 12, result, "charge")
                    elif action_ways == "isElementExist":
                        result=self.ha.isElementExist(page,element)
                        if result:
                            # self.he.write_cell_value(i, 12, "Success", "charge")
                            self.ha.click_action(Expect_page,Expect_element,element_number)
                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success", "charge")
                        except Exception as e:
                            self.he.write_cell_value(i, 12, "Fail", "charge")
                            self.ha.save_screenshot_action("../screenshot/" + Expect_element + ".png")
                        time.sleep(1)
                    self.driver.maximize_window()
        # except Exception as e:
        #     print(e)
        #     self.he.write_cell_value(i, 12, "Fail","charge")
        #     self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Student_charge(driver).charge_student()
