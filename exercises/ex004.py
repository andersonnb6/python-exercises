"""
Título: Sistema de Controle de Animais
Descrição:
    Um programa para gerenciar informações básicas sobre animais, utilizando orientação a objetos. 
    Permite criar instâncias de diferentes tipos de animais, exibir suas informações e emitir sons característicos.

Objetivo:
    - Praticar conceitos básicos de orientação a objetos, como herança e sobrescrita de métodos.
    - Trabalhar com classes, métodos e atributos.
    - Demonstrar como criar e utilizar classes base e subclasses em Python.

Entrada:
    - Nome do animal (string).
    - Espécie do animal (string).
    - Idade do animal (número inteiro).

Saída:
    - Descrição completa do animal (nome, espécie e idade).
    - Som característico do animal.

Exemplo:
    --- Sistema de Controle de Animais ---

    Criando um cachorro...
    Nome: Tico | Espécie: Canis lupus familiaris | Idade: 14
    Som: Au au

    Criando um gato...
    Nome: Montinho | Espécie: Felis catus | Idade: 2
    Som: Miau miau

Requisitos:
    - Python 3.10 ou superior
    - Conhecimento básico de classes e herança em Python
"""

class Animal():
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
  
    def descreve_animal(self):
        return f'Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade}'
    
    def emitir_som(self):
        return 'O animal emite um som genérico.'

class Cachorro(Animal):   
    def emitir_som(self):
        return 'Au au'

class Gato(Animal):   
    def emitir_som(self):
        return 'Miau miau'
    
animal_cachorro = Cachorro('Tico', 'Canis lupus familiaris', 14)
print(animal_cachorro.descreve_animal())
print(animal_cachorro.emitir_som())

print('')

animal_gato = Gato('Montinho', 'Felis catus', 2)
print(animal_gato.descreve_animal())
print(animal_gato.emitir_som())
