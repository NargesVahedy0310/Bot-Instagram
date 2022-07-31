import time
import pandas
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
class comment:
    def __init__(self, username, password,list_massags,list_username,dict_show):
        self.driver = webdriver.Chrome("C:/Users/Narges/Desktop/test1/test1/chromedriver.exe")
        self.username = username
        self.password = password
        self.list_massags =list_massags
        self.list_username = list_username
        self.dict_show=dict_show
    def Login(self):
        driver=self.driver
        action=ActionChains(driver)
        driver.get('https://www.instagram.com/accounts/login/?next=/accounts/')
        driver.maximize_window()
        time.sleep(2)
        for u in username:
            r=random.uniform(0.1,1.5)
            time.sleep(r)
            box_username=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(u)
        time.sleep(time_rondom)
        for p in password:
            r=random.uniform(0.1,1.5)
            time.sleep(r)
            box_username=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(p)
        time.sleep(time_rondom)
        btn_login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
        save_info=driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        time.sleep(5)
        direct=driver.find_element(By.XPATH,'//*[@aria-label="Direct messaging - 0 new notifications link"]').click()
        time.sleep(time_rondom)
        not_now=driver.find_element(By.XPATH,'//*[@class="_a9-- _a9_1"]').click()
        time.sleep(time_rondom)
        massage_account=driver.find_element(By.XPATH,'//*[@class=" _ab8s _ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm"]').click()
        time.sleep(time_rondom)
        account=driver.find_elements(By.XPATH,'//*[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _abm4 _abyi _a6hd"]')
        
        for a in account:
            
            action.click(a)
            action.perform()
            time.sleep(4)

        #save name
        # name=driver.find_elements(By.XPATH,'//*[@class="_aacl _aaco _aacu _aacx _aada"]//*[@class="_aacl _aaco _aacu _aacx _aada"]')
        # for u in name:
        #     list_username.append(u.text)
        # print(list_username)
            
        # #save massage
        # massages=driver.find_elements(By.XPATH,'//*[@class="_aacl _aaco _aacu _aacx _aad6 _aade"]')
        # for m in massages:
        #     list_massags.append(m.text)
        # print(list_massags)
        # dict_show = {'username':list_username,'massage one account':list_massags }
        # data = pandas.DataFrame.from_dict(dict_show, orient='index')
        # data = data.transpose()
        # test1 = pandas.ExcelWriter("project1.xlsx")
        # data.to_excel(test1)
        # test1.save()
        
time_rondom=random.randint(2,5)
list_massags=[]
list_username=[]
dict_show={}
username='seleneium_0311'
password='selenium'
test=comment(username, password,list_massags,list_username,dict_show)
test.Login()