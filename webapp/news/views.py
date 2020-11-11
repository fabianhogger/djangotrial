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
    for article in News:
        main=article.find_all('a')[0]
        #title=article.find_all('h4')[0]
        #link=main['href']
        images=main.find('img')
        if images is not None:
            if images.has_attr('srcset'):
                print(images)

        """
        if images is not None and main.find('img')['srcset'] is  not None:
            print('entered if')
            image_src=str(main.find('img')['srcset']).split("w,")[0]
        else:
            image_src =None
        print('title: ' ,title.text)
        print('link: ' ,link)
        print('image_src: ' ,image_src)
        titlet=str(title.text)
        if link is not None and image_src is not None and title is not None:
            new_headline=Headline(title=titlet,image=image_src,url=link)
            new_headline.save()
        """
    return redirect('../')

def news_list(request):
    print("news_list called")
    headlines=Headline.objects.all()[::-1]
    context={
    'object_list':headlines,
    }
    return render(request,"news.html",context)
