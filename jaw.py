import requests
from bs4 import BeautifulSoup
import pandas as pd
def news():
    # the target we want to open
    url = 'https://summerofcode.withgoogle.com/archive/2019/projects/'

    # open with GET method
    resp = requests.get(url)
    print("new")
    # http_respone 200 means OK status
    if resp.status_code == 200:
        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')
        l=soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-0"})
        l1=soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-1"})
        l2=soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-2"})
        l3=soup.findAll("div",{"class":"md-padding archive-project-card__header archive-project-card__header--mod-3"})
        name=[]
        org=[]
        pro=[]
        for i in l:
            name.append(i.a.text)
            c=0
            for t in i.findAll("div"):
                if c%2==0:
                    pro.append(t.text)
                else:
                    org.append(t.text)
                c=c+1            
        for i in l1:
            name.append(i.a.text)
            c=0
            for t in i.findAll("div"):
                if c%2==0:
                    pro.append(t.text)
                else:
                    org.append(t.text)
                c=c+1            
        for i in l2:
            name.append(i.a.text)
            c=0
            for t in i.findAll("div"):
                if c%2==0:
                    pro.append(t.text)
                else:
                    org.append(t.text)
                c=c+1            
        for i in l3:
            name.append(i.a.text)
            c=0
            for t in i.findAll("div"):
                if c%2==0:
                    pro.append(t.text)
                else:
                    org.append(t.text)
                c=c+1            
        df=pd.DataFrame({'name':name,'program':pro,'organization':org})
        df.to_csv('file1.csv')
news()