# Old Style. Utilizamos %s(para sprint), %d(inteiro), %f(numero ponto flutuante)

nome = "Juliana"
idade = 30
profissao = "Analista de dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))


print("\n")

print("\n")

# método format.

nome = "Juliana"
idade = 30
profissao = "Analista de dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}.".format(linguagem, profissao, idade, nome))

print("\n")
print("\n")
