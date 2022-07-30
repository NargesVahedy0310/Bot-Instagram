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
    def __init__(self, username, password,time_rondom):
        self.driver = webdriver.Chrome("C:/Users/Narges/Desktop/test1/test1/chromedriver.exe")
        self.username = username
        self.password = password
        self.time_rondom = time_rondom
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
        driver.get('https://www.instagram.com/explore/tags/programinglife/')
    def post_instgram(self):
        driver=self.driver
        post=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'_aagv')))
        action=ActionChains(driver)
        action.click(post)
        action.perform()
        like=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="_abl-"]//*[@aria-label="Like"]')))
        time.sleep(4)
        action=ActionChains(driver)
        action.click(like)
        action.perform()
time_rondom=random.randint(2,5)
username='username'
password='password'
test=bot(username, password,time_rondom)
test.Login()
test.post_instgram()