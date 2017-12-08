from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
cheshi = client['cheshi']
url_list = client['url_list']

# 第一个爬虫：爬取

def get_links_from(channel,pages,who_sells=0):
    list_view = ''
