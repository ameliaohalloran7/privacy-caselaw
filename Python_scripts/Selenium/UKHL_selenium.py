import urllib.request
import requests
from selenium import webdriver
import csv



# OBJECTIVE: Extract HTML data from all UKHL cases, downloading a file for each page of each UKHL case.
# INPUT: UKHL_cases.csv
# OUTPUT: A set of files in the folder ../../Intermediate_files/UKHL_downloads, one file for each page of each case.


# Import list_of_urls from the UKHL CSV. If a different date range is to be used, the CSV should be updated, and the changes will be reflected here. 
with open('Input_files/UKHL_Cases.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Create a list of URLs
    list_of_urls = []
    for row in reader:
        list_of_urls.append(row[2])


# Initializing two variables: case_ID and page_ID. Each case_ID represents a unique UKHL case. 
	# Some cases are only one page long, meaning the entire case opinion can be pulled from a single webpage. 
	# However, some cases require the user to move on to a next page. In these cases, the page_ID represents each unique page for a case.
	# This file is intended to download each page for each case. A separate file, UKHL_aggregator.py, combines the pages for each case into a single case file.

case_ID = 0
page_ID = 1

for url in list_of_urls: # Go through url list 
	case_ID += 1 # Increase case_ID by 1, meaning it moves to the next case
	page_ID = 1 # Reset page_ID to begin at 1 for each new case
	while True: # The following loop will run until the next page isn't found for the case, at which point a break will be thrown.  
		if "-1.htm" in url: # Cases with multiple pages have first-page URLs that end with -1.htm. Cases without multiple pages do not have this ending. 
			new_url = url[:-5] + str(page_ID) + ".htm" # Removes last 5 characters of URL and replaces it with page_ID. For example, x-1.htm will become x-2.htm if page_ID is currently set to 2. 
			driver = webdriver.Chrome()  # Opens chrome browser
			driver.get(new_url) # Opens new_url in chrome browser
			html = driver.page_source # Pulls html data from new_url
			if "Page cannot be found" in html: #If the page doesnt exist
				driver.quit() #Quit the page
				break # Break, meaning that we move on to the next case_ID
			else: # If the page does exist
				with open("Intermediate_files/UKHL_downloads/" + str(case_ID) + "UKHL_original" + str(page_ID) + ".txt", 'w') as f: # Open a file 
					print(html, file=f) # Write the html data to the opened file 
				driver.quit() # Quit the page
				page_ID += 1 # Increment page_ID, moving on to check the next page of the case
		else: # Cases without multiple pages will follow this conditional
			driver = webdriver.Chrome()  # Opens chrome browser
			driver.get(url) #Opens url 
			html = driver.page_source # Pulls html data from url
			with open("Intermediate_files/UKHL_downloads/" + str(case_ID) + "UKHL_original" + str(page_ID) + ".txt", 'w') as f: # Open a file
				print(html, file=f) # Write the html data to the opened file
			driver.quit() # Quit the page
			break # Break, meaning that we move on to the next case_ID

	
	

  