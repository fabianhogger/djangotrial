from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
# Create your views here.
def scrape():
    session=requests.Session()
    session.headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content=session.get(url,verify=False).content
    soup=BSoup(content)
