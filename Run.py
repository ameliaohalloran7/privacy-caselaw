import rpy2.robjects as robjects
import os
import argparse
import shutil

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--install_r_packages", help="'True' installs R packages 'knitr' and 'markdown'. If you have these packages installs, select 'False'. If you do not have these packages installed, select 'True'.", default=False)
parser.add_argument("--redownload_case_files", help="'True' deletes all downloaded original HTML files for US, UKSC, and UKHL cases and re-downloads them, which takes a significant amount of time. If you do not want to redownload these files, select 'False.' If you do want to redownload, select 'True'.", default=False)

# Parse the command-line arguments
args = parser.parse_args()


# If case files have to be redownloaded
if(args.redownload_case_files):

    # Determine directories from which files should be deleted
    original_US_files = os.listdir("Intermediate_files/US_downloads")
    original_UKHL_files = os.listdir("Intermediate_files/UKHL_downloads")
    original_UKSC_files = os.listdir("Intermediate_files/UKSC_downloads")
    intermediate_UKHL_files = os.listdir("Intermediate_files/UKHL_parsed")
    intermediate_UKSC_files = os.listdir("Intermediate_files/UKSC_parsed")
    downloaded_US_files = os.listdir("Case_downloads/US")
    downloaded_UKHL_files = os.listdir("Case_downloads/UKHL")
    downloaded_UKSC_files = os.listdir("Case_downloads/UKSC")

    # Delete each file
    for original_US_file in original_US_files:
        print(original_US_file)
        os.remove(os.path.join("Intermediate_files/US_downloads",original_US_file))
    for original_UKHL_file in original_UKHL_files:
        os.remove(os.path.join("Intermediate_files/UKHL_downloads",original_UKHL_file))
    for original_UKSC_file in original_UKSC_files:
        os.remove(os.path.join("Intermediate_files/UKSC_downloads",original_UKSC_file))
    for intermediate_UKHL_file in intermediate_UKHL_files:
        os.remove(os.path.join("Intermediate_files/UKHL_parsed",intermediate_UKHL_file))
    for intermediate_UKSC_file in intermediate_UKSC_files:
        os.remove(os.path.join("Intermediate_files/UKSC_parsed",intermediate_UKSC_file))
    for downloaded_US_file in downloaded_US_files:
        os.remove(os.path.join("Case_downloads/US",downloaded_US_file))
    for downloaded_UKHL_file in downloaded_UKHL_files:
        os.remove(os.path.join("Case_downloads/UKHL",downloaded_UKHL_file))
    for downloaded_UKSC_file in downloaded_UKSC_files:
        os.remove(os.path.join("Case_downloads/UKSC",downloaded_UKSC_file))


    # Runs selenium scripts, which downloads HTML data for each case
    with open("Python_scripts/Selenium/US_selenium.py", "r") as file: # Run US selenium script
        exec(file.read())
    with open("Python_scripts/Selenium/UKHL_selenium.py", "r") as file: # Run UKHL selenium script
        exec(file.read())
    with open("Python_scripts/Selenium/UKSC_selenium.py", "r") as file: # Run UKSC selenium script
        exec(file.read())

# Runs beautiful soup scripts, which extracts text from HTML data
print("Step 1 of 6: Running US HTML parser")
with open("Python_scripts/Beautiful_soup/US_beautifulsoup.py", "r") as file: # Run US beautiful soup script
    exec(file.read())
print("Step 2 of 6: Running UKHL HTML parser")
with open("Python_scripts/Beautiful_soup/UKHL_beautifulsoup.py", "r") as file: # Run UKHL beautiful soup script
    exec(file.read())
print("Step 3 of 6: Running UKSC HTML parser")
with open("Python_scripts/Beautiful_soup/UKSC_beautifulsoup.py", "r") as file: # Run UKSC beautiful soup script
    exec(file.read())

# Runs intermediate processing scripts, which:
    # Gets rid of unnecessary header/footer info in UKSC 
    # Aggregates all pages for a single case into a single file for UKHL
print("Step 4 of 6: Running UKHL aggregator")
with open("Python_scripts/Intermediate_processing/UKHL_file_aggregator.py", "r") as file: # Run UKHL file aggregating script
    exec(file.read())
print("Step 5 of 6: Running UKSC trimmer")
with open("Python_scripts/Intermediate_processing/UKSC_trimming.py", "r") as file: # Run UKSC file trimming script
    exec(file.read())



print("Step 6 of 6: Running R Markdown file")

# If install_r_packages = true
if(args.install_r_packages):
    robjects.r("options(repos = 'https://cran.rstudio.com/')")
    robjects.r("install.packages('knitr')")
    robjects.r("install.packages('rmarkdown')")


# Knit the R Markdown file
robjects.r(f"""
    library(knitr)
    library(rmarkdown)
    env <- Sys.getenv("RSTUDIO_PANDOC")
    Sys.setenv(RSTUDIO_PANDOC=env)
    render('Comparative_analysis.Rmd', output_format = 'html_document')
""")
   

