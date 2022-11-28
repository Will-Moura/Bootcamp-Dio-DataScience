
#MÉTODOS DE INTERPOLAÇÃO DE VARIÁVEIS. 
#Temos 3 métodos. dos 3 aseguir o métodos (f) é o melhor.
 
#Método % 
#Método format 
#Método f   

nome = "william"
idade = 23
profissao = "DataScientist"
linguagem = "Python" 
  

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {linguagem} e estou matriculado no curso de {profissao}")   


print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {3}.".format(nome, profissao, idade, linguagem)) 
 
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {linguagem} e estou matriculado no curso de {profissao}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) 
 
