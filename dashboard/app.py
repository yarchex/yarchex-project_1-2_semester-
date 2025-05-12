import streamlit as st
import pandas as pd
import plotly.express as px

# Загрузка данных
@st.cache_data
def load_data():
    return pd.read_csv('../data/processed/full_processed.csv')

df = load_data()

# Настройка страницы
st.set_page_config(page_title="Языки программирования", layout="wide")
st.title("Анализ популярности языков программирования (2019-2024)")

# Сайдбар с фильтрами
st.sidebar.header("Фильтры")
selected_years = st.sidebar.multiselect(
    "Выберите годы",
    options=df['year'].unique(),
    default=df['year'].unique()
)

selected_langs = st.sidebar.multiselect(
    "Выберите языки",
    options=df['language'].unique(),
    default=['Python', 'JavaScript', 'Java', 'CSharp', 'CPP']
)

# Фильтрация данных
filtered_df = df[
    (df['year'].isin(selected_years)) & 
    (df['language'].isin(selected_langs))
]

# Основная панель
tab1, tab2, tab3 = st.tabs(["Динамика", "Сравнение", "Выводы"])

with tab1:
    st.header("Динамика популярности")
    fig = px.line(
        filtered_df, 
        x='year', 
        y='popularity', 
        color='language',
        markers=True,
        title='Изменение популярности по годам'
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Сравнение языков")
    year_to_compare = st.selectbox(
        "Выберите год для сравнения",
        options=sorted(selected_years)
    )
    
    compare_df = filtered_df[filtered_df['year'] == year_to_compare]
    fig = px.bar(
        compare_df,
        x='language',
        y='popularity',
        title=f'Популярность языков в {year_to_compare} году'
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Ключевые выводы")
    st.markdown("""
    1. **Python** сохраняет лидерство с 2019 года
    2. **JavaScript** стабильно в топ-3
    3. **Rust** показывает наибольший рост (+15% за 5 лет)
    4. **Java** постепенно теряет популярность (-8% с 2019)
    5. **Go** вошел в топ-10 в 2022 и продолжает расти
    """)
    
    st.download_button(
        label="Скачать данные",
        data=df.to_csv().encode('utf-8'),
        file_name='programming_languages_popularity.csv',
        mime='text/csv'
    )
