#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
class Change_ifrane_learn:
    def __init__(self):
        self.driver=webdriver.Chrome()
    def learn_change_iframes(self):
        self.driver.get("https://ke.qq.com/")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"js_login")))
        self.driver.find_element_by_id("js_login").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btns-enter-qq")))
        self.driver.find_element_by_class_name("btns-enter-qq").click()
        self.driver.switch_to_frame("login_frame_qq")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "switcher_plogin")))
        self.driver.find_element_by_id("switcher_plogin").click()
        time.sleep(2)
        self.driver.close()
if __name__=="__main__":
    ci=Change_ifrane_learn()
    ci.learn_change_iframes()
