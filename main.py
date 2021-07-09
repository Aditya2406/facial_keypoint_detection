from PIL import Image
import numpy as np
image = Image.open('test03.png')
img_resized = image.resize((96,96))
F_image = image.convert(mode='L')
F_image= F_image.save("test03_bw.png")
arr=np.asarray(F_image)
print(arr)


