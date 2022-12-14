# Demographics-of-Best-CS-Scientists-Worldwide

## Problem Statement
The goal of this project is to gather information of best 1000 Computer Science researchers from this website: https://research.com/scientists-rankings/computer-science
Later we utilized the scraped data to understand the following demographics and correlations using Tableau Dashboard: 

1. A barchart of countries with average publications.
2. European countries with the number of scientists in a map (excluding Russia)
3. Which Middle Eastern universities are good at research? (using citations as metric)
4. Which column is directly correlated with World Rank column? We wanted to understand how the ranking was done.

You can visit the public dashboard here: https://public.tableau.com/app/profile/mohammad.sabik.s.irbaz/viz/DemographicsofBestCSScientistsWorldwide/Dashboard1

## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone https://github.com/msi1427/Demographics-of-Best-CS-Scientists-Worldwide.git
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads 
5. Run the scraper
```bash
python selenium_scraper/scraper.py --chromedrive_path <path_to_chromedriver>
```
6. You will get a file named `best_cs_scientist_details.csv` containing all the required fields. 
Alternatively, check our scraped data here: https://github.com/msi1427/Demographics-of-Best-CS-Scientists-Worldwide/blob/main/selenium_scraper/best_cs_scientist_details.csv

