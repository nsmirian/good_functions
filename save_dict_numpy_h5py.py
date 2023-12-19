"""
Save NumPy arrays in a dictionary structure into a HDF5 file.
Ref:
  http://docs.h5py.org
  copy from github
"""

import numpy as np
import h5py
import os

# Create a dictionary storing NumPy arrays
data_dict = {
    '0': {
        'a_array': np.random.random(size = 4),
        'b_array': 10 * np.random.random(size = 4),
        'c_array': 100 * np.random.random(size = 4),
        'd_scalar': 1.23
        },
    '1': {
        'a_array': np.random.random(size = 4),
        'b_array': 10 * np.random.random(size = 4),
        'c_array': 100 * np.random.random(size = 4),
        'd_scalar': 12.3
        }
}

# Open HDF5 file and write in the data_dict structure and info
f = h5py.File('test.hdf5', 'w')
for grp_name in data_dict:
    grp = f.create_group(grp_name)
    for dset_name in data_dict[grp_name]:
        dset = grp.create_dataset(dset_name, data = data_dict[grp_name][dset_name])
        print(grp_name, dset_name, data_dict[grp_name][dset_name])
f.close()

# Re-open HDF5 file and read out the data_dict structure and info
f = h5py.File('test.hdf5', 'r')
for grp_name in data_dict:
    for dset_name in data_dict[grp_name]:
        if '_array' in dset_name:
            print(grp_name, dset_name, f[grp_name][dset_name][:])
        if '_scalar' in dset_name:
            print(grp_name, dset_name, f[grp_name][dset_name][()])
f.close()

# Remove temporary data file
if os.path.isfile('test.hdf5'): os.remove('test.hdf5')
