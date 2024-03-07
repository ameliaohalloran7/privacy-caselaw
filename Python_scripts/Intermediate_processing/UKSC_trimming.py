# OBJECTIVE:
# INPUT: A set of files in the folder ../../Intermediate_files/UKSC_parsed, one file for each case with only the text extracted.
# OUTPUT: A set of files in the folder ../../Case_downloads/UKSC, one file for each case with only the necessary trial content extracted (Removed header/footer).


# trim_file function is intended to cut off the header and footer of UKSC files. 
# When a header and footer appears, the main content begins with JUDGMENT and ends with BAILII.
# Therefore, the trimming begins and ends at these two points.
def trim_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        found_judgment = False

        # Iterate through each line in the input file
        for line in infile:
            if not found_judgment:
                if 'JUDGMENT' in line:
                    found_judgment = True
                    outfile.write(line)  # Start writing from 'JUDGMENT'

            elif found_judgment:
                if 'BAILII' in line:
                    break  # Stop writing at the first instance of 'BAILII'
                else:
                    outfile.write(line) 

        # If 'JUDGMENT' is not found, write the entire file
        if not found_judgment:
            infile.seek(0)  # Reset file pointer to the beginning
            outfile.write(infile.read())


case_ID = 1

for i in range(898):
    inf = "Intermediate_files/UKSC_parsed/" + str(case_ID) + "UKSC_parsed.txt" 
    outf = "Case_downloads/UKSC/" + str(case_ID) + "UKSC.txt" 
    trim_file(inf, outf)
    case_ID += 1