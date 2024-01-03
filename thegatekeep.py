# Chapter 1: The Gatekeeper

    from PIL import Image
import numpy as np

# Load the image
img_path = 'chapter1.jpg'
img = Image.open(img_path)

# Convert to numpy array
img_array = np.array(img)

# Define the number to add (this is arbitrary, normally you would provide this)
number_to_add = 10

# Modify the image's pixel values
# Ensuring that the values stay within the 0-255 range
modified_img_array = np.clip(img_array + number_to_add, 0, 255)

# Convert back to an image
modified_img = Image.fromarray(modified_img_array.astype('uint8'))

# Save the modified image
modified_img_path = 'chapter1out.png'
modified_img.save(modified_img_path)

# Calculate the sum of the red pixel values in the new image
sum_red_values = np.sum(modified_img_array[:,:,0])

sum_red_values
