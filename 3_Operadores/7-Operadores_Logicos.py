# O que são operadores lógicos?
#São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.

print("\n")
# Exemplos 

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)

# o operador AND precisa que a 1º expressão seja verdadeira e a 2º também. Ou seja, todas as expressões precisam ser verdadeiras.
 
print("\n")
 
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)

# Operador OR se eu tenho verdade ou verdade é verdadeiro, se eu tenho verdade ou falso é verdade, se eu tenho falso ou verdadeiro é verdade.

print("\n")

# Operador de Negação

contratos_emergencia = []

not 1000 > 1500

not contratos_emergencia

not "Saque 1500"

not ""

print("\n")

# Parênteses 

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print( saldo>= saque and saque <= limite or conta_especial and saldo >= saque)
print("\n")
print((saldo>= saque and saque <= limite) or (conta_especial and saldo >= saque))

