import pandas as pd
import numpy as np
import os

os.makedirs('../data/processed', exist_ok=True)

def preprocess_data():
    # Загрузка сырых данных
    tiobe = pd.read_csv('../data/raw/tiobe_2024.csv')
    pypl = pd.read_csv('../data/raw/pypl_2024.csv')
    historical = pd.read_csv('../data/raw/historical_2019_2023.csv')
    
    # Очистка и преобразование данных
    tiobe_clean = tiobe[['language', 'rating', 'year']].rename(columns={'rating': 'popularity'})
    tiobe_clean['popularity'] = tiobe_clean['popularity'].astype(float)
    
    pypl_clean = pypl[['language', 'share', 'year']].rename(columns={'share': 'popularity'})
    pypl_clean['popularity'] = pypl_clean['popularity'].astype(float)
    
    # Нормализация названий языков
    def normalize_lang_names(df):
        df['language'] = df['language'].str.replace('C#', 'CSharp')
        df['language'] = df['language'].str.replace('C++', 'CPP')
        return df
    
    tiobe_clean = normalize_lang_names(tiobe_clean)
    pypl_clean = normalize_lang_names(pypl_clean)
    historical = normalize_lang_names(historical)
    
    # Сохранение обработанных данных
    tiobe_clean.to_csv('../data/processed/tiobe_processed.csv', index=False)
    pypl_clean.to_csv('../data/processed/pypl_processed.csv', index=False)
    historical.to_csv('../data/processed/historical_processed.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
    print("Data preprocessing completed!")
