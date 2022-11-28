conta_normal = True
conta_universitaria = False
  
saldo = 500
saque = 1000
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado!. Você está utilizando o cheque especial")
    else:
        print("Não foi possível realizar o saque. Saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso! ") 
    else:
        print("Saldo insuficiente.") 
else: 
    print("Erro 403. O número da conta que o senhor utilizou não consta em nosso banco de dados.")
