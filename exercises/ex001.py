"""
Título: Analisador de Notas
Descrição: 
    Um programa que coleta notas de uma turma de alunos, calcula métricas como maior nota, menor nota, média, 
    e a quantidade de alunos com notas acima da média.

Objetivo:
    - Praticar estruturas de controle, como loops e condicionais.
    - Trabalhar com listas e cálculos matemáticos básicos.
    - Validar entradas do usuário para garantir dados corretos.

Entrada:
    - Número de alunos.
    - Notas dos alunos (valores entre 0 e 10, aceitando casas decimais).

Saída:
    - Maior nota.
    - Menor nota.
    - Média da turma.
    - Quantidade de alunos acima da média.

Exemplo:
    Quantos alunos há na turma? 3
    Digite a nota do aluno 1: 8.5
    Digite a nota do aluno 2: 7.0
    Digite a nota do aluno 3: 9.5

    ---------| Resultados |---------

    Notas inseridas: [8.5, 7.0, 9.5]
    Maior nota: 9.50
    Menor nota: 7.00
    Média da turma: 8.33
    Alunos acima da média: 2

    Requisitos:
    - Python 3.10 ou superior
"""

print('\n---------> Analisador de notas\n')


# coletando o numero de alunos da turma
while True:
    try:
        total_alunos = int(input('Quantos alunos há na turma? '))
        break
    except ValueError:
        print("Valor Inválido!")

# loop para cadastrar notas
notas = []
for i in range(1,total_alunos+1):
    while True:
        try:
            nota = float(input(f'Digite a nota do aluno {i}: '))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print('\nPor favor, insira uma nota válida entre 0 e 10.\n')
        except ValueError:
            print('\nPor favor, insira uma nota válida entre 0 e 10.\n')

# calculando metricas
maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas)/len(notas)
alunos_acima_da_media = 0

# selecionando notas acima da média
notas_acima_da_media = []
for nota in notas:
    if nota > media:
       alunos_acima_da_media += 1

# Mostrando resultados
print('\n---------> Resultados\n')
print(f"Notas inseridas: {notas}")
print(f'Maior nota: {maior_nota:.2f}')
print(f'Menor nota: {menor_nota:.2f}')
print(f'Média da turma: {media:.2f}')
print(f'Alunos acima da média: {alunos_acima_da_media}')
print('')

