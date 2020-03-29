from mechanize import Browser
from bs4 import BeautifulSoup 
from pandas import *

br=Browser()

date=[]
open=[]
close=[]
high=[]
low=[]
vol=[]
adj_close=[]
flag=False
toggle="https://in.finance.yahoo.com/q/hp?s=TATAMOTORS.BO"

while flag!=True:
    flag=True
    response=br.open(toggle)
    soup=BeautifulSoup(response.read(),"html.parser")
    table=soup.find('table' , { "class" : 'yfnc_datamodoutline1' })
    link=soup.findAll('a')
    toggle=""
    for i in link:
        if i.text=="Next":
            toggle=i.get("href")
            flag=False
    toggle="https://in.finance.yahoo.com"+str(toggle)
    print toggle
    for row in table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)==7:
            date.append(cells[0].text)
            open.append(cells[1].text)
            high.append(cells[2].text)
            low.append(cells[3].text)
            close.append(cells[4].text)
            vol.append(cells[5].text)
            adj_close.append(cells[6].text)
        
    df=DataFrame(date,columns=['Date'])
    df['Open price']=open
    df['High']=high
    df['Low']=low
    df['Close']=close
    df['Volume']=vol
    df['Adj close']=adj_close

