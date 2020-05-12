#coding=utf-8
from handle.find_element import Find_elements
from handle.element_handle import Get_elements
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class Action:
    def __init__(self,driver):
        self.fe=Find_elements(driver)
        self.ge=Get_elements()
        self.driver=driver
    def open_url(self,url):#输入url
        self.driver.get(url)
    def click_action(self,page,element,number=None): # 点击操作
        self.fe.find_element(page,element,number).click()
    def input_action(self,page,element,data,number=None):#输入操作
        self.fe.find_element(page,element,number).send_keys(data)
    def clear_action(self,page,element,number=None):
        self.fe.find_element(page,element,number).clear()
    def save_screenshot_action(self,file_name):#保存截图
        self.driver.save_screenshot(file_name)
    def shut_web_action(self):#关闭浏览器
        self.driver.close()
    def get_token(self):#获取token
        token = self.driver.execute_script('return localStorage.getItem("token");')
        print(token)
        return token
    def get_sessionid(self):#获取sessionid
        sessionid = self.driver.execute_script('return localStorage.getItem("PHPSESSID");')
        print(sessionid)
        return sessionid
    def element_text(self,page,element,number=None):#获取元素文本内容
        return self.fe.find_element(page,element,number).text
    def isElementExist(self,page,pageelement):
        elemets = self.ge.get_element(page,pageelement)
        element = elemets.split(">")[1]
        type = elemets.split(">")[0]
        flag = True
        if type == "id":
            try:
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_id(element)
                return flag
            except:
                flag = False
                return flag
        elif type=="class":
            try:
                self.driver.find_element_by_class_name(element)
                return flag
            except:
                flag = False
                return flag
        elif type=="link":
            try:
                self.driver.find_element_by_partial_link_text(element)
                return flag
            except:
                flag = False
                return flag
        else:
            try:
                self.driver.find_element_by_name(element)
                return flag
            except:
                flag = False
                return flag
    def Switch_page(self,page_name):
        self.driver.switch_to_window(page_name)
    def wait_action(self,seconds):
        time.sleep(seconds)
    def wait_element_show(self,page,element):
        self.fe.wait_element(page,element)
    def wait_element_click(self,page,element):
        self.fe.wait_element_click(page,element)
    def wait_Recessive(self):#隐性等待
        self.driver.implicitly_wait(10)
    def mouse_menu(self,page,element,number=None):
        yuansu=self.fe.find_element(page,element,number)
        ActionChains(self.driver).move_to_element(yuansu).perform()
    def father_son_click(self,page1,element1,page2,element2,number1=None,number2=None):
        self.fe.father_son_element(page1,element1,page2,element2,number1,number2).click()
if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get(url="https://schooltest.xiaogj.com")
