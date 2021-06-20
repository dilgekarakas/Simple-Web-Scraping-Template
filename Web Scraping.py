from selenium import webdriver
import time
import pandas as pd


url='https://www.trustradius.com/machine-learning'

all_titles = []
all_ratings = []

for i in range(5):
    search_url = url+'?f='+str(25*i)
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\dilge\Downloads\chromedriver_win32 (1)\chromedriver.exe") #Path to Chrome Driver
    driver.get(search_url)
    
    time.sleep(10)
    
    temp_list_title = driver.find_elements_by_xpath('//h3[@class="CategoryProduct_card-product-title__1qXZD"]')
    temp_list_rating = driver.find_elements_by_xpath('//div[@class="CategoryProduct_card-counts__3jInH"]/a')
    
    all_titles.extend([elem.get_attribute("title") for elem in temp_list_title])
    all_ratings.extend([elem.text for elem in temp_list_rating])
    driver.quit()


output = pd.DataFrame()
output['productName']=all_titles
output['ratings']=pd.Series(all_ratings)
