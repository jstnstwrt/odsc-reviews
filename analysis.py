import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
# matplotlib.style.use('ggplot')


#BASE_DIR = os.path.dirname(os.path.abspath('/Users/hugobowne-anderson/repos/odsc-erotic-review'))
#db_path = os.path.join(BASE_DIR, "odsc-erotic-review/user_frequency.db")
db_path = 'user_count.db'
conn = sqlite3.connect(db_path)


df = pd.read_sql_query("select * from username_counts", conn)

df = df.rename(columns={'username': 'name', 'count(username)': 'number'})
df = df.sort('number' , ascending = 0);
df.head()


N = 100

ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence
plt.figure(figsize=(16,8))
p1 = plt.bar(ind, df.number[0:N],   width, color='r')


plt.ylabel('Number of posts/comments')
plt.title('People who say things that interest us (top ' + str(N)+')')
plt.xticks(ind+width/2., list(df.name[0:N]) , rotation='vertical' )
#plt.xticks(ind+width/2., range(1,N+1)  )
#plt.yticks(np.arange(0,81,10))
#plt.legend( (p1[0], p2[0]), ('Men', 'Women') )


plt.tight_layout()
plt.show()
