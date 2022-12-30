import requests
import csv
from bs4 import BeautifulSoup

class RedditScraper:
    def __init__(self, subreddit, thread_id):
        # Set the subreddit name and thread ID as instance variables
        self.subreddit = subreddit
        self.thread_id = thread_id
        # Set the user agent as a class variable
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'}
        # Initialize an empty dictionary to store the thread data
        self.thread_data = {}

    def scrape_thread(self):
        # Make a GET request to the thread URL
        response = requests.get(f'https://www.reddit.com/r/chennai/comments/z8u42i/what_do_you_guys_think_about_people_who_feed/', headers=self.headers)
        # Check the status code of the response to make sure the request was successful
        if response.status_code == 200:
            data_str = ""
            # Parse the HTML of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the subreddit name
            for item in self.thread_data['subreddit'] : soup.find('a', class_="_2wzi-W7JiZ7A6U6aFvfvSR").text
            data_str = data_str + item
            # Extract the thread title
            self.thread_data['thread_title'] = soup.find('h1', class_="_eYtD2XCVieq6emjKBH3m").text
            # Extract the number of upvotes
            self.thread_data['upvotes'] = soup.find('div', class_='_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo _2iiIcja5xIjg-5sI4ECvcV').text
            # Extract the number of comments
            self.thread_data['comments'] = soup.find('span', class_="FHCV02u6Cp2zYL0fhQPsO")
            # Extract the image or video URL
            image_or_video = soup.find('div', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax')
            if image_or_video:
                if image_or_video.find('img'):
                    # Extract the URL of the image
                    self.thread_data['image_or_video_url'] = image_or_video.find('img')['src']
                elif image_or_video.find('video'):
                    # Extract the URL of the video
                    self.thread_data['image_or_video_url'] = image_or_video.find('video')['src']
        # If the request was not successful, print an error message
        else:
            print('Error:', response.status_code)

    def write_to_csv(self):
    # Open the CSV file in write mode
     with open('redditgahana.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object
        writer = csv.writer(csv_file)
        # Write the column names to the CSV file
        writer.writerow(['subreddit', 'thread_title', 'upvotes', 'comments', 'image_or_video_url'])
        for key, value in self.thread_data.items():
            # Write the key-value pair to the CSV file as a row
            writer.writerow([key, value])