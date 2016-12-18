###############################################################################
# Assignment 5 by Carmen Christen (14-730-204) and Pascal Siemon
###############################################################################

import pandas as pd
import matplotlib.pyplot as plt
import math

###############################################################################
# read data
###############################################################################

dat=pd.read_csv('movie_metadata.csv')

# change the column names if you like
dat.columns = ['color','director_name','num_critic_for_reviews','duration',
               'director_facebook_likes','actor_3_facebook_likes',
               'actor_2_name','actor_1_facebook_likes','gross','genres',
               'actor_1_name','movie_title','num_voted_users',
               'cast_total_facebook_likes','actor_3_name',
               'facenumber_in_poster','plot_keywords','movie_imdb_link',
               'num_user_for_reviews','language','country','content_rating',
               'budget','year','actor_2_facebook_likes','imdb_score',
               'aspect_ratio','movie_facebook_likes']
               
###############################################################################
# task 4
###############################################################################


# get the desired data to work with
dat=pd.DataFrame(dat,columns=['movie_title','imdb_score','genres'])

# get the length of the data
n=len(dat)

# get the genres and the number of genres
genreList=dat.genres.drop_duplicates()
m=len(genreList)

# create an figure for the plot
fig = plt.figure(figsize=[25,25])
fig.suptitle('task 4', fontsize=14, fontweight='bold')
ax = fig.add_subplot(1,1,1)

# do the plot
for i in range(0,n):
    genre=dat.iloc[i,2]
    index=0
    for j in range(0,m):
        if genre==genreList.iloc[j]:
            index=j
    col=(abs(round(math.sin(31*2*math.pi/m*index),5)),abs(round(math.cos(5*2*math.pi/m*index),5)),abs(round(math.cos(13*2*math.pi/m*index),5)))
    size=int(dat.iloc[i,1]*2)
    title=dat.iloc[i,0]
    angle=i/n*360
    if angle<=90:
        ax.text(math.cos(i/n*2*math.pi)*10+12.5,math.sin(i/n*2*math.pi)*10+12.5, title, fontsize=size, color=col, rotation=angle,ha='left',va='bottom')
    if angle>90 and angle<=180:
        ax.text(math.cos(i/n*2*math.pi)*10+12.5,math.sin(i/n*2*math.pi)*10+12.5, title, fontsize=size, color=col, rotation=angle,ha='right',va='bottom')
    if angle>180 and angle<=270:
        ax.text(math.cos(i/n*2*math.pi)*10+12.5,math.sin(i/n*2*math.pi)*10+12.5, title, fontsize=size, color=col, rotation=angle,ha='right',va='top')
    if angle>270:
        ax.text(math.cos(i/n*2*math.pi)*10+12.5,math.sin(i/n*2*math.pi)*10+12.5, title, fontsize=size, color=col, rotation=angle,ha='left',va='top')

# save the plot without axes        
ax.axis([0, 25, 0, 25])
ax.set_axis_off()
plt.show()
fig = ax.get_figure()
fig.savefig('task4.png')


