from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from scipy import interpolate
import pylab
from sys import getsizeof
from write2file import write2nc
from decimal import Decimal
import sys

filein  = sys.argv[1]
fileout = sys.argv[2]
#filein  = 'TPR7_uw1_03385.19980630.131844_SAS.nc'
lon_start = 60.0
lon_end = 100.0
lat_start = 5.0
lat_end = 40.0
i=0
fhin = Dataset(filein, mode='r')
longitude = fhin.variables['longitude'][:]
latitude  = fhin.variables['latitude'][:]
surf_rain = fhin.variables['surf_rain'][:]

lon = []
for lon_i in range(int((lon_end - lon_start)/0.05) + 1):
	lon.append(1)
	lon[lon_i] = lon_start + lon_i * 0.05	
	lon[lon_i] = round(lon[lon_i],2)

lat = []
for lat_i in range(int((lat_end - lat_start)/0.05) + 1):
	lat.append(1)
	lat[lat_i] = lat_start + lat_i * 0.05 	
	lat[lat_i] = round(lat[lat_i],2)
rf = np.empty((int((lon_end - lon_start)/0.05) + 1, int((lat_end - lat_start)/0.05) + 1))

for lon_i in range(int((lon_end - lon_start)/0.05) + 1):
	for lat_i in range(int((lat_end - lat_start)/0.05) + 1):
		#print("lon_i = ",lon[lon_i])
		rf[lon_i][lat_i] = np.nan
		found = False
		for i in range(longitude.shape[0]):
			for j in range(latitude.shape[0]):
				if((abs(lon[lon_i] - longitude[i]) < 0.2 ) and (abs(lat[lat_i] - latitude[j]) < 0.2 )):
					rf[lon_i][lat_i] = surf_rain[0][i][j]
					print("surf_rain = ",surf_rain[0][i][j], "rf = ",rf[lon_i][lat_i])
					found = True
				if(found):
					break
			if(found):
				break
fhin.close()
nx = int((lon_end - lon_start)/0.05) + 1
ny = int((lat_end - lat_start)/0.05) + 1
#write2nc(lon, lat, rf, 'surf_rain', 'lon', 'lat', 'out.nc')
write2nc(lon, lat, rf, 'surf_rain', 'lon', 'lat', fileout)


