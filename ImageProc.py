import cv2 as cv #Importamos para procesar las imagenes
import matplotlib.pyplot as plt #Para visualizar las imagenes
import numpy as np

#Cargar la imagen desde su ruta
img = cv.imread('imagen.jpg') 
assert img is not None, "file could not be read, check with os.path.exists()"

#Aplica un filtro Gaussiano para reducir el ruido
blur = cv.GaussianBlur(img, (31, 31), 0)

#Crea la figura para poder procesar la imagen
plt.figure(figsize=(12, 6))

#Muestra la imagen original
plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.xticks([]), plt.yticks([])

#Muestra la imagen con el filtro correcto
plt.subplot(1, 3, 2)
plt.imshow(blur, cmap='gray')
plt.title("Procesada")
plt.xticks([]), plt.yticks([])

#Muestra todas las imagenes
plt.show()
