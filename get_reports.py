import datetime
import os
import time
import subprocess
import sys

#check for updates
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])

#update chromedriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#user and pass
User = "my_user"
Pass = "my_pass"

#dates
today = date.today()
seven_days_back = int(today.day) - 7
Big_week = today - datetime.timedelta(days=7)
year = datetime.date.today().year


#Paths
full_path = os.getcwd()
spl_word = "Desktop\\Nintendo"
rel_path = full_path.partition(spl_word)[0]

#Requests to get data
Requests = [
    ]

#Renaming reports
report_name = [ 
    
]

with driver as driver:
    #open and login
    wait = WebDriverWait(driver, 15)
    driver.get(my_url)
    driver.find_element(By.NAME, "loginid").send_keys(User)
    driver.find_element(By.NAME, "password").send_keys(Pass)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    
    time.sleep(30)

    #get reports and rename them
    for i, x in zip(Requests, report_name):
        
        driver.switch_to.new_window('tab')
        driver.get(str(i))
        driver.find_element(By.NAME, "downloadCsv").send_keys(Keys.RETURN)
        time.sleep(60)
        os.chdir(rel_path + "\\Downloads")
        print("op")
        while not os.path.exists("titleReport_" + str(Big_week.strftime("%Y-%m-%d")) + ".csv"):
            time.sleep(30)
            print('30 sec passed')
        if os.path.isfile("titleReport_" + str(Big_week.strftime("%Y-%m-%d")) + ".csv"):
            os.rename("titleReport_" + str(Big_week.strftime("%Y-%m-%d")) + ".csv", x)
        else:
            raise ValueError('No file')
        
        time.sleep(5)
    

print('The end')

