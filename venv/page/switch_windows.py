#coding=utf-8
from handle.action import Action
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Switch_window:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.ha=Action(driver=self.driver)
    def window_switch(self):
         self.ha.open_url("http://tyysdk.tianyuyou.cn/agent.php/front/index/index.html")
         self.ha.click_action("Loginpage","open_service")
         n=self.driver.window_handles
         print(n)
         mywindow=self.driver.current_window_handle
         for i in n:
             if i!=mywindow:
                 self.driver.switch_to_window(mywindow)
                 time.sleep(3)
                 self.driver.switch_to_window(i)
                 time.sleep(2)
                 self.ha.shut_web_action()
if __name__=="__main__":
    sw=Switch_window()
    sw.window_switch()