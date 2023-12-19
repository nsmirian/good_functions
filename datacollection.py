
# Collect data for compressions and BAMs
# First step of VFD project,
# Najmeh Mitian 18 Dec 2023

import time
import pydoocs
import numpy as np
import matplotlib.pyplot as plt
import h5py

# preperation of vectors
nshot=1000

addr_cam        = 'FLASH.DIAG/CAMERA/OTR9FL2XTDS/IMAGE_EXT_ZMQ';
compressionTD11='FLASH.SDIAG/BCM/FL0.DBC1.1/COMPRESSION.normalized.TD'
#img(:,:,jj)     = ddd_read.data.val_val;
com11=pydoocs.read(compressionTD11)
a,b=com11['data'].shape
com11=np.zeros([a,b,nshot])
com11_timespam==np.zeros([nshot])
##
compressionTD12='FLASH.SDIAG/BCM/FL0.DBC1.2/COMPRESSION.normalized.TD'
com12=pydoocs.read(compressionTD12)
a,b=com12['data'].shape
com12=np.zeros([a,b,nshot])
compressionTD21='FLASH.SDIAG/BCM/FL0.DBC2.1/COMPRESSION.normalized.TD'
#com21=pydoocs.read(compressionTD21)
#a,b=com21['data'].shape
com21=np.zeros([a,b,nshot])
com21_timespam==np.zeros([nshot])
##
#
##
compressionTD22='FLASH.SDIAG/BCM/FL0.DBC2.2/COMPRESSION.normalized.TD'
#com22=pydoocs.read(compressionTD22)
#com22_timespam==np.zeros([nshot])

#a,b=com22['data'].shape
com22=np.zeros([a,b,nshot])
com22_timespam==np.zeros([nshot])
#plt.plot(S21['data'][1:,0], S21['data'][1:,1], '.')
#plt.plot(S22['data'][1:,0], S22['data'][1:,1], '.')

compressionTD51='FLASH.SDIAG/BCM/FL2.SEED5.1/COMPRESSION.normalized.TD'
com51=pydoocs.read(compressionTD51)
a,b=com51['data'].shape
com51=np.zeros([a,b,nshot])
com51_timespam==np.zeros([nshot])
##
compressionTD52='FLASH.SDIAG/BCM/FL2.SEED5.2/COMPRESSION.normalized.TD'
com52=pydoocs.read(compressionTD52)
a,b=com52['data'].shape
com52=np.zeros([a,b,nshot])
com52_timespam==np.zeros([nshot])
#
BAMUBC1='FLASH.SDIAG/BAM/FL0.UBC1/ARRIVAL_TIME.relative.TD'
bamuBC1=pydoocs.read(BAMUBC1)
a,b=bamuBC1['data'].shape
bamuBC1=np.zeros([a,b,nshot])
bamuBC1_timespam==np.zeros([nshot])

BAMseed5='FLASH.SDIAG/BAM/FL2.SEED5/ARRIVAL_TIME.relative.TD'
bamuseed5=pydoocs.read(BAMseed5)
a,b=bamuseed5['data'].shape
bamuseed5=np.zeros([a,b,nshot])
bamuseed5_timespam==np.zeros([nshot])

#### cammper , do not forget
cammeraT=''
timespam_img=np.zeros([nshot])
cam_img=np.zeros([1776,2360,nshot])

for n in range(nshot):
    com11[:,:, n]=pydoocs.read(compressionTD11)['data']
    #com11_timespam[n]=pydoocs.read(compressionTD11)['timestamp']
    com12[:,:, n]=pydoocs.read(compressionTD12)['data']
    #com12_timespam[n]=pydoocs.read(compressionTD12)['timestamp']
    #com21[:,:, n]=pydoocs.read(compressionTD21)['data']
    #com21_timespam[n]=pydoocs.read(compressionTD21)['timestamp']
    #com22[:,:, n]=pydoocs.read(compressionTD22)['data']
    #com22_timespam[n]=pydoocs.read(compressionTD22)['timestamp']
    com51[:,:, n]=pydoocs.read(compressionTD51)['data']
    #com51_timespam[n]=pydoocs.read(compressionTD51)['timestamp']
    com52[:,:, n]=pydoocs.read(compressionTD52)['data']
    #com52_timespam[n]=pydoocs.read(compressionTD52)['timestamp']

    bamuBC1[:,:, n]     =pydoocs.read(BAMUBC1)['data']
    #bamuBC1_timespam[n]=pydoocs.read(BAMUBC1)['timestamp']
    bamuseed5[:,:, n]   =pydoocs.read(BAMseed5)['data']
    bamuseed5_timespam[n]=pydoocs.read(BAMseed5)['timestamp']
    
    cam_img[:,:, n]=pydoocs.read(addr_cam)['data']
    cam_img_timespam[n]=pydoocs.read(addr_cam)['timestamp']
    
    time.sleep( 0.1 )
    print(n)
    ## camera image
data_dict = {
    '1': {
        'com11': com11,
        'com12': com12,
        'com11_timespam': com11_timespam,
        'com12_timespam': com12_timespam,
        },
    '2': {
        'com21': com21,
        'com22': com22,
        'com21_timespam': com21_timespam,
        'com22_timespam': com22_timespam,
        }
   
    '5': {
        'com51': com51,
        'com52': com52,
        'com51_timespam': com51_timespam,
        'com52_timespam': com52_timespam,
        }
     'bams': {
        'bamuBC1': bamuBC1,
        'bamuseed5': bamuseed5,
        'bamuBC1_timespam': bamuBC1_timespam,
        'bamuseed5_timespam': bamuseed5_timespam,
        }
    'camera_image': {
        'cam_img': cam_img,
        'cam_img_timespam': cam_img_timespam,
        }

}


#######################################################################
##### Open HDF5 file and write in the data_dict structure and info
f = h5py.File('data.hdf5', 'w')
for grp_name in data_dict:
    grp = f.create_group(grp_name)
    for dset_name in data_dict[grp_name]:
        dset = grp.create_dataset(dset_name, data = data_dict[grp_name][dset_name])
        print(grp_name, dset_name, data_dict[grp_name][dset_name])
f.close()


#hf = h5py.File('data.h5', 'w')
#hf.create_dataset('com11', data=com11)
#hf.create_dataset('com12', data=com12)
#hf.create_dataset('com21', data=com21)
#hf.create_dataset('com22', data=com22)
#hf.create_dataset('com51', data=com51)
#hf.create_dataset('com52', data=com52)

#hf.create_dataset('bamuBC1', data=bamuBC1)
#hf.create_dataset('bamuseed5', data=bamuseed5)



#hf.close()


# #####Re-open HDF5 file and read out the data_dict structure and info
#f = h5py.File('test.hdf5', 'r')
#for grp_name in data_dict:
#    for dset_name in data_dict[grp_name]:
#        if '_array' in dset_name:
 #           print(grp_name, dset_name, f[grp_name][dset_name][:])
 #       if '_scalar' in dset_name:
 #           print(grp_name, dset_name, f[grp_name][dset_name][()])
#f.close()
