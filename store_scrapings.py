from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, UserPost

import requests
from bs4 import BeautifulSoup
import re

engine = create_engine('sqlite:///user_frequency.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()


url = "http://www.theeroticreview.com/discussion_boards/messageList.asp?boardID=12&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")


discussion_board_data = soup.find("div", { "class" : "content-layout thread-tree-paginated" })
posts =  discussion_board_data.find_all('li')


user_data = []
nonsense_data = []

for post in posts:
    try:
        post_data = post.find_all('strong')
        username = str(post_data[0])[len('<strong>'):].strip('</strong>')
        timestamp = str(post_data[1])[len('<strong>'):].strip('</strong>')
        post = UserPost(username = username, timestamp = timestamp)
        session.add(post)
        session.commit()
        print 'added post!'
    except IndexError:
        nonsense_data.append(post_data)
        print 'CRAPPY HTML!'


