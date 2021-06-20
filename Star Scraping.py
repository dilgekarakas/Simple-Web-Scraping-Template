
from selenium import webdriver #For webscraping 
import time #For waiting 
import pandas as pd


url='https://www.trustradius.com/machine-learning' #Define the URL 

all_titles = [] #Creating a list for titles
all_ratings = [] #Creating a list for ratings

i = 0 #Looking through all pages to gather all the Machine Learning titles and ratings
search_url = url+'?f='+str(25*i) #Defining the pages of Machine Learning website 

driver=webdriver.Chrome(executable_path=r"C:\Users\dilge\Downloads\chromedriver_win32 (1)\chromedriver.exe") #Path to Chrome Driver
#When the code goes to Cloud for production we should define the webdriver's destination and we might need other configurations.

driver.get(search_url) #Open the webpage

time.sleep(10) # Wait for 10 seconds so that we can see everything.

templist = driver.find_elements_by_xpath('//div[@class="RatingStars_stars__3adCY RatingStars_small__2er70"]/div') 
star_symbols = [elem.get_attribute("class") for elem in templist]

grandlist=[]
for i in star_symbols:
    if i[-1]=='S': grandlist.append(1)
    if i[-1]=='2': grandlist.append(0.5)
    if i[-1]=='B': grandlist.append(0)
        
stars = np.array(grandlist).reshape(-1,5).sum(axis=1)
output = pd.read_csv('output.csv')
output['stars'] = pd.Series(stars)
output

