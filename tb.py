import csv
import json
from io import BytesIO  # Not using

import apscheduler
import requests
import tweepy
from bs4 import BeautifulSoup
from PIL import Image
from twitter import OAuth, Twitter  # Not using


# Authenticate to Twitter
with open("details.csv") as file:
    csvContent = csv.DictReader(file)
    for content in csvContent:
        auth = tweepy.OAuthHandler(content['API Key'], content['API Key Secret'])
        auth.set_access_token(content['Access Token'], content['Access Token Secret'])
        api = tweepy.API(auth)
        
        try:
            api.verify_credentials()
            print("Authentication Successful")
        except Exception as e:
            print(e)
            print("Authentication Error")

                                    # Reading TimeLine
                                    # time_line = api.home_timeline()
                                    # for the_tweet in time_line:  
                                    #     print(f"{the_tweet.user.name} said {the_tweet.text}") 

                                    # api.update_status("This is a test tweet to learn Tweepy Python") 
        quote_raw = requests.get('https://api.quotable.io/random')
        quote = quote_raw.json()
        api.update_status(f"{quote['content']} \n\t\t\t - {quote['author']}")        

