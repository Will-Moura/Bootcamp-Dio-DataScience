valores = input().split(" ")  
 
tempo_em_horas = int(valores[0])
velocidade_media = int(valores[1])
  
distancia = (tempo_em_horas) * (velocidade_media)

carro_faz_km = 12  
 
Litros_totais_gastos = distancia / carro_faz_km 

print(f"{Litros_totais_gastos:.3f}")