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

for i in range(0,100):
	post = posts[i]
	post_data = post.find_all('strong')
	username = str(post_data[0])[len('<strong>'):].strip('</strong>')
	timestamp = str(post_data[1])[len('<strong>'):].strip('</strong>')

	post = UserPost(username = username, timestamp = timestamp)
	session.add(post)
	session.commit()
	print 'added post!'


# ## create ##
# myFirstRestaurant = Restaurant( name = "Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()

# cheesepizza = MenuItem( name = "Cheese Pizza", description = "Made with all natural ingredients"
# 				, course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()


# ## read ##
# firstResult = session.query(Restaurant).first()
# print firstResult.name

# items =  session.query(Restaurant).all()
# for item in items:
# 	print item.name


# ## update ##
# urbanVeggieBurger = session.query(MenuItem).filter_by(id = 11).one()
# urbanVeggieBurger.price = '$2.99'
# session.add(urbanVeggieBurger)
# session.commit()


# ## delete ##
# spinach = session.query(MenuItem).filter_by(name = "Spinach Ice Cream").one()
# session.delete(spinach)
# session.commit()

