import telegram
import pyshorteners
import pandas as pd
import notification
from pygooglenews import GoogleNews
from datetime import datetime
import constant
import time


def short_url(url):
    shortner = pyshorteners.Shortener()
    my_short_url = shortner.tinyurl.short(url)
    return my_short_url


gn = GoogleNews(lang='en', country='IN')
news_json = gn.top_news()
news_story = []

for entries in news_json['entries']:  # print(entries['title'], entries['link'])
    news_story.append([entries['title'], entries['link']])

panda_dataframe = pd.DataFrame(news_story[:10], columns=['news', 'link'])

panda_dataframe['short_url'] = panda_dataframe['link'].apply(short_url)
panda_new = panda_dataframe.drop(['link'], axis=1)
panda_new["news_url"] = panda_new["news"] + "\n<b>Link: " + panda_new['short_url'] + "</b>"

news_story_str = '\n\n'.join(str(e) for e in panda_new["news_url"])

date_now = datetime.now().strftime("%I:%M %p")
news_time = "<b>News @ {}</b>".format(date_now)

news_str = news_time + constant.news_message + "\n\n\n" + news_story_str

while(True):
    notification.send_to_telegram(news_str)
    time.sleep(3)


#print(pd.__version__)
