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
#prepare data and split in different categories of number_critic_for_reviews
###############################################################################

year_range = range(2000,2011)
restrictedDat = dat[dat.year.isin(year_range)]
restrictedDatMovie = restrictedDat[~np.isnan(restrictedDat.duration)]
restrictedDatReviews = restrictedDat[~np.isnan(restrictedDat.num_critic_for_reviews)]
restrictedDatPlot1 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(0,10))]
restrictedDatPlot2 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(100,200))]
restrictedDatPlot3 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(200,300))]
restrictedDatPlot4 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(300,400))]
restrictedDatPlot5 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(400,500))]
restrictedDatPlot6 = restrictedDatReviews[restrictedDatReviews.num_critic_for_reviews.isin(range(500,1000))]

###############################################################################
#create plots and add title/labels
###############################################################################

plt.xlim([0,230])
plt.scatter(restrictedDatPlot1.duration, restrictedDatPlot1.imdb_score, color = 'red', s = 150)
plt.scatter(restrictedDatPlot2.duration, restrictedDatPlot2.imdb_score, color = 'orange', s = 150)
plt.scatter(restrictedDatPlot3.duration, restrictedDatPlot3.imdb_score, color = 'yellow', s = 150)
plt.scatter(restrictedDatPlot4.duration, restrictedDatPlot4.imdb_score, color = 'green', s = 150)
plt.scatter(restrictedDatPlot5.duration, restrictedDatPlot5.imdb_score, color = 'blue', s = 150)
plt.scatter(restrictedDatPlot6.duration, restrictedDatPlot6.imdb_score, color = 'black', s = 150)
plt.legend(['reviews<100','100<reviews<200','200<reviews<300','300<reviews<400','400<reviews<500','500<reviews'])
plt.title('Duration vs. IMDb Score with number of reviews')
plt.xlabel('Duration[min]')
plt.ylabel('IMDb Score')