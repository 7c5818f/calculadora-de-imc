"""
Cod. atividade....: 3677447
Disciplina........: Linguagem de Programação
Autor.............: Isaak Gomes
Data..............: 14/08/2023
"""

import sys

print('+--------------------------------+')
print('|   Script para cálculo de IMC   |')
print('+--------------------------------+')
print('|          Faixa Etária          |')
print('| [1] Criança do sex. masculino  |')
print('| [2] Criança do sex. feminino   |')
print('| [3] Adulto (idade <= 60)       |')
print('| [4] Idoso (idade > 60)         |')
print('+--------------------------------+')

try:
    faixa = int(input('Digite uma faixa etária (1 a 4) >'))
except ValueError:
    print('Valor inválido para faixa etária!')
    sys.exit()
if faixa < 1 or faixa > 4:
    print('Valor inválido para faixa etária!')
    sys.exit()

if faixa == 1 or faixa == 2:
    imc_meninos = {
        6: (14.5, 16.6, 18), 7: (15, 17.3, 19.1), 8: (15.6, 16.7, 20.3),
        9: (16.1, 18.8, 21.4), 10: (16.7, 19.6, 22.5), 11: (17.2, 20.3, 23.7),
        12: (17.8, 21.1, 24.8), 13: (18.5, 21.9, 25.9), 14: (19.2, 22.7, 26.9),
        15: (19.9, 23.6, 27.7)
    }
    imc_meninas = {
        6: (14.3, 16.1, 17.4), 7: (14.9, 17.1, 18.9), 8: (15.6, 18.1, 20.3),
        9: (16.3, 19.1, 21.7), 10: (17, 20.1, 23.2), 11: (17.6, 21.1, 24.5),
        12: (18.3, 22.1, 25.9), 13: (18.9, 23, 27.7), 14: (19.3, 23.8, 27.9),
        15: (19.6, 24.2, 28.8)
    }
    try:
        idade = int(input('Digite a idade (de 6 a 15 anos) >'))
    except ValueError:
        print('Valor inválido para idade!')
        sys.exit()
    if idade < 6 or idade > 15:
        print('Valor inválido para idade!')
        sys.exit()

peso = input('Digite o peso em kg > ')
altura = input('Digite a altura em metros > ')

if ',' in peso:
    peso = peso.replace(',', '.')
if ',' in altura:
    altura = altura.replace(',', '.')
try:
    peso = float(peso)
    altura = float(altura)
except ValueError:
    print('ERRO: Valor inválido para peso ou altura!')
    sys.exit()

try:
    imc = peso / (altura * altura)
except ZeroDivisionError:
    print('ERRO: Divisão por zero! O valor fornecido em altura é inválido!')
    sys.exit()
if faixa == 1:
    if imc < imc_meninos[idade][0]:
        categoria = 'abaixo do peso'
    elif imc >= imc_meninos[idade][0] and imc < imc_meninos[idade][1]:
        categoria = 'peso normal'
    elif imc >= imc_meninos[idade][1] and imc < imc_meninos[idade][2]:
        categoria = 'sobrepeso'
    else:
        categoria = 'obesidade'
elif faixa == 2:
    if imc < imc_meninas[idade][0]:
        categoria = 'abaixo do peso'
    elif imc >= imc_meninas[idade][0] and imc < imc_meninas[idade][1]:
        categoria = 'peso normal'
    elif imc >= imc_meninas[idade][1] and imc < imc_meninas[idade][2]:
        categoria = 'sobrepeso'
    else:
        categoria = 'obesidade'
elif faixa == 3:
    if imc < 18.5:
        categoria = 'abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        categoria = 'peso normal'
    elif imc >= 25 and imc < 30:
        categoria = 'sobrepeso'
    elif imc >= 30 and imc < 35:
        categoria = 'obesidade grau 1'
    elif imc >= 35 and imc < 40:
        categoria = 'obesidade grau 2 (severa)'
    else:
        categoria = 'obesidade grau 3 (mórbida)'
else:
    if imc < 22:
        categoria = 'abaixo do peso'
    elif imc >= 22 and imc < 27:
        categoria = 'peso normal'
    elif imc >= 27 and imc < 30:
        categoria = 'sobrepeso'
    elif imc >= 30 and imc < 35:
        categoria = 'obesidade grau 1'
    elif imc >= 35 and imc < 40:
        categoria = 'obesidade grau 2 (severa)'
    else:
        categoria = 'Obesidade grau 3 (mórbita)'

imc = f'{imc:.1f}'
imc = imc.replace('.', ',')

print(f'\nO IMC é de {imc}. A categoria é {categoria}.')