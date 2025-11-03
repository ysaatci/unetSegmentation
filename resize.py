from PIL import Image
from skimage import data, io, filters
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from sklearn import manifold, datasets

n=136 #number of images
for i in range (1,n+1):
        path=str(i)+'.tif'
        img = io.imread('/home/batu/Desktop/test_annotate/'+path)
        #Subsection of the image
        img=img[36:544,64:576] #580 640 512
        print(img.shape)
        path=str(i)+'.tif'
        io.imsave('/home/batu/Desktop/AlteredDims/tiff_form_test_annotate/'+path,img)
