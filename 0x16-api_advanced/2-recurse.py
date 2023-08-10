#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''gives a listing for all the hot articles for a specific subreddit'''

    header = {'User-Agent':  'Chrome/66.0.3359.139 Mobile Safari/537.36'}
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        hot = response.json()["data"]["children"]
        after = response.json()["data"]["after"]
        if after is None:
            hot_list = get_children(hot, len(hot))
            return hot_list
        hot_list.append(recurse(subreddit, hot_list, after=after))
        hot_list = get_children(hot, len(hot))
    else:
        return None
    return hot_list


def get_children(hot_list, counter, return_list=[]):
    '''Gets the children from the data'''
    if counter == 0:
        return return_list
    return_list.append(hot_list[counter - 1]["data"]["title"])
    return (get_children(hot_list, counter - 1, return_list))
