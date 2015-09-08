
#############################################
#HERE WE IMPORT THE NECESSARY LIBRARIES
#############################################
import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')#COS GGPLOT RULEZ!
import numpy as np
 



##########################################################################################
#HERE WE SET DIR., MAKE SQL CONNECTION, PULL DATAFRAME
##########################################################################################
#YOU MAY NEED TO SET THE PATH CORRECTLY:
#BASE_DIR = os.path.dirname(os.path.abspath('/Users/hugobowne-anderson/repos/odsc-erotic-review'))
#db_path = os.path.join(BASE_DIR, "odsc-erotic-review/user_frequency.db")
db_path = 'user_count.db' #this is the database
conn = sqlite3.connect(db_path) #establish connection to db


df = pd.read_sql_query("select * from username_counts", conn) #make dataframe of usernames + # of posts

df = df.rename(columns={'username': 'name', 'count(username)': 'number'})
df = df.sort('number' , ascending = 0); #sort the dataframe
#df.head()



##########################################################################################
#WE GENERATE AND SAVE THE 1ST PLOT: A HISTOGRAM OF # OF POSTS BY USERNAME
##########################################################################################


N = 100
#
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence
plt.figure(figsize=(16,8))
p1 = plt.bar(ind, df.number[0:N],   width, color='r')


plt.ylabel('Number of posts')
plt.title('Total number of posts by top ' + str(N) + ' users')
plt.xticks(ind+width/2., list(df.name[0:N]) , rotation='vertical' )
#plt.xticks(ind+width/2., range(1,N+1)  )
#plt.yticks(np.arange(0,81,10))
#plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on') # labels along the bottom edge are off
    
plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    right='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off

plt.tight_layout()
plt.savefig('Fig_1_Top_100_users_.pdf')
#plt.show()



##########################################################################################
#WE GENERATE AND SAVE THE 2ND PLOT: A HISTOGRAM OF PROPORTION OF POSTS MADE BY
#MOST FREQUENT USERS
##########################################################################################

sorted_data = np.array(df.number)
p1 = np.cumsum(sorted_data)/float(sum(sorted_data))
#plt.step(sorted_data[::-1], np.arange(sorted_data.size))
p2 = (np.arange(sorted_data.size)+1)/float(sorted_data.size)*100
fig = plt.figure(figsize=(16,8))

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on') # labels along the bottom edge are off
    
plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    right='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off

ax1 = fig.add_subplot(1,1,1)
#ax2 = ax1.twinx()
plt.grid(True)
plt.title('Proportion of posts made by the most frequent users of theeroticreview.com')
ax1.set_ylabel('Proportion of Posts ( 57,053 total posts)')
ax1.set_xlabel('Users Grouped by Freqency (1,951 total users)')
ind = 5
xax = np.arange(0,ind)
width = 0.7

#plt.yticks( list([1,2,3,4,5])  )
plt.xticks( xax + width/2., list(['0% - 0.1%',' 0.1% - 1%','1% - 10%','10% - 25%','25% - 50%'])  )


p3 = [max(p1[p2<0.1]) , max(p1[p2<1]) -max(p1[p2<0.1]) , max(p1[p2<10])-max(p1[p2<1])  , max(p1[p2<25]) -max(p1[p2<10]), max(p1[p2<50])-max(p1[p2<25])]
ax1.bar(xax, p3,   width, color='r')


#plt.xticks( xax , list(['one','two','three','four','five %']) , rotation='vertical' )

#ax2 = ax1.twinx()

#ax2.bar(xax, sum(sorted_data)/100*np.asarray(p3),   width, color='r')
#ax2.set_ylabel('Total # of Posts/Comments')
#ax.axis('on')
#ax.spines['right'].set_visible(True)

#plt.axis([min(p2), max(p2), min(p1), max(p1)]) 
fig.savefig('Fig_2_Post_proportion_by_Frequent_Users.pdf')
plt.tight_layout()
#plt.show()