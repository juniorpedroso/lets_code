# Módulo 1 - Exercício 01 - Let´s Code Pass

valor = float(input('Digite um valor: R$'))
desconto = valor * 15 / 100
novoValor = valor - desconto
print(f'O valor de R${valor:.2f} menos 15%, que é \
R${desconto:.2f}, resulta em R${novoValor:.2f}')
