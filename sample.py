%pylab inline
data_dir = '/Users/Nicke/Desktop/hackthedinos/test_images'
import os

import numpy as np
import matplotlib.pyplot as plt
import cv2

image_location = os.path.join(data_dir, 'ct_scan_medref.jpg')
image_file = cv2.imread(image_location, 0) # I use openCV for this because I couldn't figure out how to read in an image as greyscale easily
image_array = np.array(image_file)

# plt.imshow(image_array)

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