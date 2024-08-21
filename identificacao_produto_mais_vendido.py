def produto_mais_vendido(produtos):
    # Dicionário para armazenar a contagem de cada produto
    contagem = {}
    
    # Contabiliza a frequência de cada produto
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    # Variáveis para armazenar o produto mais vendido e sua contagem
    max_produto = None
    max_count = 0
    
    # Itera sobre o dicionário de contagem para encontrar o produto com maior frequência
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("")
    # Converte a entrada em uma lista de strings, removendo espaços extras ao redor de cada string
    produtos = [produto.strip() for produto in entrada.split(',')]
    
    return produtos

# Obtém a lista de produtos vendidos
produtos = obter_entrada_produtos()
# Exibe o produto mais vendido
print(produto_mais_vendido(produtos))
