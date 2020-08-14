#coding=utf-8
from handle.find_element import Find_elements
from handle.element_handle import Get_elements
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
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
        token = self.driver.execute_script('return localStorage.getItem("xgj_fulltime_session");')
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
    def switch_page(self,count):
        handles=self.driver.window_handles
        self.driver.switch_to_window(handles[count-1])
        return handles
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
    def father_son_input(self,page1,element1,page2,element2,data,number1=None,number2=None):
        self.fe.father_son_element(page1,element1,page2,element2,number1,number2).send_keys(data)
    #生成手机号码
    def createPhone(self):
        for k in range(10):
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                       "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                       "186", "187", "188", "189"]
            phone=random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
            return phone
    def GBK2312(self):
        # 随机生成名字最后一个字
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        last_name = bytes.fromhex(val).decode('gb2312')
        return last_name
    #生成姓名
    def create_name(self):  # 随机生成名字
        first_name_list = [
            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        n = random.randint(0, len(first_name_list) - 1)
        first_name = first_name_list[n]
        # 随机取数组中字符，取到空字符则没有second_name
        second_name_list = [self.GBK2312(), '']
        n = random.randint(0, 1)
        second_name = second_name_list[n]
        last_name=self.GBK2312()
        name = first_name + second_name + last_name
        return name
if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get(url="https://schooltest.xiaogj.com")
