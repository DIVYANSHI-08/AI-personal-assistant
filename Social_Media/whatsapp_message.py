# pip (package install python)

# import pickle
from Body.Speak import Speak
from Body.Listen import MicExecution
import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def whatsapp_message(username,text="defualt",s="default",gender="sir"):
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
    search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
    search_box.send_keys(username + Keys.ENTER)
    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
    message_box.send_keys(text + Keys.ENTER)
    while True:
        Speak(f'{gender}, should I close whatsapp say exit sir?')
        answer = MicExecution(s).lower()
        if "exit" in answer:
            break
        Speak(f'OK {gender},to whom you want to sent message next')
        username = MicExecution(s).lower()
        Speak(f'OK {gender},what you want to send to {username}')
        text = MicExecution(s).lower()
        Speak(f"sending message to {username} wait for a while {gender}!!")
        # path 
        search_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, search_path)))
        search_box.send_keys(username + Keys.ENTER)
        # message box 
        message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
        message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
        message_box.send_keys(text + Keys.ENTER)

def new_status():
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

    # status check
    status_check_path = '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[1]/div[4]/div/span'
    status_check = wait.until(EC.element_to_be_clickable((By.XPATH, status_check_path)))
    status_check.click()
    time.sleep(10)
    #new check
    

# new_status()
# whatsapp_message('Oreo','Hey',"Rishabh", "sir")


























# path = "Database\\msedgedriver.exe"
# ser = Service(path)
# options = webdriver.EdgeOptions()
# try:
#     # options.add_argument("--enable-chrome-browser-cloud-management")
#     options.add_argument("user-data-dir=C:/Users/hp/AppData/Local/Microsoft/Edge/User Data")
#     driver = webdriver.Edge(path, options=options)
#     driver.maximize_window()
#     driver.get("https://web.whatsapp.com/") 
# except Exception as e:
#     print("Error loading cookies:", e)







# time.sleep(10)
# print(driver.get_cookies())
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
# try:
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#         print("Error "+cookie)
#     print("Cookies add successfully")
# except FileNotFoundError:
#     print("No previous session found. Please log in manually.")
# except Exception as e:
#     print("Error loading cookies:", e)
# time.sleep(10)
# driver.get("https://web.whatsapp.com/") 
















# import time

## opening amazon and searching laptop category
# path = "DataBase\\msedgedriver.exe"
# driver = webdriver.Edge(path)
# driver.maximize_window()
# driver.get("https://www.amazon.in/")
# search = driver.find_element_by_id("twotabsearchtextbox")
# search.send_keys("laptop")
# search.send_keys(Keys.RETURN)

# main = driver.find_element_by_id("main")
# print(main.text)



# print(driver.page_source)  #entire source code of the page will be print
# time.sleep(5)

# print(driver.title)
# driver.quit()



# click on particular text in website
# path = "DataBase\\msedgedriver.exe"
# driver = webdriver.Edge(path)
# driver.maximize_window()
# driver.get("https://www.amazon.in/")
# link = driver.find_element_by_link_text("Sell")
# link.click()
# driver.back() #going back
# driver.forward() #going forward in website



# # cookie clicker website
# from selenium.webdriver.common.action_chains import ActionChains
# path = "DataBase\\msedgedriver.exe"
# driver = webdriver.Edge(path)
# driver.maximize_window()
# driver.get("https://orteil.dashnet.org/cookieclicker/")
# driver.implicitly_wait(5)
# cookie = driver.find_element_by_id("bigCookie")
# cookie_count = driver.find_element_by_id("cookies")
# # product_price = driver.find_element_by_id("")
# items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]
# actions = ActionChains(driver)
# actions.click()
# for i in range(5000):
#     actions.perform()
#     count = int(cookie_count.text.split(" ")[0])
#     for item in items:
#         value = int(item.text)
#         if value <= count:
#             upgrade_actions = ActionChains(driver)
#             upgrade_actions.move_to_element(item)
#             upgrade_actions.click()
#             upgrade_actions.perform()








