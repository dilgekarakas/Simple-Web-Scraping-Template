from selenium import webdriver #For webscraping 
import time #For waiting 
import pandas as pd


url='https://www.trustradius.com/machine-learning' #Define the URL 

all_titles = [] #Creating a list for titles
all_ratings = [] #Creating a list for ratings

for i in range(5): #Looking through all pages to gather all the Machine Learning titles and ratings
    search_url = url+'?f='+str(25*i) #Defining the pages of Machine Learning website 
    
    driver=webdriver.Chrome(executable_path=r"C:\Users\dilge\Downloads\chromedriver_win32 (1)\chromedriver.exe") #Path to Chrome Driver
    #When the code goes to Cloud for production we should define the webdriver's destination and we might need other configurations.
    
    driver.get(search_url) #Open the webpage
    
    time.sleep(10) # Wait for 10 seconds so that we can see everything.
    
    # Find the titles by defining the class name and h3 with selenium function find_elements_by_xpath
    temp_list_title = driver.find_elements_by_xpath('//h3[@class="CategoryProduct_card-product-title__1qXZD"]') 
    # Find the ratings by defining the class name and div with selenium function find_elements_by_xpath
    temp_list_rating = driver.find_elements_by_xpath('//div[@class="CategoryProduct_card-counts__3jInH"]/a')
    
    all_titles.extend([elem.get_attribute("title") for elem in temp_list_title]) #Load the list with title objects
    all_ratings.extend([elem.text for elem in temp_list_rating]) #Load the list with rating objects
    driver.quit() #Close the browser

output = pd.DataFrame() #Create the output dataframe

#Adding the columns
output['productName']=all_titles 
output['ratings']=pd.Series(all_ratings)