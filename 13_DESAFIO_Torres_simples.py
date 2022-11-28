entrada = input(200, 3, 8).split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

icm = (distancia) / (diametro1 + diametro2) 
print(f"O valor de ICM é: {icm:.2f}")