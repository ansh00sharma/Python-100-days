import requests
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
from bs4 import BeautifulSoup
import re
import pandas as pd

load_dotenv()

url = "https://appbrewery.github.io/Zillow-Clone/"
form_link = ""

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_links = []
all_prices = []
all_address = []

# For getting all links to property
all_li = soup.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

for item in range(len(all_li)):
    div = all_li[item].find('div', class_='StyledPropertyCardDataWrapper')
    a_tag = div.find('a', class_="StyledPropertyCardDataArea-anchor")
    href_value = a_tag.get('href')
    trimmed_href = href_value.strip()
    all_links.append(trimmed_href)

# For getting all prices of property
    a_tag = div.find('div' ,class_='StyledPropertyCardDataArea-fDSTNn')
    span_tag = div.find('span', class_= 'PropertyCardWrapper__StyledPriceLine')
    price = span_tag.text
    trimmed_price = price.strip()
    numerical_value = trimmed_price.split("/")[0].split("+")[0]
    all_prices.append(numerical_value)


# For getting all Address of property
    a_tag = div.find('address')
    address = a_tag.text
    trimmed_address = address.strip()
    all_address.append(trimmed_address)
    

data = pd.DataFrame(columns = ["A", "P", "L"])
data['A'] = all_address
data['P'] = all_prices
data['L'] = all_links

print("all data scrapped !")

options = Options()
options.add_experimental_option("detach", True)
movies = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


for item in range(len(data)):

    driver.get(form_link)

    address_fill = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address_fill.send_keys(data['A'][item])

    price_fill = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_fill.send_keys(data['P'][item])

    link_fill = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_fill.send_keys(data['L'][item])

    submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()


driver.quit()
