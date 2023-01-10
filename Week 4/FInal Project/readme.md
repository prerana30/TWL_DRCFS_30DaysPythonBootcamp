# Welcome to week 4 of the bootcamp.

  This is my final project in which I have scrapped the sub reddit of a reddit. I chose this subreddit: https://www.reddit.com/r/chennai/comments/z8u42i/what_do_you_guys_think_about_people_who_feed/ .

I had to make a bot to scrape data from Reddit and do the following operations: 
1. Extract the subreddit name, thread title, no.of upvotes, no. comments in the thread
and image or video URL in the thread
2. Store the extracted values in the filename ‘redditgahana.csv’
3. Your program or file should use python Class, methods, constructors, class variables,
and private variables. You can use any kind of method to scrape data either selenium or bs4.

This is how we can scrape any subthread of a reddit:

# 1. We need to first visit the subreddit and inspect it.
# 2. |For example: If you want to want to see title you can just right click near title of that specific subreddit and you will get the following information:
![Alt text](../../../../../Pictures/Screenshots/Screenshot%20(368).png)

Yeah! you got to know
you can find title in h1 of  class_='_eYtD2XCVieq6emjKBH3m '

# 3. Now start to code by first importing necessary libraries, in our code by importing :
from bs4 import BeautifulSoup
import csv
import time

You may wonder why do we import time.  Scraping a website can generate a large number of requests, and if we send requests too quickly, the website's servers may become overloaded. Using time.sleep() to add a delay between requests can help to prevent this.

# 4. Then we define a class called RedditScraper that is used to scrape data from a Reddit thread which has following attributes:
 'url': Url of thread will be scraped. This attribute is initialised with value passed to _init_ method when instance of class is created.
 'subreddit' , 'title' , 'upvotes' ,'comments' , 'content' and 'media' initialised with an empty string.
 and 'thread_data' a dictionary which contain the scraped data for the thread which is also initialised with an empty dictionary.
  # NOTE: URL attribute is initialised with value passed to _init_ method when instance of class is created.

# 5 
# i.The first line of the scrape() method 
sets the value of the headers variable to a dictionary containing a user agent string. 
# ii. (requests module)
to send a GET request to the URL specified in the self.url attribute of the RedditScraper instance.
# iii. (Exception handling) 
try block in this code is used to handle any exceptions that may occur while making the request to the URL or parsing the HTML content of the page. The except block specifies which exceptions to handle and what action to take when an exception occurs. 

# 6. Extracting the data ,I am going to describe the code of extracting title only.
title_element = soup.find('h1' class_='_eYtD2XCVieq6emjKBH3m')
In this code, find() method of BeautifulSoup object to search for an HTML element with tag name and CSS class which we have already analysed before in #1.

# Then in this code :
 if title_element:
 self.title = title_element.text
 If the title_element variable is not None, this code assigns the text content of the element to the title attribute of the RedditScraper instance.

 # NOTE: .text for extracting the text content of an HTML element so, for upvotes count we need to convert it into integer.

# 7.In this code: This code defines a method called to_csv that writes the data of a RedditScraper instance to a CSV file. 
  def to_csv(self, filename):
   with open(filename, 'a') as file:
   file.write(f"{self.subreddit},{self.title},{self.upvotes},{self.comments},{self.media}\n") 
The method takes a single argument, filename, which is the name of the CSV file to write to.'a' opens the file in append mode ,and writes the data to the file using the write() method. Scraped datas are stored respectively. For example title in self.title.

# 8. FinaLLY !!!!
WE creates an instance of the RedditScraper class, using the URL 'https://www.reddit.com/r/chennai/comments/z8u42i/what_do_you_guys_think_about_people_who_feed/' as the argument. The instance is stored in the scraper variable.

Then, the scrape() method of the scraper object is called to scrape the data from the  URL.

Finally, the to_csv() method of the scraper object is called to write the scraped data to a CSV file named 'redditgahana.csv'.

# i HOPE YOU FIND THIS USEFUL.Thank you :)