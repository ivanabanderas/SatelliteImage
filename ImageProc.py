import cv2 as cv #Importamos para procesar las imagenes
import matplotlib.pyplot as plt #Para visualizar las imagenes
import numpy as np

#Cargar la imagen desde su ruta
img = cv.imread('satelite2.jpg') 
assert img is not None, "file could not be read, check with os.path.exists()"

# procesamiento
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
black_pixels = np.where(gray <= 20, 255, 0).astype(np.uint8)
kernel = np.ones((5, 5), np.uint8)
morph_gradient = cv.morphologyEx(black_pixels, cv.MORPH_GRADIENT, kernel)
blur = cv.GaussianBlur(morph_gradient, (29,29), 0)
_, thresh = cv.threshold(blur, 30, 255, cv.THRESH_BINARY_INV)

# dibujo
lines = cv.HoughLinesP(thresh, 1, np.pi / 180, threshold=200, minLineLength=100, maxLineGap=20)
filtered_lines_img = img.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(filtered_lines_img, (x1, y1), (x2, y2), (128, 0, 255), 2)

# mostrar
plt.figure(figsize=(8, 8))

plt.imshow(cv.cvtColor(filtered_lines_img, cv.COLOR_BGR2RGB))
plt.title("Líneas Filtradas de las Calles")
plt.axis("off")
plt.show()
