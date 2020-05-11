#coding=utf-8
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
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located(elemnt_loacte))
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