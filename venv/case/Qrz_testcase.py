#coding=utf-8
from bussiness import Login,add_clue,add_staff,admit_students,check_students,charge,Delete_clue
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
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        print("测试开始")
    def test_login(self):
        result=Login.Login(self.driver).login()
        self.assertTrue(result)
    def test_add_clue(self):
        result=add_clue.Clue_action(self.driver).add_clue()
        self.assertTrue(result)
    def test_add_staff(self):
        result=add_staff.Add_staff(self.driver).add_staff()
        self.assertTrue(result)
    def test_check_student(self):
        result=check_students.Check(self.driver).check_students()
        self.assertTrue(result)
    def test_admit_student(self):
        result=admit_students.register(self.driver).regist()
        self.assertTrue(result)
    def test_create_order(self):
        result=charge.Create_order(self.driver).create_order()
        self.assertTrue(result)
    def test_delete_clue(self):
        Delete_clue.Delete_clue(self.driver).delete_clue()
    def tearDown(self) -> None:
        end_time = datetime.datetime.now()
        print("测试结束")
if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_UI("test_login"))
    suite.addTest(Test_UI("test_add_clue"))
    suite.addTest(Test_UI("test_add_staff"))
    suite.addTest(Test_UI("test_check_student"))
    suite.addTest(Test_UI("test_admit_student"))
    suite.addTest(Test_UI("test_create_order"))
    suite.addTest(Test_UI("test_delete_clue"))
    time_name=str(time.strftime("%m-%d_%H-%M-%S", time.localtime())).strip(" ")
    report_name=time_name+"全日智冒烟测试结果.html"
    report_path = os.getcwd() + "\\"+report_name
    with open(report_path,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="Quanrizhi_autotest",description="test_report")
        result=runner.run(suite)
        print(result)
    f.close()
    media_id=reboat_request.Reboat_request().reboat_upload_file(report_path)
    reboat_request.Reboat_request().reboat_fileadress(media_id)