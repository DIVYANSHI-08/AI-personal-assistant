import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def new_message():
    path = "Database\\Chromedriver.exe"
    os.system("taskkill /im chrome.exe /f")
    # os.system("taskkill /im msedgedriver.exe /f")
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/hp/AppData/Local/Google/Chrome/User Data")
    chrome_service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 100)
    text=""
    hour = int(datetime.now().hour)
    if hour>=8 and hour<=12:
        text = "Good morning "
    elif hour>12 and hour<18:
        text = "Good afternoon "
    else:
        text = "Good evening "
    text2 = "...How can I help you...this is Diana(auto generated reply)....please leave a message Rishabh sir will be get back to you shortly. Thanks!"
    time.sleep(10)
    namelist = ["Oreo","Divyanshi","Senapati"]
    new = []
    for name in namelist:
        getsearchbox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
        getsearchbox.click()
        time.sleep(2)
        getsearchbox.send_keys(name)
        time.sleep(5)
        unreadMsgs=False
        getlist=driver.find_elements_by_xpath("//div[@class ='_ahlk']")
        if(len(getlist)):
            unreadMsgs=True
        
        
        if not unreadMsgs:
            cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
            cutit.click()
        else:
            # print("first")
            user = name
            new.append(name)
            # user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
            cutit.click()
            time.sleep(1)
            # print("second")
            # search_path = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
            # search_box.click()
            search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
            search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
            search_box.send_keys(name + Keys.ENTER)
            time.sleep(1)
            # msg = driver.find_elements_by_xpath("//span[@class='_ao3e selectable-text copyable-text']") 
            # print(msg)
            # print("Third")
            print(name,"username!")
            message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            message_box = driver.find_element(By.XPATH, message_box_xpath)
            message_box.send_keys(text + name + text2 + Keys.ENTER)
            # message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
            # message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
            # message_box.send_keys(text + name + text2 + Keys.ENTER)
            print(name,"texted you!")
            time.sleep(2)
            # print("four")
            initial = "personal grp"
            search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
            search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
            search_box.send_keys(initial + Keys.ENTER)
            cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
            cutit.click()
            
    

    driver.quit()
    return new

# hello=[]
# hello = new_message()


# path = "Database\\Chromedriver.exe"
# os.system("taskkill /im chrome.exe /f")
# # os.system("taskkill /im msedgedriver.exe /f")
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:/Users/hp/AppData/Local/Google/Chrome/User Data")
# chrome_service = webdriver.chrome.service.Service(path)
# driver = webdriver.Chrome(service=chrome_service, options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# wait = WebDriverWait(driver, 100)
# text=""
# hour = int(datetime.now().hour)
# if hour>=8 and hour<=12:
#     text = "Good morning "
# elif hour>12 and hour<18:
#     text = "Good afternoon "
# else:
#     text = "Good evening "
# text2 = "...How can I help you...this is Diana(auto generated reply)....please leave a message Rishabh sir will be get back to you shortly. Thanks!"
# time.sleep(10)
# namelist = ["Oreo","Divyanshi","Senapati","Tanishka"]
# while(1):
#     for name in namelist:
#         getsearchbox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
#         getsearchbox.click()
#         time.sleep(2)
#         getsearchbox.send_keys(name)
#         time.sleep(5)
#         unreadMsgs=False
#         getlist=driver.find_elements_by_xpath("//div[@class ='_ahlk']")
#         if(len(getlist)):
#             unreadMsgs=True
        
        
#         if not unreadMsgs:
#             cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
#             cutit.click()
#         else:
#             # print("first")
#             user = name
#             # user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#             cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
#             cutit.click()
#             time.sleep(1)
#             # print("second")
#             # search_path = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
#             # search_box.click()
#             search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
#             search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
#             search_box.send_keys(name + Keys.ENTER)
#             time.sleep(1)
#             # msg = driver.find_elements_by_xpath("//span[@class='_ao3e selectable-text copyable-text']") 
#             # print(msg)
#             # print("Third")
#             print(name,"username!")
#             message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
#             message_box = driver.find_element(By.XPATH, message_box_xpath)
#             message_box.send_keys(text + name + text2 + Keys.ENTER)
#             # message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
#             # message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
#             # message_box.send_keys(text + name + text2 + Keys.ENTER)
#             print(name,"texted you!")
#             time.sleep(2)
#             # print("four")
#             initial = "personal grp"
#             search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
#             search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
#             search_box.send_keys(initial + Keys.ENTER)
#             cutit=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/div[2]/button")
#             cutit.click()
        
#         # getsearchbox.send_keys(Keys.CONTROL + "a"div)
#         # getsearchbox.send_keys(Keys.BACKSPACE)
    
#     # The code will run again after 3 seconds
#     time.sleep(3)
# driver.quit()

