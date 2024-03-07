# OBJECTIVE: Aggregate all files of the same case_ID into a single file.
# INPUT: A set of files in the folder ../../Intermediate_files/UKHL_parsed, one file for each page of each case.
# OUTPUT: A set of files in the folder ../../Case_downloads/UKHL, one file for each case.

case_ID = 1
page_ID = 1

for i in range(781): # Total number of UKHL cases in this timeframe 
	while True: # Runs for each case_ID. Loops until there are no pages left for a single case_ID.
		try: 
			with open("Intermediate_files/UKHL_parsed/" + str(case_ID) + "UKHL_parsed" + str(page_ID) + ".txt") as f: # Opens the file for specified page_ID
				contents = f.read() # Reads in the file
			with open("Case_downloads/UKHL/" + str(case_ID) + "UKHL.txt", "a") as g: # Opens the aggregated file to which this text will be appended 
				print(contents, file = g) # Appends text into aggregated file
			page_ID += 1 # Moves to next page of case
		except FileNotFoundError: # If page does not exist
			page_ID = 1 # Set the page_ID back to 1 to move on to the first page of the next case
			case_ID += 1 # Move on to the next case
			break