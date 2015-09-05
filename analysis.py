import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
# matplotlib.style.use('ggplot')


BASE_DIR = os.path.dirname(os.path.abspath('/Users/hugobowne-anderson/repos/odsc-erotic-review'))
db_path = os.path.join(BASE_DIR, "odsc-erotic-review/user_frequency.db")
#db_path = 'user_count.db'
conn = sqlite3.connect(db_path)


df = pd.read_sql_query("select * from username_counts", conn)

df = df.rename(columns={'username': 'name', 'count(username)': 'number'})
df = df.sort('number' , ascending = 0);
df.head()

#
#N = 100
##
#ind = np.arange(N)    # the x locations for the groups
#width = 0.7       # the width of the bars: can also be len(x) sequence
#plt.figure(figsize=(16,8))
#p1 = plt.bar(ind, df.number[0:N],   width, color='r')
#
#
#plt.ylabel('Number of posts/comments')
#plt.title('People who say things that interest us (top ' + str(N)+')')
#plt.xticks(ind+width/2., list(df.name[0:N]) , rotation='vertical' )
##plt.xticks(ind+width/2., range(1,N+1)  )
##plt.yticks(np.arange(0,81,10))
##plt.legend( (p1[0], p2[0]), ('Men', 'Women') )
#
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='on',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='on') # labels along the bottom edge are off
#    
#plt.tick_params(
#    axis='y',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='on',      # ticks along the bottom edge are off
#    right='off',         # ticks along the top edge are off
#    labelbottom='off') # labels along the bottom edge are off
#
#plt.tight_layout()
#plt.savefig('user_hist_top_100.pdf')
#plt.show()


##

#sorted_data = np.array(df.number)
#p1 = np.cumsum(sorted_data)/float(sum(sorted_data))*100
##plt.step(sorted_data[::-1], np.arange(sorted_data.size))
#p2 = (np.arange(sorted_data.size)+1)/float(sorted_data.size)*100
#fig = plt.figure(figsize=(16,8))
#
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='on',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='on') # labels along the bottom edge are off
#    
##plt.tick_params(
##    axis='y',          # changes apply to the x-axis
##    which='both',      # both major and minor ticks are affected
##    bottom='on',      # ticks along the bottom edge are off
##    right='off',         # ticks along the top edge are off
##    labelbottom='off') # labels along the bottom edge are off
#
#ax = fig.add_subplot(1,1,1)
##ax.set_xscale('log')
##ax.set_xticklabels([0.1,0.1,1,10,100])
##ax.set_xscale('log')
##plt.xlim(0.1,100)
##plt.plot( p2 ,p1,linewidth=3)
##plt.absolute_importxlim( xmin = 1 )
#plt.title('Percentage of Posts made by Top Users')
#plt.ylabel('Percentage of Posts/Comments')
#plt.xlabel('Percentage of Top Users')
#plt.tight_layout()
##ax.axis('on')
##ax.spines['right'].set_visible(True)
#
##plt.axis([min(p2), max(p2), min(p1), max(p1)]) 
##fig.savefig('top_users.pdf')
#plt.show()
#
sorted_data = np.array(df.number)
p1 = np.cumsum(sorted_data)/float(sum(sorted_data))*100
#plt.step(sorted_data[::-1], np.arange(sorted_data.size))
p2 = (np.arange(sorted_data.size)+1)/float(sorted_data.size)*100
fig = plt.figure(figsize=(16,8))

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on') # labels along the bottom edge are off

ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()
plt.grid(False)
plt.title('Percentage of Posts made by Top Users')
ax1.set_ylabel('Percentage of Posts/Comments')
ax1.set_xlabel('Percentage of Users')
ind = 5
xax = np.arange(0,ind)
width = 0.7

plt.xticks( xax + width/2., list(['top 0.1%','top 1%','top 10%','top 25%','top 50%'])  )


p3 = [max(p1[p2<0.1]) , max(p1[p2<1]) , max(p1[p2<10]) , max(p1[p2<25]) , max(p1[p2<50])]
ax1.bar(xax, p3,   width, color='r')


#plt.xticks( xax , list(['one','two','three','four','five %']) , rotation='vertical' )

#ax2 = ax1.twinx()

ax2.bar(xax, sum(sorted_data)/100*np.asarray(p3),   width, color='r')
ax2.set_ylabel('Total # of Posts/Comments', color='blue')
#ax.axis('on')
#ax.spines['right'].set_visible(True)

#plt.axis([min(p2), max(p2), min(p1), max(p1)]) 
fig.savefig('top_users.pdf')
plt.tight_layout()
plt.show()

#%%

#sorted_data = np.array(df.number)
#p1 = np.cumsum(sorted_data)/float(sum(sorted_data))*100
##plt.step(sorted_data[::-1], np.arange(sorted_data.size))
#p2 = (np.arange(sorted_data.size)+1)/float(sorted_data.size)*100
#fig = plt.figure(figsize=(16,8))
#
#plt.tick_params(
#    axis='x',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='on',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='on') # labels along the bottom edge are off
#
#ax1 = fig.add_subplot(1,1,1)
#ax2 = ax1.twinx()
#plt.grid(False)
#plt.title('Percentage of Posts made by Top Users')
#ax1.set_ylabel('Percentage of Posts/Comments')
#ax1.set_xlabel('Percentage of Users')
#ind = 5
#xax = np.arange(0,ind)
#width = 0.7
#
#plt.xticks( xax + width/2., list(['top 0.1%','top 0.1% - 1%','top 1% - 10%','top 10% - 25%','top 25% - 50%'])  )
#
#
#p3 = [max(p1[p2<0.1]) , max(p1[p2<1]) -max(p1[p2<0.1]) , max(p1[p2<10])-max(p1[p2<1])  , max(p1[p2<25]) -max(p1[p2<10]), max(p1[p2<50])-max(p1[p2<25])]
#ax1.bar(xax, p3,   width, color='r')
#
#
##plt.xticks( xax , list(['one','two','three','four','five %']) , rotation='vertical' )
#
##ax2 = ax1.twinx()
#
#ax2.bar(xax, sum(sorted_data)/100*np.asarray(p3),   width, color='r')
#ax2.set_ylabel('Total # of Posts/Comments', color='blue')
##ax.axis('on')
##ax.spines['right'].set_visible(True)
#
##plt.axis([min(p2), max(p2), min(p1), max(p1)]) 
#fig.savefig('top_users2.pdf')
#plt.tight_layout()
#plt.show()