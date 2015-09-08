## config code

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()



## class code
class UserPost(Base):
	#table code
	__tablename__ = 'user_post'

	id = Column( Integer, primary_key = True)
	username = Column( String(80), nullable = False)
	# timestamp = Column( String(80), nullable = False)
	
## config code

engine = create_engine('sqlite:///user_frequency.db')
Base.metadata.create_all(engine)