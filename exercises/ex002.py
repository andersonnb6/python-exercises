"""
Título: Controle de Estoque
Descrição:
    Um programa interativo para gerenciar o estoque de uma loja ou armazém. 
    Permite adicionar produtos, atualizar suas quantidades, removê-los e listar os itens no estoque.

Objetivo:
    - Praticar estruturas de controle, como loops e condicionais.
    - Trabalhar com dicionários para armazenar dados.
    - Validar entradas do usuário para garantir dados corretos.
    - Desenvolver uma interface de linha de comando para interação com o usuário.

Entrada:
    - Nome do produto (string).
    - Quantidade do produto (número inteiro).

Saída:
    - Mensagens de confirmação para cada operação.
    - Lista de produtos no estoque com suas respectivas quantidades.

Exemplo:
    --- Controle de Estoque ---
    1. Adicionar Produto
    2. Atualizar Quantidade
    3. Remover Produto
    4. Listar Produtos
    5. Sair

    Escolha uma opção: 1

    Digite o nome do produto: Caneta
    Informe a quantidade do produto: 50

    Produto cadastrado com sucesso!

    Escolha uma opção: 4

    ---------| Estoque Atual |---------
    Qtd       Produto
    50        Caneta

Requisitos:
    - Python 3.10 ou superior
"""

# Importando bibliotecas
import os  # Usada para limpar a tela no terminal

# Dicionário para armazenar os produtos e suas respectivas quantidades
estoque = {}

# Variável para armazenar a opção escolhida pelo usuário no menu
opcao = 0

# Loop principal do programa, encerra quando a opção for 5 (Sair)
while opcao != 5:
    try:
        # Exibição do menu principal
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela (compatível com Windows e Unix)
        print('')
        print('--- Controle de Estoque ---\n')
        print('1. Adicionar Produto')
        print('2. Atualizar Quantidade')
        print('3. Remover Produto')
        print('4. Listar Produtos')
        print('5. Sair')
        opcao = int(input('\nEscolha uma opção: '))  # Solicita uma opção do usuário

        # Verifica se a opção está dentro do intervalo válido (1 a 5)
        if 1 <= opcao <= 5:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela antes de cada operação

            # Adicionar um novo produto
            if opcao == 1:
                novo_produto = input('\nDigite o nome do produto: ').lower()  # Recebe o nome do produto (em minúsculo)

                if novo_produto in estoque:
                    print('\nO produto informado já está cadastrado!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')
                else:
                    # Solicita a quantidade do produto enquanto não for um número válido
                    while True:
                        try:
                            qtd_novo_produto = int(input('Informe a quantidade do produto: '))
                            estoque[novo_produto] = qtd_novo_produto  # Adiciona o produto ao estoque
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('\nProduto cadastrado com sucesso!')
                            input('\nPressione <ENTER> para voltar ao menu principal.')
                            break
                        except ValueError:
                            print('\nPor favor, informe um número inteiro!')

            # Atualizar a quantidade de um produto existente
            elif opcao == 2:
                produto = input('\nInforme o produto que deseja atualizar: ').lower()

                while True:
                    if produto in estoque:
                        try:
                            quantidade = int(input('\nInforme a nova quantidade do produto: '))
                            estoque[produto] = quantidade  # Atualiza a quantidade no dicionário
                            print('\nQuantidade atualizada com sucesso!')
                            input('\nPressione <ENTER> para voltar ao menu principal.')
                            break
                        except ValueError:
                            print('\nPor favor, informe um número inteiro!')
                    else:
                        print('\nO produto ainda não foi cadastrado!')
                        input('\nPressione <ENTER> para voltar ao menu principal.')
                        break

            # Remover um produto do estoque
            elif opcao == 3:
                produto = input('\nInforme o produto que deseja remover: ').lower()

                if produto in estoque:
                    estoque.pop(produto)  # Remove o produto do dicionário
                    print('\nProduto removido com sucesso!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')
                else:
                    print('\nProduto não encontrado!\nConsulte a lista de produtos!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')

            # Listar todos os produtos no estoque
            elif opcao == 4:
                print(f"{'Qtd':<10}{'Produto':<10}")  # Cabeçalho da tabela

                for produto, quantidade in estoque.items():
                    print(f'{quantidade:<10}{produto:<10}')  # Exibe cada produto e sua quantidade

                input("\nPressione <ENTER> para voltar ao menu principal.")
        else:
            print('\nOpção Inválida!!')
            input('\nPressione <ENTER> para tentar novamente.')
    except ValueError:  # Captura entradas inválidas no menu principal
        print('\nOpção Inválida!!')
        input('\nPressione <ENTER> para tentar novamente.')