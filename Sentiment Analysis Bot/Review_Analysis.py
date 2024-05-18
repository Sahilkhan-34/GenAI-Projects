import requests
import streamlit as st 
import google.generativeai as genai
from bs4 import BeautifulSoup

st.title("Reviews Scraping and Sentiment Analysis")
url = st.text_input("Enter The Review link", "")

def movies_reviews(url):
    reviews = []
    headers = {
        'User-Agent': 'Use your own user agent',
        'Accept-Language': 'en-us,en;q=0.5'
    }

    page_url = url
    page = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # names = soup.find_all('p', class_='_2NsDsF AwS1CA')
    # titles = soup.find_all('h3', itemprop="name")
    # ratings = soup.find_all('div', class_=['XQDdHH Ga3i8K', 'XQDdHH Czs3gR Ga3i8K' , 'XQDdHH Js30Fc Ga3i8K'])
    comments = soup.find_all('div', class_='content')

    for comment in zip(comments):
        review_data_dict = {}
        # review_data_dict['reviewer_name'] = name.get_text()
        # review_data_dict['review_title'] = title.get_text()
        # review_data_dict['rating'] = rating.get_text() if rating else '0'
        review_data_dict['review_text'] = comment[0]

        reviews.append(review_data_dict)

    return reviews




button  = st.button("Response")
if button:
    review = movies_reviews(url)
    st.write(review)

