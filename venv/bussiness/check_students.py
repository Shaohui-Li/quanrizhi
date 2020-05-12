#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
class Check:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def check_students(self):
        rows = self.he.get_rows(2)
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4, 2)
                module_name = self.he.get_value(i, 2, 2)
                if is_run == "yes" :
                    action_ways = self.he.get_value(i, 5, 2)
                    input_data = self.he.get_value(i, 6, 2)
                    print(input_data)
                    page = self.he.get_value(i, 7, 2)
                    element = self.he.get_value(i, 8, 2)
                    Expect_page = self.he.get_value(i, 9, 2)
                    Expect_element = self.he.get_value(i, 10, 2)
                    EXpect_result = self.he.get_value(i, 11, 2)
                    element_number = self.he.get_value(i, 13, 2)
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
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        if EXpect_result != result:
                            flag = True
                            self.he.write_cell_value(i, 12, "Success", "check_students")
                            return flag
                        else:
                            flag = False
                            self.ha.save_screenshot_action("../screenshot/"+result+".png")
                            self.he.write_cell_value(i, 12, "Fail", "check_students")
                            return flag
                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success", "check_students")
                        except Exception as e:
                            self.he.write_cell_value(i, 12, "Fail", "check_students")
                            self.ha.save_screenshot_action("../screenshot/"+Expect_element+".png")
                        time.sleep(1)
                    self.driver.maximize_window()
        except Exception as e:
            print(e)
            self.he.write_cell_value(i, 12, "Fail","check_students")
            self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Check(driver).check_students()
