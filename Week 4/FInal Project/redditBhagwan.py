import requests
from bs4 import BeautifulSoup
import csv
import time

class RedditScraper:
    def __init__(self, url):
        self.url = url
        self.subreddit = " "
        self.title = ""
        self.upvotes =""
        self.comments =""
       
        self.content =""
        self.media  = ""
        self.thread_data = {}
    
    def scrape(self):
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            # Send a GET request to the URL
            page = requests.get(self.url,headers = headers)
            time.sleep(5)

            # Parse the HTML content of the page
            soup = BeautifulSoup(page.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return

        # Extract the subreddit name from the page
        subreddit_element = soup.find('span', class_='_2wzi-W7JiZ7A6U6aFvfvSR')
        if subreddit_element:
            self.subreddit = subreddit_element.text

        # Extract the thread title from the page
        title_element = soup.find('h1', class_='_eYtD2XCVieq6emjKBH3m')
        if title_element:
            self.title = title_element.text

        # Extract the number of upvotes from the page
        upvotes_element = soup.find('div', class_='_23h0-EcaBUorIHC-JZyh6J')
        if upvotes_element:
            self.upvotes = int(upvotes_element.text)
           

        # Extract the number of comments from the page
        comments_element = soup.find('span', class_='FHCV02u6Cp2zYL0fhQPsO')
        if comments_element:
            self.comments = comments_element.text

        # Extract the content of the thread
        content_element = soup.find('div', class_='_3AStxql1mQsrZuUIFP9xSg s1y8gf4b-0 gXUyBJ')
        if content_element:
            self.content = content_element.text
        
        media_url = soup.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax')
        self.media = media_url.get('src') if media_url else None

    def to_csv(self, filename):
     with open(filename, 'a') as file:
            file.write(f"{self.subreddit},{self.title},{self.upvotes},{self.comments},{self.media}\n")
  

# Create a RedditScraper object with the given URL
scraper = RedditScraper('https://www.reddit.com/r/chennai/comments/z8u42i/what_do_you_guys_think_about_people_who_feed/')

# Scrape the data from the page
scraper.scrape()

# Write the data to a CSV file
scraper.to_csv('redditgahana.csv')