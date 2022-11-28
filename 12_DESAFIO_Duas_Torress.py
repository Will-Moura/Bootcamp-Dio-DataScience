# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# Abaixo segue um exemplo de código que você pode ou não utilizar 
   
 #entrada = input("informe as três distancias separadas").split()

#distancia = int(entrada[0])
#diametro1 = int(entrada[1])
#diametro2 = int(entrada[2]) 
 
#icm = (distancia) / (diametro1 + diametro2) 
#print(f"O valor de ICM é: {icm:.2f}") 
 
entrada = input("informe as três distancias separadas por virgula").split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2]) 
 
icm = (distancia) / (diametro1 + diametro2) 
print(f"O valor de ICM é: {icm:.2f}")


