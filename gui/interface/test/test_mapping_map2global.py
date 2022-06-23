import folium

import pandas as pd
import matplotlib.pyplot as plt



def show(img, title=None):
    plt.figure(figsize=(6, 6))
    plt.imshow(img)

    if title is not None:
        plt.title(title)

        plt.axis('off')
#Define coordinates of where we want to center our map
boulder_coords = [40.015, -105.2705]

#Create the map
my_map = folium.Map(location = boulder_coords, zoom_start = 13)

#Display the map
my_map

