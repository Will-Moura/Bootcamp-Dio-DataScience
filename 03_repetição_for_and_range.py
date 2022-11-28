 
#usando o "for" 
texto = input("Informe um texto.")
VOGAIS = "AEIOU"

#exemplo usando o literável 
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") 
else:
    print()
    print("executa no final do laço")  

     

#Exemplo usando a função built-in range
for numero in range (0,51,5):
    print(numero, end=" ") 
     

 
