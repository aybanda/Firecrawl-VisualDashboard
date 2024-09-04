import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Initialize FirecrawlApp with the API key
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

# Set up the Streamlit app
st.title('Web Content Visualization Dashboard')

# Sidebar for user input
st.sidebar.header('User Input')
url = st.sidebar.text_input('Enter URL to scrape:')
scrape_button = st.sidebar.button('Scrape Data')

if scrape_button and url:
    try:
        with st.spinner('Scraping data...'):
            # Scrape the URL
            result = firecrawl_app.scrape_url(url, params={'formats': ['html']})
            html_content = result.get('html', '')

            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract text content from paragraphs
            paragraphs = soup.find_all('p')
            text_content = [p.get_text() for p in paragraphs]

            # Create a DataFrame
            df = pd.DataFrame({'paragraph': text_content})
            df['word_count'] = df['paragraph'].apply(lambda x: len(x.split()))

            # Display the data
            st.subheader('Scraped Data Overview')
            st.write(df)

            # Visualizations
            st.subheader('Word Count Distribution')
            fig, ax = plt.subplots()
            sns.histplot(data=df, x='word_count', kde=True, ax=ax)
            ax.set_xlabel('Word Count')
            ax.set_ylabel('Frequency')
            st.pyplot(fig)

            # Basic statistics
            st.subheader('Basic Statistics')
            st.write(df['word_count'].describe())

            # Top 10 longest paragraphs
            st.subheader('Top 10 Longest Paragraphs')
            st.write(df.nlargest(10, 'word_count'))

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Firecrawl API key status
st.sidebar.subheader('Firecrawl API Status')
if firecrawl_api_key:
    st.sidebar.success('Firecrawl API key is set')
else:
    st.sidebar.error('Firecrawl API key is not set')