import urllib.request
import requests
from selenium import webdriver
import os 
import csv

# OBJECTIVE: Extract HTML data from all US cases, downloading a file for each page of each US case.
# INPUT: US_cases.csv
# OUTPUT: A set of files in the folder ../../Intermediate_files/US_downloads, one file for each each case.

wd = os.getcwd() 

# Import list_of_urls from the US CSV. If a different date range is to be used, the CSV should be updated, and the changes will be reflected here. 
with open('Input_files/US_Cases.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a list of URLs
    list_of_urls = []
    for row in reader:
        list_of_urls.append(row[2])

case_ID = 0
for url in list_of_urls: # Go through url list
	case_ID += 1
	driver = webdriver.Chrome()  # Opens chrome browser
	driver.get(url) # Opens url in chrome browser
	html = driver.page_source # Get the page source after it has fully loaded
	with open("Intermediate_files/US_downloads/" + str(case_ID) + "US_original.txt", 'w') as f:
 		print(html, file=f) # Write the html data to the opened file
	driver.quit()  # Close the browser
