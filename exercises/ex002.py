# importando bibliotecas
import os

# dicionario para armazenar produtos e quantidades
estoque = {}

# variavel para armazenas opcoes do usuario 
opcao = 0

while opcao != 5:
    try:
        # menu do programa
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('--- Controle de Estoque ---\n')
        print('1. Adicionar Produto')
        print('2. Atualizar Quantidade')
        print('3. Remover Produto')
        print('4. Listar Produtos')
        print('5. Sair')
        opcao = int(input('\nEscolha uma opção: '))

        if 1 <= opcao <= 5:
            os.system('cls' if os.name == 'nt' else 'clear')

            if opcao == 1:
                novo_produto = input('\nDigite o nome do produto: ').lower()

                if novo_produto in estoque:
                    print('\nO produto informado já está cadastrado!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')          
                else:
                    while True:
                        try:
                            qtd_novo_produto = int(input('Informe a quantidade do produto: '))
                            estoque[novo_produto] = qtd_novo_produto
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('\nProduto cadastrado com sucesso!')
                            input('\nPressione <ENTER> para voltar ao menu principal.')
                            break
                        except ValueError:
                            print('\nPor favor, informe um número inteiro!')

            elif opcao == 2:
                produto = input('\nInforme o produto que deseja atualizar: ').lower()
                
                while True: 
                    if produto in estoque:
                        try:
                            quantidade = int(input('\nInforme a quantidade do produto: '))
                            estoque[produto] = quantidade
                            print('\nQuantidade atualizada com sucesso!')
                            input('\nPressione <ENTER> para voltar ao menu principal.')
                            break
                        except ValueError:
                            print('\nPor favor, informe um número inteiro!')
                    else:
                            print('\nO produto ainda não foi cadastrado!')
                            input('\nPressione <ENTER> para voltar ao menu principal.')
                            break

            elif opcao == 3:
                produto = input('\nInforme o produto que deseja remover: ').lower()

                if produto in estoque:
                    estoque.pop(produto)
                    print('\nProduto removido com sucesso!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')
                else:
                    print('\nProduto não encontrado!\nConsulte a lista de produtos!')
                    input('\nPressione <ENTER> para voltar ao menu principal.')       
                
            elif opcao == 4:
                print(f"{'Qtd':<10}{'Produto':<10}")

                for produto, quantidade in estoque.items():
                    print(f'{quantidade:<10}{produto:<10}')
                
                input("\nPressione <ENTER> para voltar ao menu principal.")
        else:
            print('\nOpção Inválida!!')
            input('\nPressione <ENTER> para tentar novamente.')
    except ValueError:
        print('\nOpção Inválida!!')
        input('\nPressione <ENTER> para tentar novamente.')



    