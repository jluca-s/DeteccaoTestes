import cv2
import numpy as np
import os

largura, altura = 220, 220
amostra = 1
id = 3
caminhos = [os.path.join('fotos3', f) for f in os.listdir('fotos3')]
print (caminhos)

for caminhoImagem in caminhos:
    imagemCinza = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
    imagemFace = cv2.resize(imagemCinza, (largura, altura))
    cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
    amostra += 1

print("Faces convertidas com sucesso!")