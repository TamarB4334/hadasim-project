import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("image.png")  
image_np = np.array(image)

red_channel = image_np[:, :, 0].flatten()
green_channel = image_np[:, :, 1].flatten()
blue_channel = image_np[:, :, 2].flatten()

plt.figure(figsize=(10, 5))

plt.hist(red_channel, bins=256, color='red', alpha=0.5, label='Red')
plt.hist(green_channel, bins=256, color='green', alpha=0.5, label='Green')
plt.hist(blue_channel, bins=256, color='blue', alpha=0.5, label='Blue')

plt.title("RGB Histogram")
plt.xlabel("Color value (0-255)")
plt.ylabel("Pixel count")
plt.legend()
plt.tight_layout()
plt.show()