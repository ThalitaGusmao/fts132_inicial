import pytest

    # Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_quadrado(base, altura):
    return base * altura

def calcular_area_retangulo(lado1, lado2):
    return lado1 * lado2

def calcular_area_triangulo(base,altura):
    return (base * altura)/2

# Calcular e testar a área de um círculo
# Area = Pi * raio ** 2

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2


if __name__ == '__main__':

    # Garçon - Requisições / Chamadas
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}') # <-- Prato

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3,5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8,2)
    print(f'A divisão é {resultado}')

    # Degustador / Teste
    resultado = elevar_um_numero_pelo_outro(2,3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_quadrado(2,2)
    print(f'A área do quadrado é {resultado}')

    resultado = calcular_area_retangulo(7,6)
    print(f'A área do retangulo é {resultado}')

    resultado = calcular_area_triangulo(3,5)
    print(f'A área do triangulo é {resultado}')

    '''


def testar_somar_dois_numeros():
    # - 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
'''

    ### Oiii