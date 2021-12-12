from selenium import webdriver
import login_data as  user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time 


#used to auto install or find path for Chrome Driver in your device
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# path = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(path)

driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=D92825882E7CA0FC20EEEF0FBA3D5CC7.worker2&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/menulist.htm")

# driver.maximize_window()  if you want to maximize than remove comment 


Email = driver.find_element_by_id("user_id")
Email.send_keys(user.id)

Password = driver.find_element_by_id("password")
Password.send_keys(user.pswd)

#waiting  for Security Quesiton to load
try: 
    Sec_question = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.ID,"question"))
    )
    for key, value in user.Sec_que.items():
     if key == Sec_question.text:
         answer = value
         break
     else:
         continue                       
except:    
    driver.quit();


ans = driver.find_element_by_id("answer")
ans.send_keys(answer)

login = driver.find_element_by_id("loginFormSubmitButton")
print("getting login id")

login.click();
print("clicked")

#from this line we make script keep running
temp = input()



