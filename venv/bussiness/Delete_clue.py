#coding=utf-8
#coding=utf-8
from handle.action import Action
from selenium import webdriver
from handle.excel_handle import Excel_handle
import time
"""删除线索"""
class Delete_clue:
    def __init__(self,driver):
        self.ha=Action(driver)
        self.driver=driver
        self.he = Excel_handle()
    def delete_clue(self):
        rows = self.he.get_rows(5)
        flag = True
        student_name = None
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4, 5)
                module_name = self.he.get_value(i, 2, 5)
                if is_run == "yes":
                    action_ways = self.he.get_value(i, 5, 5)  # 操作方法
                    input_data = self.he.get_value(i, 6, 5)  # 输入内容
                    page = self.he.get_value(i, 7, 5)  # 当前页面
                    element = self.he.get_value(i, 8, 5)  # 元素
                    Expect_page = self.he.get_value(i, 9, 5)  # 期望页面
                    Expect_element = self.he.get_value(i, 10, 5)  # 期望元素
                    EXpect_result = self.he.get_value(i, 11, 5)  # 期望结果
                    element_number = self.he.get_value(i, 13, 5)  # 元素位置
                    pre_page = self.he.get_value(i, 14, 5)  # 前置页面
                    pre_element = self.he.get_value(i, 15, 5)  # 前置元素
                    pre_element_number = self.he.get_value(i, 16, 5)  # 前置元素位置
                    son_page = self.he.get_value(i, 17, 5)
                    son_element = self.he.get_value(i, 18, 5)
                    son_number = self.he.get_value(i, 19, 5)
                    pre_flag = True
                    if action_ways == "open_browser":
                        self.ha.open_url(input_data)
                        self.driver.maximize_window()
                    elif action_ways == "input_action":
                        self.ha.input_action(page, element, input_data, element_number)
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
                        result2 = self.ha.father_son_text(page, element, pre_page, pre_element, element_number,
                                                          pre_element_number)
                        self.he.write_cell_value(i, 12, result2, "delete_clue")
                    elif action_ways == "element_text":
                        result = self.ha.element_text(page, element, element_number)
                        if student_name==None:
                            student_name = result
                        if EXpect_result != None:
                            print(result)
                            if result != student_name:
                                flag = True
                                self.he.write_cell_value(i, 12, "Success", "delete_clue")
                            else:
                                flag = False
                                self.he.write_cell_value(i, 12, "Fail", "delete_clue")
                        else:
                            self.he.write_cell_value(i, 12, result, "delete_clue")
                        # self.he.write_cell_value(i, 12, result, "delete_clue")
                    elif action_ways == "isElementExist":
                        result = self.ha.isElementExist(page, element)
                        if result:
                            # self.he.write_cell_value(i, 12, "Success", "delete_clue")
                            self.ha.click_action(Expect_page, Expect_element, element_number)
                    if Expect_element != None:  # 如果期待元素为空，则不执行
                        try:
                            flag = True
                            self.ha.wait_element_show(Expect_page, Expect_element)
                            self.he.write_cell_value(i, 12, "Success", "delete_clue")
                        except Exception as e:
                            flag = False
                            self.he.write_cell_value(i, 12, "Fail", "delete_clue")
                            self.ha.save_screenshot_action("../screenshot/" + Expect_element + ".png")
                            return flag
        except Exception as e:
            flag=False
            self.he.write_cell_value(i, 12, "Fail", "delete_clue")
            self.ha.save_screenshot_action("../screenshot/" + element + ".png")
        return flag
if __name__=="__main__":
    driver=webdriver.Chrome()
    if(Delete_clue(driver).delete_clue()):
        print("用例执行成功")
    else:
        print("用例执行失败")
    driver.quit()