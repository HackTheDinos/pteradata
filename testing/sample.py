%pylab inline
data_dir = '/Users/Nicke/Desktop/hackthedinos/test_images'
import os

import numpy as np
import matplotlib.pyplot as plt
# import cv2
import matplotlib.image as mpimg

# Need this to convert images to greyscale. I don't like the way I do this--there's gotta be a better way
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

image_location = os.path.join(data_dir, 'ct_scan_medref.jpg')
# image_file = cv2.imread(image_location, 0)
image_array = np.array(image_file)

image_file = mpimg.imread(image_location)
gray = rgb2gray(image_file)
image_array = np.array(gray)

plt.imshow(image_array)

contours = measure.find_contours(image_array, 100)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(image_array, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()