from bs4 import BeautifulSoup

# OBJECTIVE:
# INPUT: A set of files in the folder ../../Intermediate_files/UKHL_downloads, one file for each page of each case.
# OUTPUT: A set of files in the folder ../../Intermediate_files/UKHL_parsed, one file for each page of each case with only the trial content extracted.

case_ID = 1
page_ID = 1

for i in range(781):
	while True: # Runs until no pages left for this case_ID
		try:
			with open("Intermediate_files/UKHL_downloads/" + str(case_ID) + "UKHL_original" + str(page_ID) + ".txt") as f: # Opens the original downloaded file
				soup = BeautifulSoup(f.read(), 'html.parser') # Parses content of file and saves to soup
			div_content = soup.find('div', id='maincontent')  # UKHL HTML saved with text either in maincontent, maincontent1, or contentholder div class
			if div_content is None: # First checks if maincontent exists 
				div_content = soup.find('div', id='maincontent1')  # If not found, find div with class maincontent1
			if div_content is None:
				div_content = soup.find('div', id='contentholder') 
			if div_content is not None: # If either maincontent or maincontent1 exist
				text = div_content.get_text() # Get the text from the div class 
				with open("Intermediate_files/UKHL_parsed/" + str(case_ID) + "UKHL_parsed" + str(page_ID) + ".txt", 'w') as g:
					print(text, file=g)
			page_ID += 1 # Moving to next page
		except FileNotFoundError: # If no page exists
			page_ID = 1 # Set page back to 1 before moving on to next case
			case_ID += 1 # Move on to next case 
			break # No pages left for this case_ID, break