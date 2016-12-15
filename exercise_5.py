###############################################################################
# Assignment 5 by Carmen Christen (14-730-204) and Pascal Siemon (14-721-864)
###############################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
# task 1
###############################################################################

# get the desired data to work with
year_range=range(2000,2011)
dat1=dat[dat.year.isin(year_range)]
dat1=pd.DataFrame(dat1,columns=['year','imdb_score','genres'])

groupedDat=dat1.groupby(by=['genres','year'])
groupedDatAv=groupedDat['imdb_score'].agg(np.average)

ax = plt.subplot(1,2,1)


for label in groupedDat:
    groupedDatAv.plot(x='year',y='imdb_score',ax=ax, label=label)
plt.legend()


###############################################################################
# useful commands and intermediate steps from the tasks
###############################################################################

# task 1

'''    print(dat1.country.drop_duplicates())       -> Used to check whether there 
                                                      are other terms for 'Switzerland'
                                                   
'''


# useful commands

'''     dat.duplicated()     -> returns an array from 0 to num. of rows of dat with
                                entry False if this row appears for the first time
                                and True if not
        dat.head()           -> returns the first 5 rows for every column  
'''
