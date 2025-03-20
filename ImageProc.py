import cv2 as cv #Importamos para procesar las imagenes
import matplotlib.pyplot as plt #Para visualizar las imagenes
import numpy as np #Para detectar los pixeles negros

#Cargar la imagen desde su ruta
img = cv.imread('satelite2.jpg') 
assert img is not None, "file could not be read, check with os.path.exists()" #mensaje de error en caso de que el path no sea correcto

# procesamiento
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #cambia la imagen a escala de grises
black_pixels = np.where(gray <= 20, 255, 0).astype(np.uint8) #detecta aquellos pixeles negros
kernel = np.ones((5, 5), np.uint8) #crea el kernel para hacer el gradiante
morph_gradient = cv.morphologyEx(black_pixels, cv.MORPH_GRADIENT, kernel) #gradiente para resaltar los bordes
blur = cv.GaussianBlur(morph_gradient, (29,29), 0)  #reducir ruido con el filtro gaussiano 
_, thresh = cv.threshold(blur, 30, 255, cv.THRESH_BINARY_INV)  #treshold para regresar los pixeles negros

# dibujo
#trasnformada de houghes para detectar lineas en la imegen 
lines = cv.HoughLinesP(thresh, 1, np.pi / 180, threshold=200, minLineLength=100, maxLineGap=20) #treshold: es el número de interscecciones necesarias, min para ser detectada, max separación permitdida para ser considerada línea
filtered_lines_img = img.copy() #crea una copia para mostrar la imagen
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0] #extrae las coordenadas
        cv.line(filtered_lines_img, (x1, y1), (x2, y2), (128, 0, 255), 2)  #las dibuja sobre la copia en color rosa

# mostrar
plt.figure(figsize=(8, 8)) #tamaño de la figura

plt.imshow(cv.cvtColor(filtered_lines_img, cv.COLOR_BGR2RGB)) #convierte el formato de opencv a matplotlib
plt.title("Líneas Filtradas de las Calles")  #título de la figura
plt.axis("off")  #para no dibujar los axis 
plt.show()   #muestra la figura
