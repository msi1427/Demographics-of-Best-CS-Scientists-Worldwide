from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--chromedrive_path', type=str, help="Check where the Chromedriver is in your PC and share the path")
args = parser.parse_args()

columns = ["World Rank", "National Rank", "Name", "Image URLs", "Affiliation", "Country", "H-Index", "Citations", "#DBLP"]

def get_scholar_details(row):
    details = row.text.split('\n')
    contents = {}
    contents["World Rank"] =    details[0]
    contents["National Rank"] = details[1]
    contents["Name"] =          details[2]
    contents["Affiliation"] =   details[3].split(',')[0]
    contents["Country"] =       details[3].split(',')[1].strip()
    contents["H-Index"] =       details[4]
    contents["Citations"] =     details[5].replace(',','')
    contents["#DBLP"] =         details[6].replace(',','')
    contents["Image URLs"] =    row.find_element(By.CLASS_NAME, 'lazyload').get_attribute('src')
    return contents


def main():
    webdriver_path = parser.chromedrive_path
    scholar_data = []

    for page_id in range(1,11): 
        driver = webdriver.Chrome(webdriver_path)
        url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
        driver.get(url)
        rankings = driver.find_element(By.ID, 'rankingItems')
        rows = rankings.find_elements(By.CLASS_NAME, 'cols')
        for idx, row in enumerate(rows):
            if idx % 4 == 0:
                scholar_data.append(get_scholar_details(row))
        driver.close()

    df = pd.DataFrame(data=scholar_data, columns=columns)
    df.to_csv("best_cs_scientist_details.csv", index=False)
    return

if __name__ == "__main__":
    main()