#coding=utf-8
import warnings
import sys
sys.path.append(r"D:\project\quanrizhi\venv")
from bussiness import Login,add_clue,add_clue_pc,add_clue_phone,add_student,add_staff,admit_students,check_students,Create_clue_order,Create_student_order,student_charge,Delete_clue
import unittest
from selenium import webdriver
import HTMLTestRunner
import os
from handle import reboat_request
import time
import datetime


class Test_UI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("测试开始")
        warnings.simplefilter('ignore', ResourceWarning)
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')


    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=self.option)
        print("用例开始执行")

    def test_login(self):
        result = Login.Login(self.driver).login()
        self.assertTrue(result)

    def test_add_clue(self):
        result = add_clue.Clue_action(self.driver).add_clue()
        self.assertTrue(result)

    def test_add_student(self):
        result = add_student.Student_action(self.driver).add_student()
        self.assertTrue(result)

    def test_add_PC_clue(self):
        result = add_clue_pc.Clue_action(self.driver).add_clue()
        self.assertTrue(result)

    def test_add_clue_phone(self):
        mobileEmulation = {'deviceName': 'iPhone X'}
        self.option.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=self.option)
        result = add_clue_phone.Clue_action(self.driver).add_clue()
        self.assertTrue(result)

    def test_add_staff(self):
        result = add_staff.Add_staff(self.driver).add_staff()
        self.assertTrue(result)

    def test_check_student(self):
        result = check_students.Check(self.driver).check_students()
        self.assertTrue(result)

    def test_admit_student(self):
        result = admit_students.register(self.driver).regist()
        self.assertTrue(result)

    def test_create_clue_order(self):
        result = Create_clue_order.Create_clue_order(self.driver).Create_clue_order()
        self.assertTrue(result)

    def test_Create_student_order(self):
        result = Create_student_order.Create_student_order(self.driver).Create_student_order()
        self.assertTrue(result)

    def test_student_charge(self):
        result = student_charge.Charge(self.driver).charge()
        self.assertTrue(result)

    def test_delete_clue(self):
        Delete_clue.Delete_clue(self.driver).delete_clue()

    def tearDown(self):
        self.driver.close()
        print("用例执行结束")

    @classmethod
    def tearDownClass(self) -> None:
        print("测试结束")
        self.driver.quit()


if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_UI("test_login"))
    suite.addTest(Test_UI("test_add_clue"))
    suite.addTest(Test_UI("test_add_PC_clue"))
    suite.addTest(Test_UI("test_add_clue_phone"))
    suite.addTest(Test_UI("test_add_staff"))
    suite.addTest(Test_UI("test_check_student"))
    suite.addTest(Test_UI("test_admit_student"))
    suite.addTest(Test_UI("test_create_clue_order"))
    suite.addTest(Test_UI("test_Create_student_order"))
    suite.addTest(Test_UI("test_delete_clue"))
    time_name=str(time.strftime("%m-%d_%H-%M-%S", time.localtime())).strip(" ")
    report_name=time_name+"全日智冒烟测试结果.html"
    report_path = os.path.dirname(os.getcwd()) + "\\Report\\"+report_name
    picture_name = datetime.datetime.now().strftime("%Y{y}%m{m}%d{d}%H{h}%M{s}").format(y="年", m="月", d="日", h="时",
                                                                                       s="分", )
    report_picture = picture_name +"冒烟报告"
    with open(report_path,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title=report_picture,description="全日智GUI测试报告")
        result=runner.run(suite)
        print(result)
    f.close()
    piture_path=reboat_request.Reboat_request().html_to_img(report_path)
    reboat_request.Reboat_request().upload_img(piture_path)
    reboat_request.Reboat_request().reboat_upload_file(report_path)
    media_id = reboat_request.Reboat_request().reboat_upload_file(report_path)
    reboat_request.Reboat_request().reboat_fileadress(media_id)
