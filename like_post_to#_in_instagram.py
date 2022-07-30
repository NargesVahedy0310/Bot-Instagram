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
class bot():
    def __init__(self, username, password,time_rondom,value_search):
        self.driver = webdriver.Chrome("C:/Users/Narges/Desktop/test1/test1/chromedriver.exe")
        self.username = username
        self.password = password
        self.time_rondom = time_rondom
        self.value_search = value_search
    def Login(self):
        driver=self.driver
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
        time.sleep(7)
        save_info=driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        time.sleep(5)
        search_box=driver.find_element(By.XPATH,'//div[@class=" QY4Ed P0xOK"]').click()
        time.sleep(time_rondom)
        search=random.choice(value_search)
        box_search= driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search)
        time.sleep(time_rondom)
        menu_search=driver.find_element(By.XPATH,'//div[@class="uo5MA   _2ciX tWgj8 XWrBI "]//a[@class="-qQT3"]').click()
    def post_instgram(self):
        driver=self.driver
        action=ActionChains(driver)
        driver.implicitly_wait(15)
        posts=driver.find_elements(By.CLASS_NAME,"_aagv")
        count=0
        for p in posts:
            if count<=3:
                action.click(p)
                action.perform()
                time.sleep(time_rondom)
                if driver.find_element(By.XPATH,'//*[@class="_aamw"]//*[@aria-label="Like"]'):
                    like=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="_aamw"]//*[@class="_abl-"]')))
                    action.click(like)
                    action.perform()
                    driver.back()
                elif driver.find_element(By.XPATH,'//*[@class="_aamw"]//*[@aria-label="Unlike"]'):
                    time.sleep(time_rondom)
                    driver.back()
                count+=1
            else:
                break
time_rondom=random.randint(2,5)
value_search=['#programing','#برنامه_نویسی','#python']
username='username'
password='password'
test=bot(username, password,time_rondom,value_search)
test.Login()
test.post_instgram()