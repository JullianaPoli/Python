# If, else, ilif

saldo = 2000.0
saque = float(input("Informe o valor do Saque"))

if saldo >= saque:
    print("Realizado saque!")
    
if saldo < saque:
    print("Saldo insuficiente!")
    
# outra forma usando IF / ELSE.
print("\n")
        
saldo = 2000.0
saque = float(input("Informe o valor do Saque"))

if saldo >= saque:
    print("Realizado saque!")
else: 
    print("Saldo insuficiente")    
    
    
# Codigo usando IF / ELIF / ELSE 

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    
elif opcao == 2:
    print("Exibindo o extrato...  ")
    
else:
    SystemExit.exit("Opção inválida")
    
# em uma estrutura de codigo pode ser usado o elif quantas vezes forem necessarias.

# IF

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar sua CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")    
    
print("\n")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")        
    
print("\n")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
    
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas.")    
    
else:
    print("Ainda não pode tirar a CNH")        
    
print("\n")    

# IF ANINHADO

#if conta_normal:
#  if saldo >= saque:
    # print("Saque realizado com sucesso!")
#  elif saque <=(saldo + cheque_especial):
    # print("Saque realizida com uso do cheque especial")
#elif conta_universitatia:
   #if saldo >= saque: 
    #print(" Saque realizado com sucesso"!)
   #else:
   #print("Saldo insuficiente")
   
print("\n") 
  
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450 
  
if conta_normal:
    if saldo >= saque:
      print("Saque realizado com sucesso")
      
    elif saque <= (saldo + cheque_especial):
      print("Saque realizado com uso do cheque especial")
      
elif conta_universitaria:
    if saldo >= saque: 
      print("Saque realizado com sucesso")      
    else:
      print("Saldo insuficiente")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente")
    
    
print("\n")    

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")