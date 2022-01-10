import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now=datetime.datetime.now()

#email content placeholder
content=''
#extracting data

def extract_news(url):
    print("extracting data")
    cnt=''
    cnt += ('<b>HN Top Stories</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    c=soup.find_all('a',attrs={'class':'storylink'})
    for i,tag in enumerate(c):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + "<br>") if tag.text != 'more' else '')
    return(cnt)

cnt=extract_news('https://news.ycombinator.com/')
content +=cnt
content += ('<br>---------<br>')
content +=('<br><br>End of Message')
print(content)

#email

Server= 'smtp.gmail.com'
Port= 587
From = '#'
To = '#' #can also take a list
Pass = '#'

msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories'+' '+str(now.day)+"-"+str(now.month)+'-'+str(now.year)
msg['From'] = From
msg['To'] = To

msg.attach(MIMEText(content,'html'))

server = smtplib.SMTP(Server, Port)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(From, Pass)
server.sendmail(From, To, msg.as_string())

print('Email Sent...')

server.quit()