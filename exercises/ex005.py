import os; os.system('clear')

class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        if saldo < 0:
            raise ValueError('O valor do saldo não pode ser menor que zero.')
        self.titular = titular
        self.saldo = saldo
   
    def validar_valor(self, valor: float, operacao: str):
        if valor <= 0:
            return f'O valor de {operacao} deve ser maior que zero.'
        elif operacao == 'saque' and valor > self.saldo:
            return f'Saque não efetuado! Saldo insuficiente.'
        else:
            return None  
    
    def depositar(self, valor):
        mensagem_erro = self.validar_valor(valor, 'depósito')
        if mensagem_erro:
            return mensagem_erro
        else:
            self.saldo += valor
            return f'Depósito efetuado com sucesso no valor de R$ {valor:.2f}\n{self.exibir_saldo()}'
    
    def sacar(self, valor):
        mensagem_erro = self.validar_valor(valor, 'saque')
        if mensagem_erro:
            return mensagem_erro
        else:
            self.saldo -= valor
            return f'Saque efetuado com sucesso no valor de R$ {valor:.2f}\n{self.exibir_saldo()}'
    
    def exibir_saldo(self):
        return f'Seu saldo atual é de R$ {self.saldo:.2f}'
    
    def exibir_titular(self):
        return f'Titular: {self.titular}\n'

    def exibir_cabecalho(self):
        self.limpar_tela()
        return '--------------------------------------------------------------------\nBanco Fura Bolso\nSeu dinheiro é a nossa alegria!\n--------------------------------------------------------------------\n'
    
    def limpar_tela(self):
        return os.system('clear')

    def exibir_mensagem_voltar(self):
        return '\nPressione <ENTER> para voltar.'


while True:
    os.system('clear')
    print('--------------------------------------------------------------------')
    print('Banco Fura Bolso')
    print('Seu dinheiro é a nossa alegria!')
    print('--------------------------------------------------------------------')
    print('Setor de Criação de Contas (SCC)')

    titular = input('\nDigite o nome do titular da conta: ').strip()
    
    if not titular or not titular.replace(" ", "").isalpha():
        print("\nNome inválido! O nome do titular deve conter apenas letras e não pode estar vazio.")
        input('\n\nPressione [ENTER] para tentar novamente.')
        continue

    try:
        saldo = float(input('Adicione um valor para abrir a conta: '))
        if saldo <= 0:
            print("\nO saldo inicial deve ser um número maior que zero.")
            input('\n\nPressione [ENTER] para tentar novamente.')
            continue
    except ValueError:
        print("\nO saldo inicial deve ser um número maior que zero.")
        input('\n\nPressione [ENTER] para tentar novamente.')
        continue

    # Se ambos os inputs forem válidos, sai do loop
    break

# Instanciando objeto
cliente = ContaBancaria(titular, saldo)

print(cliente.exibir_cabecalho())
print('Setor de Criação de Contas (SCC)')
print(f"\nConta criada com sucesso para {cliente.titular}!\nSeu saldo inicial é de R$ {cliente.saldo:.2f}.")
input('\n\nPressione [ENTER] para acessar as funcionalidade da MELHOR agencia bancária!')

opcao = 0
while opcao != 4:
    print(cliente.exibir_cabecalho())
    print(cliente.exibir_titular())
    print('1. Checar saldo')
    print('2. Depositar')
    print('3. Sacar')
    print('4. Sair')   
    try:
        opcao = float(input('\nEscolha uma opção: '))
    except ValueError:
        print('Opção Inválida! Pressione <ENTER> para tentar novamente.')
        continue
    
    if opcao == 1:
        print(cliente.exibir_cabecalho())
        print(cliente.exibir_titular())
        print(cliente.exibir_saldo())
        input(cliente.exibir_mensagem_voltar())
    
    if opcao == 2:
        while True:
            print(cliente.exibir_cabecalho())
            print(cliente.exibir_titular())

            try:
                valor_deposito = float(input('Digite um valor para depósito: '))
                
                comando = ''
                if  valor_deposito <= 0:
                    print('\nOperação não realizada! O valor de depósito deve ser um número maior que zero.') 
                    comando = input('\nPressione [ENTER] para tentar novamente ou digite [-v] para voltar ao menu principal: ')
                    if comando == '-v': break
                    continue
                else:
                    if comando != '-v':
                        print(cliente.limpar_tela())
                        print(cliente.exibir_cabecalho())
                        print(cliente.exibir_titular())
                        print(cliente.depositar(valor_deposito))
                        input(cliente.exibir_mensagem_voltar())
                        break
                    else:
                        break

            except ValueError:
                print('\nOperação não realizada! O valor de depósito deve ser um número maior que zero.')
                comando = input('\nPressione [ENTER] para tentar novamente ou digite [-v] para voltar ao menu principal: ')
                if comando == '-v': break
        

    if opcao == 3:       
        while True:
            print(cliente.exibir_cabecalho())
            print(cliente.exibir_titular())

            try:
                valor_saque = float(input('Digite o valor que deseja sacar: '))

                comando = ''
                if valor_saque <= 0:
                    print('\nOperação não realizada! O valor de saque deve ser um número maior que zero.')
                    comando = input('\nPressione [ENTER] para tentar novamente ou digite [-v] para voltar ao menu principal: ')
                    if comando == '-v': break
                    continue
                else:
                    if comando != '-v':
                        print(cliente.limpar_tela())
                        print(cliente.exibir_cabecalho())
                        print(cliente.exibir_titular())
                        print(cliente.sacar(valor_saque))
                        input(cliente.exibir_mensagem_voltar())
                        break
                    else:
                        break    
            except ValueError:
                print('\nOperação não realizada! O valor de saque deve ser um número maior que zero.')
                comando = input('\nPressione [ENTER] para tentar novamente ou digite [-v] para voltar ao menu principal: ')
                if comando == '-v': break

    if opcao == 4:
        cliente.limpar_tela()
        print(cliente.exibir_cabecalho())
        print(f'Até mais {titular}!... \n\t...Vá trabalhar para trazer mais dinheiro!\n\n')
        break