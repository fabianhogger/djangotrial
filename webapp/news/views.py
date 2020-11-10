from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from django.http import HttpResponse

# Create your views here.
def scrape(request):
    session=requests.Session()
    session.headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content=session.get(url,verify=True).content
    soup=BSoup(content,"html.parser")
    News=soup.find_all('article',{"class":"sc-1pw4fyi-7 gDJTEP js_post_item"})
    print('entered scrape')
    for article in News:
        print('entered loop')
        main=article.find_all('a')[0]
        title=article.find_all('h4')[0]
        link=main['href']
        image_src=str(main.find('img')['srcset']).split(" ")[-4]
        print('title: ' ,title.text)
        print('link: ' ,link)
        print('image_src: ' ,image_src)
        if link is not None and image_src is not None and title is not None:
            new_headline=Headline(title=title.text,image=image_src,url=link)
            new_headline.save()
    return redirect('../')

def news_list(request):
    print("news_list called")
    headlines=Headline.objects.all()[::-1]
    context={
    'object_list':headlines,
    }
    return render(request,"news.html",context)
