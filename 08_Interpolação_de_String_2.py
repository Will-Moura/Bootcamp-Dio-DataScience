nome = "william"
idade = 23
profissao = "DataScientist"
linguagem = "Python" 
saldo = 1212
dados = {"nome":"Will", "idade":23}

print("nome: %s, idade: %d" %(nome, idade)) 

print("nome: {}, idade: {}".format(nome, idade))
print("nome: {0}, idade: {1}".format(nome, idade)) 
print("nome: {nome}, idade: {idade}".format(nome=nome, idade=idade))
print("nome: {name}, idade: {age}".format(name=nome, age=idade))
print("nome: {nome}, idade: {idade}".format(**dados))  

print(f"nome: {nome}, idade: {idade}") 
 
print(f"nome: {nome}, idade: {idade} Saldo: {saldo:5.2f}")