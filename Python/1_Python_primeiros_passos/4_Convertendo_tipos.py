# variaveis do tipo string, que armazenam numeros e precisamos fazer alguma operação matematica com esse valor # 

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

preco = 10
print(preco)

print(preco / 2) # Resultado 5.0 (quando eu tenho um numero inteiro e utilizo apenas 1 barra '/' ele me retorna um numero float) #

print(preco // 2) # Resultado 5 (quando eu tenho um numero inteiro e utilizo apena 2 barra '//' ele me retorna um numero inteiro, ele preserva o numero da variavel) #

# Exemplo numerico para string #

preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

# Exemplo string para numerico #

preco = "10.50"
idade = "28"

print(float(preco))

print(int(idade))

# erro de conversão #

# preco = "python" print(float(preco))#

# Traceback (most recent call last):  File "c:\Users\juh_j\DIO - Engenharia de dados\Python\Convertendo_tipos.py",#
# line 49, in <module> print(float(preco))^^^^^^^^^^^^ValueError: could not convert string to float: 'python' # 

print("\n")

print(int(1.9))
print(int("10"))
print(float("10.10"))
print(float(100))

print("\n")

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print("\n")

print(100/2)
print(100 // 2)
