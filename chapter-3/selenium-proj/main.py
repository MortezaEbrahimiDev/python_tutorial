from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# if msedgedriver.exe not in path
#      service=Service('msedgedriver.exe')

# if msedgedriver.exe in path
driver = webdriver.Edge()

driver.get('https://bing.com')


search_bar=driver.find_element(By.NAME,'q')

search_bar.send_keys('آموزش پایتون مکتب خونه')
search_bar.send_keys(Keys.ENTER)

print(driver.page_source)
soup=BeautifulSoup(driver.page_source)

all_h3=soup.find_all('h3')

for item in all_h3:
    print(item.text)

input()