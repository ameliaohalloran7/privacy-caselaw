from bs4 import BeautifulSoup

# OBJECTIVE:
# INPUT: A set of files in the folder ../../Intermediate_files/UKSC_downloads, one file for each case.
# OUTPUT: A set of files in the folder ../../Intermediate_files/UKSC_parsed, one file for each case with only the text extracted.


case_ID = 1

for i in range(898):
	with open("Intermediate_files/UKSC_downloads/" + str(case_ID) + "UKSC_original.txt") as f:
		soup = BeautifulSoup(f.read(), 'html.parser') # Parses content of file and saves to soup
	div_content = soup.find('ol')  # UKSC HTML saved with text either in ol or body div class
	if div_content is None: # First checks if ol exists
		div_content = soup.find('body')  # If not found, find div with class body
	if div_content is not None: # If either ol or body exist
		text = div_content.get_text() # Get the text from the div class 
		with open("Intermediate_files/UKSC_parsed/" + str(case_ID) + "UKSC_parsed.txt", 'w') as g:
			print(text, file=g)
	else:
		print("Div with class ol or body not found" + str(case_ID)) # Error checking
	case_ID += 1 # Move on to next case 