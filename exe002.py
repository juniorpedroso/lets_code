# Módulo 1 - Exercício 02 - Let´s Code Pass

idade = int(input('Digite uma idade entre 0 e 150 anos: '))
if idade < 0 or idade > 150:
    print(f'ERRO! Você digitou {idade} que é uma idade inválida!')
salario = int(input('Digite o valor do salário: '))
if salario < 0:
    print(f'ERRO! Você digitou {salario} que é um valor inválido!')
sexo = input('Digite o sexo (M, F, Outro: ')
if sexo not in ('M', 'F', 'Outro'):
    print('ERRO! Você digitou um sexo inválido!')
