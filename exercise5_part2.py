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
#     
###############################################################################
 
year_range = range(1915,2014)
totalNumber = 99*[0] 
numberOfAnimation = 99*[0]
numberOfAction = 99*[0]
numberOfRomance = 99*[0]
numberOfDocumentary = 99*[0]
numberOfComedy = 99*[0]
numberOfDrama = 99*[0]
totalNumberGenres = 99*[0]
restrictedDat = dat[dat.year.isin(year_range)]
        
for year in year_range:  
    dataForYear = restrictedDat[restrictedDat.year.isin([year])]
    for genre in dataForYear.genres:
        if 'Animation' in genre:
            numberOfAnimation[year-1915] = numberOfAnimation[year-1915] + 1
        if 'Action' in genre:
            numberOfAction[year-1915] = numberOfAction[year-1915] + 1
        if 'Romance' in genre:
            numberOfRomance[year-1915] = numberOfRomance[year-1915] + 1
        if 'Documentary' in genre:
            numberOfDocumentary[year-1915] = numberOfDocumentary[year-1915] + 1
        if 'Comedy' in genre:
            numberOfComedy[year-1915] = numberOfComedy[year-1915] + 1
        if 'Drama' in genre:
            numberOfDrama[year-1915] = numberOfDrama[year-1915] + 1        
        totalNumber[year-1915] = totalNumber[year-1915] + 1
        totalNumberGenres[year-1915] = numberOfAnimation[year-1915] + numberOfAction[year-1915] + numberOfRomance[year-1915] + numberOfDocumentary[year-1915] + numberOfComedy[year-1915] + numberOfDrama[year-1915]
        
numberOfAnimationRef = 99*[0]
numberOfActionRef = 99*[0]
numberOfRomanceRef = 99*[0]
numberOfDocumentaryRef = 99*[0]
numberOfComedyRef = 99*[0]
numberOfDramaRef = 99*[0]

for i in range(0,99):
    if totalNumberGenres[i] != 0:
        numberOfAnimationRef[i] = float(numberOfAnimation[i])/totalNumberGenres[i] * 100    
        numberOfActionRef[i] = float(numberOfAction[i])/totalNumberGenres[i] * 100
        numberOfRomanceRef[i] = float(numberOfRomance[i])/totalNumberGenres[i] * 100
        numberOfDocumentaryRef[i] = float(numberOfDocumentary[i])/totalNumberGenres[i] * 100
        numberOfComedyRef[i] = float(numberOfComedy[i])/totalNumberGenres[i] * 100        
        numberOfDramaRef[i] = float(numberOfDrama[i])/totalNumberGenres[i] * 100
    
plt.subplot(2,1,1) 
plt.plot(year_range, totalNumber, color = 'black', linewidth = 10)
plt.stackplot(year_range, numberOfAnimation, numberOfAction, numberOfRomance, numberOfDocumentary, numberOfComedy, numberOfDrama)
plt.xlim([1915,2013])
plt.legend(['Total Movies','Animation','Action','Romance','Documentary','Comedy','Drama'], loc = 'upper center', ncol = 7)
plt.xticks(np.arange(1915, 2013+1, 10))

plt.subplot(2,1,2)
plt.stackplot(year_range, numberOfAnimationRef, numberOfActionRef, numberOfRomanceRef, numberOfDocumentaryRef, numberOfComedyRef, numberOfDramaRef)
plt.xlim([1915,2013])
plt.legend(['Animation','Action','Romance','Documentary','Comedy','Drama'], loc = 'upper center', ncol = 6)
plt.xticks(np.arange(1915, 2013+1, 10))