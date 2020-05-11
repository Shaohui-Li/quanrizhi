#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome()
driver.get("https://ke.qq.com/")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"js_login")))
driver.find_element_by_id("js_login").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"btns-enter-qq")))
driver.find_element_by_class_name("btns-enter-qq").click()
driver.switch_to_frame("login_frame_qq")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"switcher_plogin")))
driver.find_element_by_id("switcher_plogin").click()
time.sleep(2)
driver.close()