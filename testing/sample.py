import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
from skimage import measure
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral

## Import image and convert

image_location = os.path.join(data_dir, 'ct_scan_medref.jpg')
image_file = cv2.imread(image_location, 0) # Still using openCV to read in the image. Should fix.
image_array = np.array(image_file)

plt.imshow(image_array)

## Denoise image

image_array2 = denoise_tv_chambolle(image_array, weight=100, multichannel=True)

# plt.show(image_array2)

## Find contours
contours = measure.find_contours(image_array, 100)
contour_thresh = 60
large_contours = [x for x in contours if len(x) > contour_thresh]
# large_contours = remove_small_objects(contours)

# # Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(image_array2, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(large_contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()