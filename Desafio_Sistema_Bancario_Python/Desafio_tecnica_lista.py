def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        produto = produto.strip()  # Remove espaços em branco
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # Encontre o produto com a maior contagem:
    for produto, count in contagem.items():
        # Compare a contagem atual com a contagem máxima armazenada em max_count:
        if count > max_count:  # Se a contagem atual for maior que max_count
            max_count = count  # Atualize max_count
            max_produto = produto  # Defina max_produto como o produto atual
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converta a entrada em uma lista de strings, removendo espaços extras:
    return entrada.split(',')

# Obtém a lista de produtos
produtos = obter_entrada_produtos()
# Imprime o produto mais vendido
print(produto_mais_vendido(produtos))
