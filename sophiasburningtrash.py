# -*- coding: utf-8 -*-
"""SophiasBurningTrash.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mhak9pxcscVUU0m-eGYOZi1NReYMiznv
"""

from bokeh.io import output_file, show, output_notebook, show, curdoc
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bokeh.palettes import Reds7
from bokeh.themes import built_in_themes


output_file("gmap.html")

map_options = GMapOptions(lat=30, lng=-85, map_type="roadmap", zoom=6)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:

 
p = gmap("AIzaSyBpzHrL-D9VewwuEby1ybkWIiBEYpaD_Pw", map_options, title="Alabama")

fileData = pd.read_csv('https://raw.githubusercontent.com/williamshammond/dont-burn-your-tv/main/AL_data.csv', warn_bad_lines=True, error_bad_lines = False)
source = ColumnDataSource(data=fileData)
cat_list = source.data["Category"].tolist()


colormap = {'Landfill': 'red', 'C&D Landfill': 'orange', 'Transfer Station': 'yellow', 'Municipal Landfill': 'red', 'Compost Facility': 'green'
,'Waste Tire Facility': 'black','Recycling Center': 'blue'}

# Create a list of colors for each value that we will be looking at.

tooltips=[
        ('Name', '@Name'),
        ("Ditch your TV here?", '@{Residential Electronic Waste}')
]

p.add_tools(HoverTool(tooltips=tooltips))

#Render glyph/ For cmap use fill_color instead of color
p.circle(x="Long", y="Lat", fill_color=factor_cmap("Category", palette=Reds8, factors=cat_list),
       fill_alpha=1.0, source=source)


output_notebook()
show(p)

