from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os

application_path = os.getcwd()

website = 'https://www.thesun.co.uk/tech/'
driver_path = '/Users/nidesh/Desktop/datasci/chromedriver'
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

option = Options()
option.binary_location = brave_path
option.headless = True
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(service=service, options=option)
browser.get(website)


#The use of Xpath method to get the elements of the website titles, subtitles and links
titles = []
subtitles = []
links = []

#The below variables holds all the corresponding elements found
information = browser.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

#Iterating all required elements from "information" variable
for info in information:
    titles.append(info.find_element(by='xpath', value='./a/h3').text)
    subtitles.append(info.find_element(by='xpath', value='./a/p').text)
    links.append(info.find_element(by='xpath', value='./a').get_attribute('href'))

#Creating a dictionary
info_dict = {
    "title": titles,
    'subtitle': subtitles,
    "link": links
}

#Converting the dictionary to a dataframe
df_info = pd.DataFrame(info_dict)

#Converting the dataframe to CSV file
date_time = datetime.now()
date = date_time.strftime('%m-%d-%Y')
time = date_time.strftime('%X')
filename = f'{date}-technology.csv'
final_path = os.path.join(application_path, filename)
df_info.to_csv(final_path)

print(f'Successfully exported to CSV file at date {date} and time {time}.')
browser.quit()







 