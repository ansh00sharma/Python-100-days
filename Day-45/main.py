from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
movies = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.empireonline.com/movies/features/best-movies-2/")

get_name = driver.find_elements(By.XPATH, '//div[@class="listicle_listicle__item__CJna4"]/h3')

for item in get_name:
    movies.append(item.text)


movies.reverse()

for item in movies:
    print(item)

