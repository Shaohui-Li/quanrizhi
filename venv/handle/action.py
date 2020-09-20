#coding=utf-8
from handle.find_element import Find_elements
from handle.element_handle import Get_elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import datetime


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
    def isElementExist(self,page,pageelement):#确认元素是否存在
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
    def switch_page(self,count):#切换页面
        handles=self.driver.window_handles
        self.driver.switch_to_window(handles[count-1])
        return handles
    def wait_action(self,seconds):#强制等待
        time.sleep(seconds)
    def wait_element_show(self,page,element):#等待元素出现
        self.fe.wait_element(page,element)
    def wait_element_click(self,page,element):
        self.fe.wait_element_click(page,element)
    def wait_Recessive(self):#隐性等待
        self.driver.implicitly_wait(10)
    def mouse_menu(self,page,element,number=None):#鼠标移动
        yuansu=self.fe.find_element(page,element,number)
        ActionChains(self.driver).move_to_element(yuansu).perform()
    def father_son_mouseaction(self,page1,element1,page2,element2,number1=None,number2=None):
        yuansu = self.fe.father_son_element(page1,element1,page2,element2,number1=None,number2=None)
        ActionChains(self.driver).move_to_element(yuansu).perform()
    def father_son_click(self,page1,element1,page2,element2,number1=None,number2=None):
        self.fe.father_son_element(page1,element1,page2,element2,number1,number2).click()
    def father_son_input(self,page1,element1,page2,element2,data,number1=None,number2=None):
        self.fe.father_son_element(page1,element1,page2,element2,number1,number2).send_keys(data)
    def father_son_text(self,page1,element1,page2,element2,number1=None,number2=None):
        return self.fe.father_son_element(page1,element1,page2,element2,number1,number2).text
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

    def data_input(self,page,element,number):
        """日期输入前置操作，去掉readonly属性  仅适用于PC端"""
        elemets=self.ge.get_element(page,element)
        element = elemets.split(">")[1]
        type = elemets.split(">")[0]
        if number==None:
            try:
                if type=="id":
                     js1 = "document.getElementById('%s').removeAttribute('readonly')"%(element)
                elif type=="class":
                    js1 = "document.getElementsByClassName('%s').removeAttribute('readonly')"%(element)
            except:
                return None
        else:
            try:
                if type == "class":
                    js1 = "document.getElementsByClassName('%s')[%d].removeAttribute('readonly')"%(element,number)
            except:
                return None
        self.driver.execute_script(js1)

    def scroll_page(self,page,element,number):
        """页面滑动"""
        page_element=self.fe.find_element(page,element,number)
        self.driver.execute_script("arguments[0].scrollIntoView();", page_element)

    def page_scroll(self,page, element, number):
        """页面tab键  元素必须是输入框才可以使用"""
        self.fe.find_element(page, element, number).send_keys(Keys.TAB)

    def ident_generator(self):
        # 身份证号的前两位，省份代号
        province = ('11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35',
                    '36', '37', '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63',
                    '64', '65', '71', '81', '82')
        # 第3-第6位为市和区的代码。这里傻瓜式的设置为随机4位数(我知道这里没有0000-0999)
        district = random.randint(1000, 9999)
        # 第7-第14位出生的年月日的代码，这里设置的是，大于等于18岁左右，小于68岁左右
        birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(6500, 25000)))
        # 第15-第16位为户籍所在地派出所。这里傻瓜式的设置为随机2位数
        police_station = random.randint(10, 99)
        # 第17位性别
        gender = random.randrange(0, 9, 1)

        # 拼接出身份证号的前17位
        ident = province[random.randint(0, 33)] + str(district) + birthdate.strftime("%Y%m%d") + str(
            police_station) + str(gender)

        # 将前面的身份证号码17位数分别乘以不同的系数，系数见coe，然后将这17位数字和系数相乘的结果相加。用加出来和除以11，看余数是多少？
        coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,
               17: 2}
        summation = 0

        # ident[i:i+1]使用的是python的切片获得每位数字
        for i in range(17):
            summation = summation + int(ident[i:i + 1]) * coe[i + 1]

        # 用余数对照key得到校验码，比如余数为2，则校验码（第18位）为X
        key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        check_code = key[summation % 11]
        return ident + check_code
    def registration_number(self):
        """生成学籍号"""
        num = random.randint(1000000, 10000000)
        capa = chr(random.randint(65, 90))
        capb = chr(random.randint(65, 90))
        vercode = capa + capb + str(num)
        return vercode
if __name__=="__main__":
    driver = webdriver.Chrome()
    # driver.get(url="https://schooltest.xiaogj.com")
    print(Action(driver).ident_generator())
    print(Action(driver).registration_number())

