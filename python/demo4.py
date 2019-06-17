import scipy

from scipy import misc, signal
import numpy as np

#im = misc.imread('../images/lena.jpg')/255. # scale pixel values in [0,1] for each channel

im = scipy.misc.face(gray=True).astype(float)

print(np.max(im))
# 1.0
print(im.shape)
# (220, 220, 3)

sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
im_sharpened = np.ones(im.shape)
for i in range(3):
    im_sharpened[...,i] = np.clip(signal.convolve2d(im[...,i], sharpen_kernel, mode='same', boundary="symm"),0,1)

fig, ax = plt.subplots(nrows=2, figsize=(10, 20))
ax[0].imshow(im)
ax[0].set_title('Original Image', size=20)
ax[1].imshow(im_sharpened)
ax[1].set_title('Sharpened Image', size=20)
plt.show()
