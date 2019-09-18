import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

filename = 'data/img536.jpg'

# using imageio
import imageio

imio = imageio.imread (filename)

print ('imageio.imread(): ', type(imio), ' a subclass of np.ndarray')
print ('meta: ', imio.meta)
print ('numpy array can be obtained through ')
plt.imshow (imio)
plt.title ('imageio RGB')
plt.pause(2)

# using opencv
imcv = cv.imread(filename)

print ('opencv.imread(): ', type(imcv))

plt.imshow (imcv)
plt.title ('opencv BGR')
plt.pause(2)

# using PIL
from PIL import Image

impil = Image.open (filename)

print ('PIL.Image.open(): ', type(impil))

plt.imshow (impil)
plt.title ('PIL.Image RGB')
plt.pause(2)
