#calculadora/teste_meu_modulo.py
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada, fatorial, potencia
from calculadora import logaritmo, exponencial

a = 4
b = 2

print("=" * 40)
print(f"{'Resultados das Operações':^40}")
print("=" * 40)

print(f"{'Operação':<20}{'Resultado':>20}")
print("-" * 40)
print(f"{'Soma':<20}{somar(a, b):>20.2f}")
print(f"{'Subtração':<20}{subtrair(a, b):>20.2f}")
print(f"{'Multiplicação':<20}{multiplicar(a, b):>20.2f}")
print(f"{'Divisão':<20}{dividir(a, b):>20.2f}")
print(f"{'Raiz Quadrada':<20}{raiz_quadrada(25):>20.2f}")
print(f"{'Fatorial':<20}{fatorial(a):>20.2f}")
print(f"{'Potência':<20}{potencia(a, b):>20.2f}")
print(f"{'Logaritmo':<20}{logaritmo(10, 100):>20.2f}")
print(f"{'Exponencial':<20}{exponencial(1):>20.2f}")
print("=" * 40)

