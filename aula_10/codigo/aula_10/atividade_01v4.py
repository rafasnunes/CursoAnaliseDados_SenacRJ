# Exercício 01 Versão 4
# Criar uma calculadora que receba dois números e seja capaz de somar, subtrair, multiplicar e dividir
# Versão 4: O usuário entra com 2 números e seleciona qual operação deseja executar.


import random


# Funções do Programa


def calc_soma(n1, n2):
    resultado = n1 + n2
    return resultado


def calc_subt(n1, n2):
    resultado = n1 - n2
    return resultado


def calc_mult(n1, n2):
    resultado = n1 * n2
    return resultado


def calc_div(n1, n2):
    resultado = n1 / n2
    return resultado


# Início do código


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('Digite a operação: ( + ) Soma ( - ) Subtração ( * ) Multiplicação ( / ) Divisão')

calculadora = input('Digite a operação: ')

print(f'Números para o calculo: {num1} e {num2}')

match calculadora:
    case '+':
        soma = calc_soma(num1, num2)
        print(f'Soma de {num1} + {num2} = {soma}')
    case '-':
        subtracao = calc_subt(num1, num2)
        print(f'Subtração: {subtracao}')
    case '*':
        multiplicacao = calc_mult(num1, num2)
        print(f'Multiplicação: {multiplicacao}')
    case '/':
        divisao = calc_div(num1, num2)
        print(f'Divisão: {divisao}')
