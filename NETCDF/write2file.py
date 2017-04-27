from netCDF4 import Dataset
from numpy import arange, dtype 
import numpy as np

def write2nc_2d(lon, lat, out, out_name, dimx_name, dimy_name, file_name ):
	nx = out.shape[0]
	ny = out.shape[1]
	ncfile = Dataset(file_name,'w') 
	ncfile.createDimension(dimx_name, nx)
	ncfile.createDimension(dimy_name, ny)
	data_lon = ncfile.createVariable("lon", "f4", ("lon",))
	data_lat = ncfile.createVariable("lat", "f4", ("lat",))
	data = ncfile.createVariable(out_name, dtype('float').char,(dimx_name, dimy_name))

	data_lon.units = 'degrees'
	data_lon.long_name = 'longitude' 
	data_lat.units = 'degrees'
	data_lat.long_name = 'latitude' 
	data.units = 'mm/hr'
	data.long_name = '2A25 rainfall rate near the surface'
	#data.missing_value = '-999.f'

	data_lon[:] = lon
	data_lat[:] = lat
	data[:] = out
	ncfile.close()

def write2nc_4d(file, nlats, nlons, nlevs, nrecs, press_out, temp_out):
	#  
	#print("Hi We are in 3d netcdf write function")
	ncfile = Dataset(file,'w')
	ncfile.createDimension('latitude',nlats)
	ncfile.createDimension('longitude',nlons)
	ncfile.createDimension('level',nlevs)
	ncfile.createDimension('time',None)
	lats = ncfile.createVariable('latitude',dtype('float32').char,('latitude',))
	lons = ncfile.createVariable('longitude',dtype('float32').char,('longitude',))
	lats.units = 'degrees_north'
	lons.units = 'degrees_east'
	lats[:] = lats_out
	lons[:] = lons_out
	press = ncfile.createVariable('pressure',dtype('float32').char,('time','level','latitude','longitude'))
	temp = ncfile.createVariable('temperature',dtype('float32').char,('time','level','latitude','longitude'))
	press.units =  'hPa'
	temp.units = 'celsius'
	for nrec in range(nrecs):
		press[nrec,:,::] = press_out[nrec,:,::]
		temp[nrec,:,::] = temp_out[nrec,:,::]
	ncfile.close()
#---testing 
if __name__ == "__main__":
	lon = np.empty((4))
	lat = np.empty((4))
	lev = np.empty((4))
	out = np.empty((4,4,4))
	out[:][:][:] = 0.0
	lon[:] = 0.0
	lat[:] = 0.0
	lev[:] = 0.0
	write2nc_3d(lon, lat, lev, out, 'out', 'nx', 'ny', 'nz', 'test.nc' )
#	write2nc(out, 'out', 'nx', 'ny', 'test.nc')
#	write2nc(out, 'out', 'nx', 'ny', 'test.nc')
#---testing 
	#nrecs = 2; nlevs = 2; nlats = 6; nlons = 12; file = "test.nc"
	#lats_out = -25.0 + 5.0*arange(nlats,dtype='float32')
	#lons_out = -125.0 + 5.0*arange(nlons,dtype='float32')
	## output data.
	#press_out = 900. + arange(nrecs*nlevs*nlats*nlons,dtype='float32') # 1d array
	#press_out.shape = (nrecs,nlevs,nlats,nlons) # reshape to 2d array
	#temp_out = 9. + arange(nrecs*nlevs*nlats*nlons,dtype='float32') # 1d array
	#temp_out.shape = (nrecs,nlevs,nlats,nlons) # reshape to 2d array
	#write2nc_4d(file, nlats, nlons, nlevs, nrecs, press_out, temp_out)
	#print('*** SUCCESS writing example file pres_temp_4D.nc')





