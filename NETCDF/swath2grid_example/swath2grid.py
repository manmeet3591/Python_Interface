from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from scipy import interpolate
import pylab
from sys import getsizeof
from write2file import write2nc_2d,write2nc_4d
from decimal import Decimal
import sys
from rounding import myround

filein  = sys.argv[1]
fileout = sys.argv[2]
#filein  = 'TPR7_uw1_03385.19980630.131844_SAS.nc'
#filein  = '2A25.20050621.43299.7.nc'
lon_start = -180
lon_end = 180
lat_start = -90.0
lat_end = 90.0
i=0
fhin = Dataset(filein, mode='r')
longitude = fhin.variables['Longitude'][:]
latitude  = fhin.variables['Latitude'][:]
rain = fhin.variables['rain'][:]
rainType = fhin.variables['rainType'][:]
surf_rain = fhin.variables['e_SurfRain'][:]
res = 0.5
#print(rainType)
rf = np.empty((int((lon_end - lon_start)/res) + 1, int((lat_end - lat_start)/res) + 1))

lon = []
for lon_i in range(int((lon_end - lon_start)/res) + 1):
	lon.append(1)
	lon[lon_i] = lon_start + lon_i * res
	lon[lon_i] = round(lon[lon_i],2)
#lon = np.asarray(lon)

lat = []
for lat_i in range(int((lat_end - lat_start)/res) + 1):
	lat.append(1)
	lat[lat_i] = lat_start + lat_i * res
	lat[lat_i] = round(lat[lat_i],2)
#lat = np.asarray(lat)

#print(lon.shape)

# nscan X nray
# array.index(value)
for j in range(longitude.shape[1]):
	for i in range(longitude.shape[0]):
		#print(myround(longitude[i,j], 2, 0.05))
		x_index = lon.index(myround(longitude[i,j], 2, res))
		y_index = lat.index(myround(latitude[i,j], 2, res))
		rf[x_index, y_index] = rf[x_index, y_index] + surf_rain[i,j]

write2nc_2d(lon, lat, rf, 'surf_rain', 'lon', 'lat', fileout)
#write2nc_4d(fileout, nlats, nlons, nlevs, nrecs, press_out, temp_out)

		#print(rf[x_index, y_index])
#print(latitude)
#test = []
#test[1:10] = 0
#print(test)

#for lon_i in range(int((lon_end - lon_start)/0.05) + 1):
#	for lat_i in range(int((lat_end - lat_start)/0.05) + 1):
#		#print("lon_i = ",lon[lon_i])
#		rf[lon_i][lat_i] = np.nan
#		found = False
#		for i in range(longitude.shape[0]):
#			for j in range(latitude.shape[0]):
#				if((abs(lon[lon_i] - longitude[i]) < 0.2 ) and (abs(lat[lat_i] - latitude[j]) < 0.2 )):
#					rf[lon_i][lat_i] = surf_rain[0][i][j]
#					print("surf_rain = ",surf_rain[0][i][j], "rf = ",rf[lon_i][lat_i])
#					found = True
#				if(found):
#					break
#			if(found):
#				break
#fhin.close()
#nx = int((lon_end - lon_start)/0.05) + 1
#ny = int((lat_end - lat_start)/0.05) + 1
##write2nc(lon, lat, rf, 'surf_rain', 'lon', 'lat', 'out.nc')
#write2nc(lon, lat, rf, 'surf_rain', 'lon', 'lat', fileout)


