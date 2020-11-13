from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from django.http import HttpResponse
import re
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
        title=article.find_all('h4')[0]
        link=main['href']
        images=main.find('img')
        if images is not None:
            if images.has_attr('srcset'):
                #print(images)
                image_src=str(main.find('img')['srcset']).split(".jpg")[0]
                print('title: ' ,title.text)
                print('link: ' ,link)

                titlet=str(title.text)
                image_src=image_src+'.jpg'
                print('image_src: ' ,image_src)
                if link is not None and image_src is not None and title is not None:
                    new_headline=Headline(title=titlet,image=image_src,url=link)
                    new_headline.save()
    return redirect('news')

def scrape_article(request):
    if request.method== 'POST':
        url=request.POST['URL']
        session=requests.Session()
        session.headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        content=session.get(url,verify=True).content
        soup=BSoup(content,"html.parser")
        article=soup.find('meta',{"name":"description"})['content']
        title=soup.title.string
        images=soup.find('img')
        print("IMAGES ",images)
        print('                                 ')
        print('                                 ')
        print('                                 ')

        if images is not None:
            if images.has_attr('data-srcset'):
                txt=str(soup.find('img')['data-srcset'])
                img_list=re.findall("(?<=https).*?(?=jpg)",txt)
                img_list='https'+img_list[1]+'jpg'
                print('image link: ',img_list)
        print('                                 ')
        print('                                 ')
        print('                                 ')

        print('article',article)
        print('title',title)

    return redirect("news")
    #new_article=Article(title=title,image=title,url=url)


def news_list(request):
    print("news_list called")
    headlines=Headline.objects.all()[::-1]
    context={
    'object_list':headlines,
    }
    return render(request,"news.html",context)
