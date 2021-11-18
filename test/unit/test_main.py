import pytest

from main import*



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

def testar_subtrair_dois_numeros():
    num1 = 6
    num2 = 3
    resultado_esperado = 3
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():
    num1 = 5
    num2 = 4
    resultado_esperado = 20
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():
    num1 = 15
    num2 = 3
    resultado_esperado = 5
    resultado_atual = dividir_dois_numeros(num1,num2)
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    num1 = 7
    num2 = 4
    resultado_esperado = 2401
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_quadrado():
    num1 = 2
    num2 = 10
    resultado_esperado = 20
    resultado_atual = calcular_area_quadrado(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_retangulo():
    num1 = 9
    num2 = 7
    resultado_esperado = 63
    resultado_atual = calcular_area_retangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_triangulo():
    num1 = 12
    num2 = 4
    resultado_esperado = 24
    resultado_atual = calcular_area_triangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    raio = 1
    resultado_esperado = 3.14
    resultado_atual = calcular_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado