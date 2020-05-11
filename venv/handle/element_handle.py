#coding=utf-8
import configparser
class Get_elements:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read("../config\elements.ini")
    def get_element(self,page,element):
        data=self.cf.get(page,element)
        return data
if __name__=="__main__":
    ge=Get_elements()
    print(ge.get_element("Loginpage","username"))
