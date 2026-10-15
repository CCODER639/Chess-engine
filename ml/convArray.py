
from PIL import Image
import numpy as np

image = Image.open("number.png").convert("L")

array = np.array(image)

print(array)