#coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from handle.element_handle import Get_elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Find_elements:
    def __init__(self,driver):
        self.ge=Get_elements()
        self.driver=driver
    def find_element(self,page,element,number=None):
        elemets = self.ge.get_element(page, element)
        element = elemets.split(">")[1]
        type = elemets.split(">")[0]
        if number==None:
            try:
                if type=="id":
                     return self.driver.find_element_by_id(element)
                elif type=="class":
                    return self.driver.find_element_by_class_name(element)
                elif type=="xpath":
                    return self.driver.find_element_by_xpath(element)
                elif type=="link":
                    return self.driver.find_element_by_partial_link_text(element)
                elif type=="css":
                    return self.driver.find_element_by_css_seletor(element)
                elif type=="tag":
                    return self.driver.find_element_by_tag_name(element)
                else:
                    return self.driver.find_element_by_name(element)
            except:
                return None
        else:
            try:
                if type == "id":
                    return self.driver.find_elements_by_id(element)[number]
                elif type == "class":
                    return self.driver.find_elements_by_class_name(element)[number]
                elif type == "xpath":
                    return self.driver.find_elements_by_xpath(element)[number]
                elif type == "link":
                    return self.driver.find_elements_by_partial_link_text(element)[number]
                elif type == "css":
                    return self.driver.find_elements_by_css_seletor(element)[number]
                elif type == "tag":
                    return self.driver.find_elements_by_tag_name(element)[number]
                else:
                    return self.driver.find_elements_by_name(element)[number]
            except:
                return None
    def wait_element(self,page,element):
        elemets = self.ge.get_element(page, element)
        element = elemets.split(">")[1]
        type = elemets.split(">")[0]
        if type == "id":
            elemnt_loacte=(By.ID,element)
        elif type == "class":
            elemnt_loacte=(By.CLASS_NAME,element)
        elif type == "xpath":
            elemnt_loacte=(By.XPATH,element)
        elif type == "link":
            elemnt_loacte=(By.LINK_TEXT,element)
        elif type == "css":
            elemnt_loacte=(By.CSS_SELECTOR,element)
        elif type == "tag":
            elemnt_loacte=(By.TAG_NAME,element)
        else:
            elemnt_loacte=(By.NAME,element)
        WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(elemnt_loacte))
    def wait_element_click(self,page,element):
        elemets = self.ge.get_element(page,element)
        element = elemets.split(">")[1]
        type = elemets.split(">")[0]
        if type == "id":
            elemnt_loacte = (By.ID, element)
        elif type == "class":
            elemnt_loacte = (By.CLASS_NAME, element)
        elif type == "xpath":
            elemnt_loacte = (By.XPATH, element)
        elif type == "link":
            elemnt_loacte = (By.LINK_TEXT, element)
        elif type == "css":
            elemnt_loacte = (By.CSS_SELECTOR, element)
        elif type == "tag":
            elemnt_loacte = (By.TAG_NAME, element)
        else:
            elemnt_loacte = (By.NAME, element)
        WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(elemnt_loacte))
    def father_son_element(self,page1,element1,page2,element2,number1=None,number2=None):
        father_elements=self.ge.get_element(page1,element1)
        son_elements=self.ge.get_element(page2,element2)
        father_element = father_elements.split(">")[1]
        father_type = father_elements.split(">")[0]
        son_element = son_elements.split(">")[1]
        son_type = son_elements.split(">")[0]
        if number1 == None:
            try:
                if father_type == "id":
                    father_action= self.driver.find_element_by_id(father_element)
                elif father_type == "class":
                    father_action= self.driver.find_element_by_class_name(father_element)
                elif father_type == "xpath":
                    father_action= self.driver.find_element_by_xpath(father_element)
                elif father_type == "link":
                    father_action= self.driver.find_element_by_partial_link_text(father_element)
                elif father_type == "css":
                    father_action= self.driver.find_element_by_css_seletor(father_element)
                elif father_type == "tag":
                    father_action= self.driver.find_element_by_tag_name(father_element)
                else:
                    father_action= self.driver.find_element_by_name(father_element)
            except:
                return None
        else:
            try:
                if father_type == "id":
                    father_action=self.driver.find_elements_by_id(father_element)[number1]
                elif father_type == "class":
                    father_action=self.driver.find_elements_by_class_name(father_element)[number1]
                elif father_type == "xpath":
                    father_action=self.driver.find_elements_by_xpath(father_element)[number1]
                elif father_type == "link":
                    father_action=self.driver.find_elements_by_partial_link_text(father_element)[number1]
                elif father_type == "css":
                    father_action=self.driver.find_elements_by_css_seletor(father_element)[number1]
                elif father_type == "tag":
                    father_action=self.driver.find_elements_by_tag_name(father_element)[number1]
                else:
                    father_action=self.driver.find_elements_by_name(father_element)[number1]
            except:
                return None
        if number2 == None:
            try:
                if son_type == "id":
                    return father_action.find_element_by_id(son_element)
                elif son_type == "class":
                    return father_action.find_element_by_class_name(son_element)
                elif son_type == "xpath":
                    return father_action.find_element_by_xpath(son_element)
                elif son_type == "link":
                    return father_action.find_element_by_partial_link_text(son_element)
                elif son_type == "css":
                    return father_action.find_element_by_css_seletor(son_element)
                elif son_type == "tag":
                    return father_action.find_element_by_tag_name(son_element)
                else:
                    return father_action.find_element_by_name(son_element)
            except:
                return None
        else:
            try:
                if son_type == "id":
                    return father_action.find_elements_by_id(son_element)[number2]
                elif son_type == "class":
                    return father_action.find_elements_by_class_name(son_element)[number2]
                elif son_type == "xpath":
                    return father_action.find_elements_by_xpath(son_element)[number2]
                elif son_type == "link":
                    return father_action.find_elements_by_partial_link_text(son_element)[number2]
                elif son_type == "css":
                    return father_action.find_elements_by_css_seletor(son_element)[number2]
                elif son_type == "tag":
                    return father_action.find_elements_by_tag_name(son_element)[number2]
                else:
                    return father_action.find_elements_by_name(son_element)[number2]
            except:
                return None
