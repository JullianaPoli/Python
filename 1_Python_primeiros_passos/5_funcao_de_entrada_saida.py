# função input = função builtin input é utilizada quando quremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuario na saida padrão (tela). A função lê a entrada coberte para sring e retorna o valor.#
# Exemplo #
nome = input("Digite seu nome:  ")

print('\n')

# Função print = função print é utilizada quando queremos exibir dados na saida padrão (tela).
# Ela recebe um argumento obrigatorio do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush).
# Todos os objetos são convertidos para string, separados por sep e termoinados por end. A string final é exibida para o usuario.#

nome = "Juliana"
sobrenome = "Poli"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome,sobrenome, sep="#")

print("\n")

nome = input("Informe o seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(nome, idade, end= "...\n")
print (nome, idade, sep=" #")