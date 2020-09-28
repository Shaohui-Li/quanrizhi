#coding=utf-8
from bussiness import Login,add_clue,add_clue_phone,add_staff,admit_students,check_students,Delete_clue
import unittest
from selenium import webdriver
import HTMLTestRunner
import os
from handle import reboat_request
import time
import datetime

class Test_UI(unittest.TestCase):
    def setUp(self):
        start_time=datetime.datetime.now()
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        print("测试开始")
    def test_add_clue_phone(self):
        mobileEmulation = {'deviceName': 'iPhone X'}
        self.option.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=self.option)
        result=add_clue_phone.Clue_action(self.driver).add_clue()
        self.assertTrue(result)
    def tearDown(self) -> None:
        end_time = datetime.datetime.now()
        self.driver.quit()
        print("测试结束")
if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_UI("test_add_clue_phone"))
    time_name=str(time.strftime("%m-%d_%H-%M-%S", time.localtime())).strip(" ")
    report_name=time_name+"全日智冒烟测试结果.html"
    report_path = os.getcwd() + "\\"+report_name
    with open(report_path,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="Quanrizhi_autotest",description="test_report")
        result=runner.run(suite)
        print(result)
    f.close()
    # media_id=reboat_request.Reboat_request().reboat_upload_file(report_path)
    # reboat_request.Reboat_request().reboat_fileadress(media_id)