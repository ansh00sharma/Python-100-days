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

options = Options()
options.add_experimental_option("detach", True)
movies = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.amazon.in/Chuwi-HeroBook-Pro-Windows-Mini-HDMI/dp/B0CP9TFVK4/ref=sr_1_3?keywords=laptop&sr=8-3&th=1")

time.sleep(10)

get_price = driver.find_element(By.XPATH, '//span[@id="tp_price_block_total_price_ww"]/span[1]')
text = get_price.text

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=gmail,password=password)
    connection.sendmail(from_addr=gmail, to_addrs=gmail, msg=f"latop price is {text}")
