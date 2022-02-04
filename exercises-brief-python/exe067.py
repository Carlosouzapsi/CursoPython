from math import sqrt

perimetro = 0

coord_x = float(input('Informe a primeira coordenada do ponto x: '))
coord_y = float(input('Informe a primeira coordenada do ponto y: '))
anterior_x = coord_x
anterior_y = coord_y
proxima_coord_x = str(input('Informe a próxima coordenada do ponto x: '))
while proxima_coord_x != "":
    proxima_coord_x = float(proxima_coord_x)
    proxima_coord_y = float(input('Informe a próxima coordenada do ponto y: '))
    distancia = sqrt((anterior_x - proxima_coord_x) ** 2 + (anterior_y - proxima_coord_y) ** 2)
    perimetro = perimetro + distancia
    anterior_x = proxima_coord_x
    anterior_y = proxima_coord_y
    proxima_coord_x = str(input('Informe a próxima coordenada do ponto x: '))

distancia = sqrt((coord_x - proxima_coord_x) ** 2 + (coord_y - proxima_coord_y) ** 2)
perimetro = perimetro + distancia

print(f"O perímetro do polígono é: {perimetro}")
