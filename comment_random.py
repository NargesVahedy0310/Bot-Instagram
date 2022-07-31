import time
import pandas
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
class comment:
    def __init__(self, username, password,time_rondom,value_search,comment_random,num_comment,num_post):
        self.driver = webdriver.Chrome("C:/Users/Narges/Desktop/test1/test1/chromedriver.exe")
        self.username = username
        self.password = password
        self.time_rondom = time_rondom
        self.value_search = value_search
        self.comment_random = comment_random
        self.num_comment = num_comment
        self.num_post = num_post
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
    def search_and_comment(self):
        driver=self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(time_rondom)
        not_now=driver.find_element(By.XPATH,'//*[@class="_a9-- _a9_1"]').click()
        num=0
        action=ActionChains(driver)
        while num < num_post:
            #search box
            search_box=driver.find_element(By.XPATH,'//*[@class="_aawf _aawg _aexm"]').click()
            time.sleep(time_rondom)
            search=random.choice(value_search)
            box_search= driver.find_element(By.XPATH,'//*[@aria-label="Search input"]')
            for c in search:
                r=random.uniform(0.1,1.5)
                time.sleep(r)
                box_search.send_keys(c)
            time.sleep(time_rondom)
            menu_search=driver.find_element(By.XPATH,'//*[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _abm4 _a6hd"]').click()
            time.sleep(6)
            #post
            driver.implicitly_wait(15)
            posts=driver.find_elements(By.CLASS_NAME,"_aagv")
            count=0
            for p in posts:
                if count<=3:
                    action.click(p)
                    action.perform()
                    time.sleep(time_rondom)
                    radom_comment=random.choice(comment_random)
                    #comment
                    comments=driver.find_element(By.XPATH,'//*[@class="_aao9"]//*[@class="_ablz _aaoc"]').click()
                    time.sleep(3)
                    number=0
                    while number<num_comment:
                        time.sleep(5)
                        text_comment=driver.find_element(By.XPATH,'//*[@class="_aao9"]//*[@class="_ablz _aaoc focus-visible"]')
                        for c in radom_comment:
                            r=random.uniform(0.1,1.5)
                            time.sleep(r)
                            text_comment.send_keys(c)
                        time.sleep(3)
                        comment_send=driver.find_element(By.XPATH,'//*[@type="submit"]').click()
                        time.sleep(4)
                        number+=1
                    driver.back()
                    count+=1
time_rondom=random.randint(2,5)
num_comment=2
num_post=3
comment_random=['wow','omg','Woow','Woow!!!','omg!!!']
value_search=['#programing','#برنامه_نویسی','#python',]
username='username'
password='password'
test=comment(username, password,time_rondom,value_search,comment_random,num_comment,num_post)
test.Login()
test.search_and_comment()
