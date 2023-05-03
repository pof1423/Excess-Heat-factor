import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt


def amplitude(I, Q):
    with rasterio.open(I) as slc_i:
        band_i = slc_i.read(1)
    with rasterio.open(Q) as slc_q:
        band_q= slc_q.read(1)
    
    amplitude = np.sqrt(np.power(band_i,2)+np.power(band_q,2))
    return amplitude

def save_array_totiff(array, nrows,ncols, name, path):
    output_file = path + name + ".tif"
    with rasterio.open(output_file, 'w', driver='GTiff', width=ncols, height=nrows, dtype=np.float32, count=1,
                    crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs +towgs84=0,0,0', transform=None,
                ) as r1:
        r1.write(array, 1)
    