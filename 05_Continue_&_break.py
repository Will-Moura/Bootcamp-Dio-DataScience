#Utilizando o continue (continue = pular uma execução)
 
for numero in range(100):
    if numero % 2 == 0:
        continue 
    print(numero, end=" ") 
     


#Usando o continue e break  (break = pausar uma execução)  
while True:
    numero = int(input("Informe um número: ")) 
    
    if numero % 2 == 0:
        continue
    if numero == 10:
        break 
    print(numero)