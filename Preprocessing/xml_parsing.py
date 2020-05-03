import os
import xml.dom.minidom
import pandas as pd
from datapreprocessing import calculateDistance
 
def getListOfFiles(directory):
    file_list = os.listdir(directory)
    return file_list

def file_content(file_name):
    """Returns the content of the file"""
    ''' f = open(file_name,"r")
    content = f.read()
    return content'''
    doc = xml.dom.minidom.parse(file_name)
    nodes = doc.getElementsByTagName("node")
    list_lat_long=list()
    for node in nodes:
        list_lat_long.append([node.getAttribute("lat"),node.getAttribute("lon")])
    return list_lat_long

def generate_distance():
    inter = pd.read_csv('intersections.csv')
    lag_lat = '40.7733'
    lag_lon = '-73.8743'
    distance = []
    for index, row in inter.iterrows():
        d =calculateDistance(str(row['Lat']),str(row['Lon']),lag_lat,lag_lon) 
        distance.append(d[0])
    inter['distance'] = distance
    inter.head()
    inter.to_csv('final.csv')

def main():
    '''final_list = []
    path = 'map_data/'''
    file = file_content('export.osm')
    ''' for i in files:
        list = file_content(path+i)
        final_list = final_list + list'''
    df = pd.DataFrame(file,columns = ["Lat","Lon"])
    df.to_csv('intersections.csv')
    generate_distance()
    
if __name__ == "__main__":
    main()