# filename: rgb_hsv.py
# REF: http://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_rgb_to_hsv.html

# RGB -> HSV is done with skimage.color.rgb2hsv()
#    * RGB, HSV data are assumed to be in the ranage [0,1]

import sys
import numpy as np 
import cv2 
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt 
import imageio # this will be used to load an image file
import skimage # rgb <-> hsv conversion in [0,1] pixel scale

# show the image
def imshow (img, title=None):
    if img.ndim == 3: 
        plt.imshow (img)
    else:
        plt.imshow (img, cmap='gray')

    if title is None: title = 'imshow'
    plt.title (title)
    plt.pause (1)
    plt.close ()
#

rgb = imageio.imread ('data/nature.jpg') #https://wallpapercave.com/pretty-nature-wallpapers
if rgb is None:
    print ('image file open error')
    sys.exit ()
#

imshow (rgb, 'RGB Image')

# The conversion assumes an input data range of [0, 1] for all color components.
rgb01 = rgb/255.
hsv = skimage.color.rgb2hsv (rgb01) 
hue = hsv[:,:,0]
saturation = hsv[:,:,1]
value = hsv[:,:,2]

imshow (hue, 'Hue Image')
imshow (saturation, 'Saturation Image')
imshow (value, 'Value Image (== Gray Scale)')

print ('HSV(Red)   = {}'.format(skimage.color.rgb2hsv([[[1.,0,0]]])))
print ('HSV(Yellow)= {}'.format(skimage.color.rgb2hsv([[[1.,1.,0]]])))
print ('HSV(Green) = {}'.format(skimage.color.rgb2hsv([[[0,1.,0]]])))
print ('HSV(Blue)  = {}'.format(skimage.color.rgb2hsv([[[0,0,1.]]])))
print ('HSV(White) = {}'.format(skimage.color.rgb2hsv([[[1.,1.,1.]]])))

hsvpixel = [[[0.999, 1., 1.]]]
print ('RGB({}) = '.format(hsvpixel), skimage.color.hsv2rgb (np.array(hsvpixel)))
hsvpixel = [[[0., 1., 1.]]]
print ('RGB({}) = '.format(hsvpixel), skimage.color.hsv2rgb (np.array(hsvpixel)))

print ('Now Extract Redful pixels only.')
for r in range(hsv.shape[0]):
    for c in range (hsv.shape[1]):
        if (hsv[r,c,0] > 0.9 or hsv[r,c,0] < 0.1):
            pass # this is a red
        else:
            hsv[r,c,:] = [0,0,0] # black
#
rgb_redful = skimage.color.hsv2rgb (hsv)
imshow (rgb_redful, 'Redful')
imageio.imwrite ('data/redful.png', (rgb_redful*255).astype(np.uint8))

# Q. Can you remove white pixels in the clouds?
#    Hint: Examine the HSV Cylinder. ( hsv[r,c,1] > 0.5 )

# Q. Rotate the color along the HUE axis, make a video of the chage.
#    Step = 0, 0.01, 1

# EOF
