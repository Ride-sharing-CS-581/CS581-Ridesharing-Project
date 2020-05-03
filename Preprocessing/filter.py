import pandas as pd
import numpy as np

def filtering_taxi_trips_data():
    from_count = 0 
    to_count = 0
    for i in range (1,7):
        file_name = 'yellow_tripdata_2016-1' + str(i) 
        df = pd.read_csv(file_name+'.csv')

        #from the airport 

        fromT=df.loc[(df['pickup_longitude'].between(-73.8875,-73.8572) ) & (df['pickup_latitude'].between(40.7713,40.7748)) ]

        #to the airport

        to=df.loc[(df['dropoff_longitude'].between(-73.8875,-73.8572) ) & (df['dropoff_latitude'].between(40.7713,40.7748)) ]
        res = pd.concat([fromT,to])
        res.to_csv(file_name+'filtered.csv')
        
def removing_unwanted_data():
    file_name = ['jan.csv','feb.csv','mar.csv','apr.csv','may.csv','june.csv']
    for i in range (1,7):
        file_name= 'yellow_tripdata_2016-0'+str(i)+'filtered.csv'
        df = pd.read_csv(file_name)
        #from the airport 
        initial = len(df)
        discard=df.loc[(df['pickup_longitude'].between(-73.8875,-73.8572) ) & (df['pickup_latitude'].between(40.7713,40.7748)) &
                    (df['dropoff_longitude'].between(-73.8875,-73.8572) ) & (df['dropoff_latitude'].between(40.7713,40.7748))]
        df=df.drop(discard.index)
        same_time = df.loc[df['tpep_pickup_datetime'] == df['tpep_dropoff_datetime']]
        df=df.drop(same_time.index)
        distance_zero=df.loc[df['trip_distance']==0]
        df=df.drop(distance_zero.index)
        df.to_csv(file_name[i])