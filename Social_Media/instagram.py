import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def my_profile():
    path = "Database\\Chromedriver.exe"
    os.system("taskkill /im chrome.exe /f")
    # os.system("taskkill /im msedgedriver.exe /f")
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/hp/AppData/Local/Google/Chrome/User Data")
    chrome_service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    wait = WebDriverWait(driver, 100)

    # my profile show
    # my_profile_path = '//*[@id="mount_0_0_2k"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div'
    my_profile_path = '//*[@id="mount_0_0_Z0"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div'
    my_profile = wait.until(EC.element_to_be_clickable((By.XPATH, my_profile_path)))
    my_profile.click()
    # time.sleep(10)

my_profile()


