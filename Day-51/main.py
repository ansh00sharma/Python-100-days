from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import smtplib
import os


load_dotenv()

gmail = os.getenv("MY_GMAIL_ACCOUNT")
password = os.getenv("MY_GMAIL_PASSWORD")
address = os.getenv("MY_ADDRESS")
phone = os.getenv("MY_NUMBER")

options = Options()
options.add_experimental_option("detach", True)
movies = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.speedtest.net/")

time.sleep(5)

get_cookie = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button')
get_cookie.click()


get_speed = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
get_speed.click()

time.sleep(45)

# For checking if there is a pop up poster
try:
    close_poster = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
    close_poster.click()

# if Poster is not there directly scrap   
except:
    pass
    
finally:
    downlaod_speed = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    down = downlaod_speed.text

    upload_speed = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    up = upload_speed.text

    result_id =  driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]')
    id = result_id.text



message = f"I have taken a 6 month Internet Connection in {address}. The Plan I have Taken is for 100MBPS (download) why I am getting only {down}down/{up}up ???. This is the result ID = {id} you can confirm this by yourself on https://www.speedtest.net/result/id . If this issue is not resolved I have to take actions. Contact : {phone}"
print(message)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=gmail,password=password)
    connection.sendmail(from_addr=gmail, to_addrs="support@spirenetbroadband.com", msg=message)