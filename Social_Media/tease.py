import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def tease(name="default",n=0,temp="defualt"):
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
        
        # search name 
    # username = "Oreo"
    # search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
    # search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
    # search_box.send_keys(username + Keys.ENTER)
        # time.sleep(1)
        # target = f"{username}"
        # contact path search
        # Xpath ='//tagname[contains(@Atrribut,'+ target +')]'
        # contact_path = '//span[contains(@title,'+ target +')]'
        # contact = wait.until(EC.presence_of_all_elements_located((By.XPATH,contact_path)))
        
        # contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))
        # contact.click()

        # message send
    while n!=0:
        username = name
        search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
        search_box.send_keys(username + Keys.ENTER)
        # search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        # search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
        # search_box.send_keys(username + Keys.ENTER)
        text = temp
        message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        message_box = driver.find_element(By.XPATH, message_box_xpath)
        message_box.send_keys(text + Keys.ENTER)
        # message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
        # message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
        # message_box.send_keys(text + Keys.ENTER)
        n-=1
        time.sleep(2)

