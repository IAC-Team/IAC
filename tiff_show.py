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

FILE_2015 = '../IAC_data/preliminary/quickbird2015.tif'
FILE_2017 = '../IAC_data/preliminary/quickbird2017.tif'
FILE_cadastral2015 = '../IAC_data/20170907_hint/cadastral2015.tif'
FILE_tinysample = '../IAC_data/20170907_hint/tinysample.tif'
# 0: g  1: r 2: b 3: ir
# im = tiff.imread(FILE_2017).transpose([1, 2, 0])
#
# im = tiff.imread(FILE_2017).transpose([1, 2, 0])

# im = tiff.imread(FILE_tinysample)

im = tiff.imread(FILE_cadastral2015)

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

# the original code
# fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(16, 6))
#
# p1 = plt.subplot(121)
# i1 = p1.imshow(scale_percentile(im[100:1000, 100:1000, :3]))
# plt.colorbar(i1)
#
# # p2 = plt.subplot(122)
# i2 = p2.imshow(im[100:1000, 100:1000, 3])
# plt.colorbar(i2)


# im.shape


# For 2015&2017 image processing&show
# plt.imshow(scale_percentile(im[50:5000, 50:5000, :3])) # 1st
# plt.imshow(scale_percentile(im[50:5000, 5000:10000, :3])) # 2nd
# plt.imshow(scale_percentile(im[50:5000, 10000:15000, :3])) # 3rd


# For tiny&cadastral image processing&show
# plt.imshow(im[50:5000, 50:5000])
# plt.imshow(im[50:5000, 5000:10000])
plt.imshow(im[50:5000, 10000:15000])


# image saving
plt.savefig('../IAC_data/im_tiny_3.jpg', dpi=2000)


#image show
# plt.show()