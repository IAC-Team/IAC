from collections import defaultdict
import csv
import sys

# import cv2
# from shapely.geometry import MultiPolygon, Polygon
# import shapely.wkt
# import shapely.affinity
import numpy as np
import tifffile as tiff

# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import cm

FILE_2015 = './preliminary/quickbird2015.tif'
FILE_2017 = './preliminary/quickbird2017.tif'
FILE_cadastral2015 = './20170907_hint/cadastral2015.tif'
FILE_tinysample = './20170907_hint/tinysample.tif'
# 0: g  1: r 2: b 3: ir
im = tiff.imread(FILE_2015).transpose([1, 2, 0])
#
# im_2017 = tiff.imread(FILE_2017).transpose([1, 2, 0])

# im_tiny = tiff.imread(FILE_tinysample)

# im_cada = tiff.imread(FILE_cadastral2015)

def scale_percentile(matrix):
    w, h, d = matrix.shape
    matrix = np.reshape(matrix, [w * h, d]).astype(np.float64)
    # Get 2nd and 98th percentile
    mins = np.percentile(matrix, 1, axis=0)
    maxs = np.percentile(matrix, 99, axis=0) - mins
    matrix = (matrix - mins[None, :]) / maxs[None, :]
    matrix = np.reshape(matrix, [w, h, d])
    matrix = matrix.clip(0, 1)
    return matrix

# fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(16, 6))
#
# p1 = plt.subplot(121)
# i1 = p1.imshow(scale_percentile(im[100:1000, 100:1000, :3]))
# plt.colorbar(i1)
#
# # p2 = plt.subplot(122)
# i2 = p2.imshow(im[100:1000, 100:1000, 3])
# plt.colorbar(i2)

# im = scale_percentile(im[100:1000, 100:1000, :1])
plt.imshow(scale_percentile(im[50:5000, 50:5000, :3]))
# plt.imshow(im[10:20, 10:20,:3])
# plt.savefig('im_2015.jpg', , dpi=1000)
plt.show()
