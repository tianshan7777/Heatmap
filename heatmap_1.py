#To create an interactive heatmap overlaying Google maps.
#The end result will be an HTML file that you can open and zoom in/out or pan through to visualize customer addresses
import pandas as pd 
import gmplot
#For improved table display in the notebook
'''
raw_data = pd.read_csv("alberlet_rent.csv")
#Success! Display the first 5 row of the dataset
print(raw_data.head(n = 5))
print(raw_data.info())

#Row wise to column wise
new_data = pd.DataFrame(raw_data.T)
print(new_data.head(n=3))

new_data.to_csv("albert.csv")'''

new_data = pd.read_csv("albert.csv")
#Store our latitude and longtitude

#Limit the dataset to the first 15,000 records
data = new_data.head(n = 200)

latitudes = new_data["Latitude"]
longitudes = new_data["Longitude"]

#Create the location we would like to initialize the focus on
#Parameters: Latitude, Longitude, Zoom
gmap = gmplot.GoogleMapPlotter(47.497913, 19.040236, 15)

#Overlay out datapoints onto the map
gmap.heatmap(latitudes, longitudes)

#Generate the heatmap into an HTML file
gmap.draw("numberOfRent_heatmap.html")