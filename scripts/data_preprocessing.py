import pandas as pd
import os

def clean_data():
    raw_path = '../data/raw/'
    processed_path = '../data/processed/'
    os.makedirs(processed_path, exist_ok=True)
    
    dfs = []
    for file in os.listdir(raw_path):
        if file.endswith('.csv'):
            df = pd.read_csv(f"{raw_path}{file}")
            dfs.append(df)
    
    combined = pd.concat(dfs)
    combined = combined.drop_duplicates()
    combined = combined.dropna()
    
  combined.to_csv(f"{processed_path}programming_languages.csv", index=False)

if __name__ == "__main__":
    clean_data()
    print("Data preprocessing completed!")
