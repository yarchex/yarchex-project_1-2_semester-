import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_stackoverflow():
    base_url = "https://stackoverflow.com/questions/tagged/"
    languages = ['python', 'javascript', 'java', 'c++', 'go', 'rust']
    data = []
    
    for lang in languages:
        url = f"{base_url}{lang}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        count = soup.find('div', class_='fs-body3').get_text(strip=True).split()[0]
        data.append({'language': lang, 'source': 'StackOverflow', 'count': int(count.replace(',', '')), 'date': datetime.now().strftime('%Y-%m-%d')})
        time.sleep(2)
    
    return pd.DataFrame(data)

def save_data(df, filename):
    os.makedirs('../data/raw', exist_ok=True)
    df.to_csv(f'../data/raw/{filename}', index=False)

if __name__ == "__main__":
    so_data = scrape_stackoverflow()
    save_data(so_data, 'stackoverflow_questions.csv')
    print("Data collection completed!")
