import sys

from geopandas import sindex

print(sys.path)
import numpy as np
import pandas as pd
import shapely
import geopandas as gpd
from shapely import wkt
from shapely import geometry as geo
import matplotlib.pyplot as plt
import rtree


gsr_points = gpd.GeoSeries()
gsr_ploygons = gsr_points.buffer(0.5)
ax = gsr_ploygons.plot(figsize = (8,10),cmap = "tab10")
gsr_points.plot(color = "red",ax = ax)
plt.show()

