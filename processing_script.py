import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import os
import datetime

def Filter_to_Timeline():

    ## Define paths 
    cur_path = os.path.dirname(os.path.realpath(__file__))
    csv_read_name = "Swainson's Hawks.csv"
    csv_read_path = os.path.join(cur_path, csv_read_name)

    csv_output_name = 'SwainsonsHawks_filtered.csv'
    csv_output = os.path.join(cur_path, csv_output_name)

    ## Filter data to 1997-1998
    df = pd.read_csv(csv_read_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[df['timestamp'].between('1996-07-01', '1997-07-07')]
    df.to_csv(csv_output)
    return 1



def CreateLineString():

    ## Define Paths necessary to navigate reading and outputing processed data
    geojson_read_name = "Swainson's Hawks_raw.geojson"
    geojson_output_name_paths = "SwainsonHawks_linestrings.geojson"
    cur_path = os.path.dirname(os.path.realpath(__file__))
    read_path = os.path.join(cur_path, geojson_read_name)
    output_paths_only = os.path.join(cur_path, geojson_output_name_paths) #output just linestrings


    # Read in the Raw Swainson Hawk data in geojson format
    df = gpd.read_file(read_path)
    df = df[df['timestamp'] >= '1996-07-01']
    df = df[df['timestamp'] <= '1997-07-07']

    # Iterate down to each bird (SW#) --> then to each Timestamp --
    # --> create LineString of coordinates from initial timestamp to current timestamp (give view of growing line over time to show path) 
    main_df = pd.DataFrame()
    for x in df.groupby(['individual-local-identifier']): # Access each bird (SW#)
        temp = []

        for i in range(1,len(x[1]['timestamp'].values)): # Iterate over each individual timestamp
            time_temp = []
            k=0
            if i+1 > 4:
                k=i-4

            for j in range(k,i+1): # Iterate from initial timestamp to the timestamp identified in the previous for loop.
                time_temp.append((x[1].iloc[j]['geometry'].x, x[1].iloc[j]['geometry'].y))

            temp.append([x[0], x[1].iloc[i]['timestamp'],str(x[1].iloc[i]['geometry'].y), str(x[1].iloc[i]['geometry'].x),LineString(time_temp)]) #Create linestring and append to tracker-list
            # format example is:[SW8, 1995-08-18T16:10:00, LINESTRING OBJECT]


        # Take the temporary array, make that into a dataframe, then concat each dataframe to result in one final pandas DF
        for i in range(len(temp)):
            dfa = gpd.GeoDataFrame([temp[i][0], temp[i][1], temp[i][2], temp[i][3], temp[i][4]])
            temp_df = dfa.T
            main_df = pd.concat([main_df, temp_df])


    # label the colums of the DF and convert it to a GeoPandas Dataframe (GeoPandas does not have a pd.concat function, so the main workaround is to resort to using
    # a pandas dataframe and running .concat on it.)
    main_df.columns = ['individual-local-identifier', 'timestamp','lat','long', 'flight_path']
    gdf = gpd.GeoDataFrame(main_df, geometry= 'flight_path')

    gdf.to_file(output_paths_only, driver = 'GeoJSON') # This creates a geojson of JUST THE FLIGHT PATHS


if __name__ =='__main__':
    Filter_to_Timeline()
    CreateLineString()
















