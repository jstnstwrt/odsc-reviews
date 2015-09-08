import requests
from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, UserPost


# Creating the database connection.
engine = create_engine('sqlite:///user_frequency.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Interating over the pages of the forum.
for i in range(1,101):
    # Setting the base url of the general discussion forum.
    url = "http://www.theeroticreview.com/"\
          "discussion_boards/messageList.asp?boardID=12&page=" + str(i)
    r = requests.get(url) # Grabbing the source code of the webpage.
    soup = BeautifulSoup(r.content, "lxml") # Parsing the html.
    # Identifying the key element containing all the posts. 
    discussion_board_data = soup.find(
        "div", 
        { "class" : "content-layout thread-tree-paginated" })
    # Creating a list of all the list elements. 
    # Each list element is contains one post.
    posts =  discussion_board_data.find_all('li')
   
    for post in posts:
        # All usernames are contained in strong html tags. 
    	post_data = post.find_all('strong')
    	try:
    		username = str(post_data[0])[len('<strong>'):].strip('</strong>')
    		post = UserPost(username = username)
            # Store username as an entry in the database. 
    		session.add(post)
    		session.commit()
    		print 'added post to db!'
    	except: 
    		print 'some error'