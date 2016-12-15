###############################################################################
# Assignment 5 by Carmen Christen (14-730-204) and Pascal Siemon
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


###########################################

# get the desired data to work with

year_range=range(2000,2011)
dat1=dat[dat.year.isin(year_range)]
         
''' Add the next line if you only want to consider movies from Switzerland
    (doesn't make so much sense because then you end up with just one value)'''
#dat1=dat1[dat1.country.isin(['Switzerland'])]

dat1=pd.DataFrame(dat1,columns=['year','imdb_score','genres'])

###########################################



###########################################

# get a list of all genres

genres=dat1.genres.drop_duplicates()
genres2=[]

for genre in genres:
    genreList=genre.split("|")
    for i in range(0,len(genreList)):
        genres2.append(genreList[i])

genres=pd.DataFrame(genres2).drop_duplicates()

###########################################



###########################################

# plot the desired graph with imdb averages

for j in range(0,len(genres)):
    gen=[]
    for k in range(0,len(dat1)):
        genk=dat1.iloc[k,2].split("|")
        for i in range(0,len(genk)):
            if genk[i]==genres.iloc[j,0]:
                gen.append(dat1.iloc[k])
    genDF=pd.DataFrame(gen)
    groupedY=genDF.groupby(by=['year'])
    genAgg=groupedY['imdb_score'].agg(np.average)
    plt.subplot(1,2,1)
    ax=genAgg.plot(label=genres.iloc[j,0],legend=True,title='Average IMDb-Score',figsize=[30,15])

##########################################



###########################################

# plot the desired graph with imdb mean values

for j in range(0,len(genres)):
    gen=[]
    for k in range(0,len(dat1)):
        genk=dat1.iloc[k,2].split("|")
        for i in range(0,len(genk)):
            if genk[i]==genres.iloc[j,0]:
                gen.append(dat1.iloc[k])
    genDF=pd.DataFrame(gen)
    groupedY=genDF.groupby(by=['year'])
    genAgg=groupedY['imdb_score'].agg(np.mean)
    plt.subplot(1,2,2)
    ax=genAgg.plot(label=genres.iloc[j,0],legend=True,title='Mean IMDb-Score',figsize=[30,15])

##########################################



#########################################

# save the figure
fig = ax.get_figure()
fig.savefig('task1.png')

#########################################




###############################################################################
# useful commands and intermediate steps from the tasks
###############################################################################

# task 1

'''    print(dat1.country.drop_duplicates())       -> Used to check whether there 
                                                      are other terms for 'Switzerland'
                                                    
       for name,group in dat1.groupby(by=['genres']):
           groupedDatY=group.groupby(by=['year'])
           groupedDatYAv=groupedDatY['imdb_score'].agg(np.average)
           groupedDatYAv.plot(label=name)                               -> first version
                                                   
'''


# useful commands

'''     dat.duplicated()     -> returns an array from 0 to num. of rows of dat with
                                entry False if this row appears for the first time
                                and True if not
        
        dat.head()           -> returns the first 5 rows for every column  
        
        import os
        os.chdir(path)       -> set working directory
        
        os.chdir('C:/Users/Carmen/Documents/Uni Zürich Bachelor/Uni Zürich 5. Semester/Informatik/Data Visualization/Exercises/Assignment_5/dv_ex_5_14730204/DataVis')
        
        len(groupedDat)      -> Länge (573)
        
        groupedDatY['imdb_score'].agg(np.average).astype('pd.core.frame.DataFrame')
'''
