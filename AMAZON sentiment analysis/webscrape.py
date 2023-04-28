# Importing necessary libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

data = []


#scraping
for page in range(1,21): # iterate through 20 pages
    url = f'https://www.amazon.in/s?k=gaming+laptops&page={page}&crid=UXJ95A8PSI3E&sprefix=gaming+lapt%2Caps%2C604&ref=nb_sb_noss_2'
    headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        try:
            product_name = product.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').text.strip()
            price = product.find('span', class_='a-price').find('span', class_='a-offscreen').text.split('₹')[1].strip()
            actual_price_span = product.find('span', class_='a-price a-text-price')
            actual_price = actual_price_span.find('span', class_='a-offscreen').text.split('₹')[1].strip()  if  actual_price_span else price
            discount_div = product.find('div', class_='a-row a-size-base a-color-base')
            discount_percentage = discount_div.text.strip().split("(")[1].split("%")[0].strip() if discount_div and '%' in discount_div.text.strip() else "0"
            rating_div = product.find('div', class_='a-row a-size-small')
            if rating_div is not None:
                rating_div_spans = rating_div.find_all('span')
                for tag in rating_div_spans:
                    if 'stars' in tag.text:
                        rating = tag.text.strip('out')[0].strip()
                    else:
                        count = tag.text
            else:
                rating = '0'
                count =  '0'
              
            product_link = product.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']
            product_links = 'https://www.amazon.in/' + product_link
            url = 'https://www.amazon.in/' + product_link
            response_product = requests.get(url, headers=headers)
            soup_product = BeautifulSoup(response_product.text, 'html.parser')
            soup_review_div = soup_product.find('div', {'data-hook': 'top-customer-reviews-widget'})
            if soup_review_div is not None:
                soup_review = soup_review_div.find_all('div',{'data-hook' : 'review','class' :'a-section review aok-relative'})
                for contents in soup_review:
                    review= contents.find('div', {'data-hook' : 'review-collapsed'}).text.strip()
                    reviewer = contents.find('span', class_= 'a-profile-name').text.strip()
                    review_date = contents.find('span', {'data-hook': 'review-date'}).text.split('on')[1].strip()
                    review_head= contents.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').span.text.strip()
                    data.append([product_name, price, actual_price, discount_percentage,rating, count,review, reviewer, review_date, review_head])
                    
            else:
                review = reviewer = review_date = review_head = 'No review'
                data.append([product_name, price, actual_price, discount_percentage,rating, count,review, reviewer, review_date, review_head])   
            
            product_name
        except Exception as e:
            print(product_name,e)
            continue
#creating data frame
columns = ['Name', 'Price', 'Actual Price', 'Discount','Rating','Count','review', 'reviewer', 'review_date', 'review_title']
df = pd.DataFrame(data, columns=columns)
df.to_csv('Laptops_amazon.csv')
