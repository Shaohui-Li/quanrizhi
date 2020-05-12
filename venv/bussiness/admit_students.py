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
        rows = self.he.get_rows(3)
        student_name="学生名字"
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4, 3)
                module_name = self.he.get_value(i, 2, 3)
                if is_run == "yes" :
                    action_ways = self.he.get_value(i, 5, 3)
                    input_data = self.he.get_value(i, 6, 3)
                    print(input_data)
                    page = self.he.get_value(i, 7, 3)
                    element = self.he.get_value(i, 8, 3)
                    Expect_page = self.he.get_value(i, 9, 3)
                    Expect_element = self.he.get_value(i, 10, 3)
                    EXpect_result = self.he.get_value(i, 11, 3)
                    element_number = self.he.get_value(i, 13, 3)
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
                    elif action_ways=="mouse_menu":
                        self.ha.mouse_menu(page, element,number)
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        if result=="录取成功":
                            flag=True
                            self.he.write_cell_value(i, 12, "Success", "Admission")
                            return flag
                        else:
                            flag = False
                            self.he.write_cell_value(i, 12, "Fail", "Admission")
                            self.ha.save_screenshot_action("../screenshot/" + student_name + ".png")
                            return flag
                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success", "Admission")
                        except Exception as e:
                            self.he.write_cell_value(i, 12, "Fail", "Admission")
                            self.ha.save_screenshot_action("../screenshot/" + Expect_element + ".png")
                        time.sleep(1)
                    self.driver.maximize_window()
        except Exception as e:
            print(e)
            self.he.write_cell_value(i, 12, "Fail","Admission")
            self.ha.save_screenshot_action("../screenshot/"+element+".png")
if __name__=="__main__":
    driver=webdriver.Chrome()
    Check(driver).check_students()