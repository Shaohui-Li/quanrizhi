#coding=utf-8
from handle.excel_handle import Excel_handle
from handle.action import Action
from selenium import webdriver
import unittest
import time
class Test_charge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.he = Excel_handle()
        self.ha = Action(self.driver)
    def test_charge(self):
        self.driver.maximize_window()
        rows=self.he.get_rows()
        try:
            for i in range(1, int(rows) + 1):
                is_run = self.he.get_value(i, 4)
                if is_run == "yes":
                    action_ways = self.he.get_value(i, 5)
                    input_data = self.he.get_value(i, 6)
                    page = self.he.get_value(i, 7)
                    element = self.he.get_value(i, 8)
                    Expect_page = self.he.get_value(i, 9)
                    Expect_element = self.he.get_value(i, 10)
                    element_number = self.he.get_value(i, 13)
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
                    if Expect_element != None:
                        time.sleep(1)
                        flag = self.ha.isElementExist(Expect_page, Expect_element)
                        if flag:
                            self.he.write_cell_value(i, 12, "Success")
                        else:
                            self.ha.save_screenshot_action("../screenshot/login.png")
                            self.he.write_cell_value(i, 12, "Fail")
                        time.sleep(1)
                        self.assertTrue(flag, "用例执行成功")

        except Exception as e:
            print(e)
            self.ha.save_screenshot_action("../screenshot/"+element+".png")
    def tearDown(self):
        self.ha.shut_web_action()
if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_charge)
    unittest.TextTestRunner().run(suite)