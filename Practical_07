from scipy import misc,ndimage
import numpy as np
import matplotlib.pyplot as plt 

# 1 ----------------------------------------
image = misc.face()
plt.imshow(image)
plt.imsave("output1.jpg",image)
plt.show()

# 2 -----------------------------------------
# Every image is just a numerical matrix, to change the rows of matrix to columns 
# and vice-vera use the flipud() methods provided by the numpy by passing the original 
# image matrix  
upside_down_image = np.flipud(image) 
plt.imsave("output2.jpg",upside_down_image)
plt.imshow(upside_down_image)
plt.show()

# 3 ----------------------------------------
# Rotates the original image by 45
rotate_image = ndimage.rotate(image,45)
plt.imsave("output3.jpg",rotate_image)
plt.imshow(rotate_image)
plt.show()

# 4 -----------------------------------------
# Adding Blur To The Image 
blurred_image = ndimage.gaussian_filter(image,sigma=12) # Sigma define the intensity of Gausian Blur 
plt.imsave("output4.jpg",blurred_image)
plt.imshow(blurred_image)
plt.show()

# 5 ------------------------------------------  
# Edge-Detection using the sobel function 
image = plt.imread('output1.jpg')

# Convert the image to grayscale
gray_image = np.mean(image, axis=2)

# Apply the Sobel operator to detect edges
sobel_x = ndimage.sobel(gray_image, axis=0, mode='constant')
sobel_y = ndimage.sobel(gray_image, axis=1, mode='constant')

# Calculate the magnitude of the gradients
edge_strength = np.hypot(sobel_x, sobel_y)

# Display the original image and the detected edges
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot-01 
axes[0].imshow(image)
axes[0].set_title('Original Image')

# Plor-02 
axes[1].imshow(edge_strength, cmap='gray')
axes[1].set_title('Edge Detection')
plt.imsave("output5.jpg",edge_strength)
plt.show()
