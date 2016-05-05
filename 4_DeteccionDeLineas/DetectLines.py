import numpy as np
from sys import argv
import cv2

#Obtener imagen
nombreImagen = argv[1]
img = cv2.imread(nombreImagen,0)
ancho, alto = img.shape

#Bordes
edges = cv2.blur(img,(2,2))
edges = cv2.Canny(edges,90,180,)
cv2.imwrite(nombreImagen + 'BORDES.jpg', edges)
print "Se guardo imagen bordes"

# Rho and Theta ranges
thetas = np.deg2rad(np.arange(-90.0, 90.0))
width, height = img.shape
diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)

# Cache some resuable values
cos_t = np.cos(thetas)
sin_t = np.sin(thetas)
num_thetas = len(thetas)


# Hough array de los votos
accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint64)
y_idxs, x_idxs = np.nonzero(edges)  # (row, col) de los que no son cero, es  decir son bordes

# Vote in the hough accumulator
for i in range(len(x_idxs)):
    x = x_idxs[i]
    y = y_idxs[i]

    for t_idx in range(num_thetas):
        # Calculate rho. diag_len is added for a positive index
        rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
        accumulator[rho, t_idx] += 1

cv2.imwrite(nombreImagen + 'LINEAS1.jpg', accumulator)
print "Se guardo imagen de matriz de votos"

maxAcc = np.argmax(accumulator)
votes = accumulator[maxAcc / accumulator.shape[1], maxAcc % accumulator.shape[1]] - 35

#Obtiene los picos y hace las lineas
ix, jy = int(2 * diag_len), int(num_thetas)
for i in range(ix):
    for j in range(jy):
        if accumulator[i,j] > votes:
            #Si tiene mas de 100votos
            idx = np.argmax(accumulator)
            rho = rhos[idx / accumulator.shape[1]]
            theta = thetas[idx % accumulator.shape[1]]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
            #Borra ese punto mayor
            accumulator[idx / accumulator.shape[1],idx % accumulator.shape[1]] = 0
        else:
            accumulator[i,j] = 0


cv2.imwrite(nombreImagen + 'LINEAS2.jpg', img)
print "Se guardo imagen con lineas"
