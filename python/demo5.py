import scipy
import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt


im = misc.imread('1zb705v.png') / 255.0 # scale pixel values in [0,1] for each channel

#im = misc.imread('lena.png') / 255.0 # scale pixel values in [0,1] for each channel
print( "type of im = ", type(im), " ", im.shape )

#im = scipy.misc.face()
#im = im[0:512, 0:512, 0:3]
#print( "type of im = ", type(im), " ", im.shape )

# First a 1-D Gaussian
t = np.linspace(-10, 10, 30)
bump = np.exp(-0.1*t**2)
bump /= np.trapz(bump) # normalize the integral to 1

# make a 2-D kernel out of it
kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

im_blur = ndimage.convolve(im, kernel.reshape(30,30,1))

im_sharp = np.clip(2*im - im_blur, 0, 1)

fig, ax = plt.subplots(nrows=3, figsize=(10, 20))

ax[0].imshow(im)
ax[0].set_title('Original Image', size=20)

ax[1].imshow(im_sharp)
ax[1].set_title('Sharpened Image', size=20)

ax[2].imshow(255 - (im_sharp - im) )
ax[2].set_title('Sharpened Image', size=20)

plt.show()
