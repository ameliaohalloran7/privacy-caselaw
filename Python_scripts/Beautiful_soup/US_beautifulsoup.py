from bs4 import BeautifulSoup

# OBJECTIVE:
# INPUT: A set of files in the folder ../../Intermediate_files/US_downloads, one file for each case.
# OUTPUT: A set of files in the folder ../../Case_downloads/US, one file for each case with only the trial content extracted.

case_ID = 1

for i in range(2254):
	with open("Intermediate_files/US_downloads/" + str(case_ID) + "US_original.txt") as f:
		soup = BeautifulSoup(f.read(), 'html.parser')
	div_content1 = soup.find('div', id='caselaw-content') # In US cases, the case content is in the class caselaw-content.
	if div_content1 != None:
		text1 = div_content1.get_text() # Text is extracted from the specified div class 
	with open("Case_downloads/US/" + str(case_ID) + "US.txt", 'w') as g:
		print(text1, file=g) # Print extracted text to file
	case_ID += 1 # Move on to next case