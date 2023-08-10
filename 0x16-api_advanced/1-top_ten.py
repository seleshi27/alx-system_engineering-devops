#!/usr/bin/python3
import requests


def top_ten(subreddit):
    '''Finds and prints the titles of the first 10 host posts'''

    header = {'User-Agent':  'Chrome/66.0.3359.139 Mobile Safari/537.36'}
    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        hot_list = response.json()["data"]["children"]

        counter = 0
        for hot in hot_list:
            if counter == 10:
                break
            print(hot["data"]["title"])
            counter += 1
    else:
        print("None")
