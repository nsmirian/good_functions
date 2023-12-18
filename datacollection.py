
# collectind data for compressions and BAMs
# fisrst step of VFD project,
# Najmeh Mitian 18 Dec 2023

import time
import pydoocs
import numpy as np
import matplotlib.pyplot as plt

# preperation of vectors
nshot=1000

addr_cam        = 'FLASH.DIAG/CAMERA/OTR9FL2XTDS/IMAGE_EXT_ZMQ';
compressionTD11='FLASH.SDIAG/BCM/FL0.DBC1.1/COMPRESSION.normalized.TD'
#img(:,:,jj)     = ddd_read.data.val_val;
com11=pydoocs.read(compressionTD11)
a,b=com11['data'].shape
com11=np.zeros([a,b,nshot])
##
compressionTD12='FLASH.SDIAG/BCM/FL0.DBC1.2/COMPRESSION.normalized.TD'
com12=pydoocs.read(compressionTD12)
a,b=com12['data'].shape
com12=np.zeros([a,b,nshot])
compressionTD21='FLASH.SDIAG/BCM/FL0.DBC2.1/COMPRESSION.normalized.TD'
com21=pydoocs.read(compressionTD21)
a,b=com21['data'].shape
com21=np.zeros([a,b,nshot])
##
compressionTD21='FLASH.SDIAG/BCM/FL0.DBC2.1/COMPRESSION.normalized.TD'
com21=pydoocs.read(compressionTD21)
a,b=com21['data'].shape
com21=np.zeros([a,b,nshot])
##
compressionTD22='FLASH.SDIAG/BCM/FL0.DBC2.2/COMPRESSION.normalized.TD'
com22=pydoocs.read(compressionTD22)

a,b=com22['data'].shape
com22=np.zeros([a,b,nshot])
#plt.plot(S21['data'][1:,0], S21['data'][1:,1], '.')
#plt.plot(S22['data'][1:,0], S22['data'][1:,1], '.')

compressionTD51='FLASH.SDIAG/BCM/FL2.SEED5.1/COMPRESSION.normalized.TD'
com51=pydoocs.read(compressionTD51)
a,b=com51['data'].shape
com51=np.zeros([a,b,nshot])
##
compressionTD52='FLASH.SDIAG/BCM/FL2.SEED5.2/COMPRESSION.normalized.TD'
com52=pydoocs.read(compressionTD52)
a,b=com52['data'].shape
com52=np.zeros([a,b,nshot])
#
BAMUBC1='FLASH.SDIAG/BAM/FL0.UBC1/ARRIVAL_TIME.relative.TD'
bamuBC1=pydoocs.read(BAMUBC1)
a,b=bamuBC1['data'].shape
bamuBC1=np.zeros([a,b,nshot])

BAMseed5='FLASH.SDIAG/BAM/FL2.SEED5/ARRIVAL_TIME.relative.TD'
bamuseed5=pydoocs.read(BAMseed5)
a,b=bamuseed5['data'].shape
bamuseed5=np.zeros([a,b,nshot])

#### cammper , do not forget
cammeraT=''


for n in range(nshot):
    com11[:,:, n]=pydoocs.read(compressionTD11)['data']
    com12[:,:, n]=pydoocs.read(compressionTD12)['data']
    com21[:,:, n]=pydoocs.read(compressionTD21)['data']
    com22[:,:, n]=pydoocs.read(compressionTD22)['data']
    com51[:,:, n]=pydoocs.read(compressionTD51)['data']
    com52[:,:, n]=pydoocs.read(compressionTD52)['data']

    bamuBC1[:,:, n]=pydoocs.read(BAMUBC1)['data']
    bamuseed5[:,:, n]=pydoocs.read(BAMUBCseed5)['data']
     time.sleep( 0.1 )
     print(n)
    ## camera image

hf = h5py.File('data.h5', 'w')
hf.create_dataset('com11', data=com11)
hf.create_dataset('com12', data=com12)
hf.create_dataset('com21', data=com21)
hf.create_dataset('com22', data=com22)
hf.create_dataset('com51', data=com51)
hf.create_dataset('com52', data=com52)

hf.create_dataset('bamuBC1', data=bamuBC1)
hf.create_dataset('bamuseed5', data=bamuseed5)



hf.close()
