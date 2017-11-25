import numpy as np
import scipy
from scipy import ndimage

im = scipy.misc.imread('output_image.png',flatten=1)
im = np.where(im > 128, 0, 1)
label_im, num = ndimage.label(im)
slices = ndimage.find_objects(label_im)
centroids = ndimage.measurements.center_of_mass(im, label_im, xrange(1,num+1))

angles = []
for s in slices:
    height, width = label_im[s].shape
    opp = height - np.where(im[s][:,-1]==1)[0][-1] - 1
    adj = width - np.where(im[s][-1,:]==1)[0][0] - 1
    angles.append(np.degrees(np.arctan2(opp,adj)))
print 'centers:', centroids
print 'angles:', angles
