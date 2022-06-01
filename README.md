# Web-Scrap

A simple script that scraps the https://www.trustradius.com/machine-learning

My intention was to crawl name, number of reviews, stars and urls of logos of each product categorized under machine learning solutions on trustradius.com. The url I have worked on is: https://www.trustradius.com/machine-learning. Once I landed on the url you will see a list of products by scrolling a little bit down. My task was to collect relevant information about each product and put them in an output file in the csv format. 

## For Anaconda Users

If you need to install Selenium with Pip, use this in your command line.
```
pip install Selenium
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Selenium needs a webdriver to work with your browser.

- To install Selenium Webdriver, just go to [Seleniumhq.org](https://Seleniumhq.org/) and go to “Third Party Browser Drivers” section.

- Click on “Google Chrome Driver” . If you use Mozilla, just install Mozilla GeckoDriver (or any other browser that you use).

- Click on the latest stable release.

- Download the correct version for your operating system. 

- Unzip the folder (You will need the destination of folder)

- Go back to Anaconda Prompt and type python.

- Import Selenium Webdriver

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For webdriver.Chrome(executable_path=...) you will need to write the destination of Google Chrome Driver (name of the file is chromedriver.exe for Windows Users).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

StarScraping needs the output csv of Web Scraping.py
