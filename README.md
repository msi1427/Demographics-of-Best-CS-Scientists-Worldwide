# Demographics-of-Best-CS-Scientists-Worldwide

## Build From Sources
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

## Analytics
Tableau Public View: https://public.tableau.com/app/profile/mohammad.sabik.s.irbaz/viz/DemographicsofBestCSScientistsWorldwide/Dashboard1
