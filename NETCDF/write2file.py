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

def write2nc_3d(lon, lat, lev, out, out_name, dimx_name, dimy_name, dimz_name, file_name ):
	nx = out.shape[0]
	ny = out.shape[1]
	nz = out.shape[2]
	ncfile = Dataset(file_name,'w') 
	ncfile.createDimension(dimx_name, nx)
	ncfile.createDimension(dimy_name, ny)
	ncfile.createDimension(dimz_name, nz)
	data_lon = ncfile.createVariable("lon", "f4", ("lon",))
	data_lat = ncfile.createVariable("lat", "f4", ("lat",))
	data_lev = ncfile.createVariable("lev", "f4", ("lat",))
	data = ncfile.createVariable(out_name, dtype('float').char,(dimx_name, dimy_name, dimz_name))

	data_lon.units = 'K/hr'
	data_lon.long_name = 'longitude' 
	data_lat.units = 'degrees'
	data_lat.long_name = 'latitude' 
	data.units = 'K/hr'
	data.long_name = '2H25 latent heating (SLH)'
	data._FillValue = '-999.f'
	data.missing_value = '-999.f'
	data.valid_range = '-400.f, -400.f'

	data_lon[:] = lon
	data_lat[:] = lat
	data_lev[:] = lev
	data[:] = out
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




