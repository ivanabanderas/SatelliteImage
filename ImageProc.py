import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pytesseract

img = cv.imread('imagen.jpg') 
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.GaussianBlur(mask, (31, 31), 0)


plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(blur, cmap='gray')
plt.title("Procesada")
plt.xticks([]), plt.yticks([])

plt.show()

texto = pytesseract.image_to_string(blur, lang='spa')

print("\nTexto detectado:")
print(texto)
