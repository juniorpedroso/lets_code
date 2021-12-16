# Módulo 1 - Exercício 03 - Let´s Code Pass
pontos = 0
resp = ''
print('===' * 10)
print('Questionário policial.\n' +
      'Respostas apenas S ou N.')

while resp != 'S' and resp != 'N':
    resp = input('Mora perto da vítima?: ').upper()
    if resp == 'S':
        pontos += 1

resp = ''
while resp != 'S' and resp != 'N':
    resp = input('Já trabalhou com a vítima?: ').upper()
    if resp == 'S':
        pontos += 1

resp = ''
while resp != 'S' and resp != 'N':
    resp = input('Telefonou para a vítima?: ').upper()
    if resp == 'S':
        pontos += 1

resp = ''
while resp != 'S' and resp != 'N':
    resp = input('Esteve no local do crime?: ').upper()
    if resp == 'S':
        pontos += 1

resp = ''
while resp != 'S' and resp != 'N':
    resp = input('Devia para a vítima?: ').upper()
    if resp == 'S':
        pontos += 1

if pontos == 5:
    situacao = 'ASSASSINO'
elif 5 > pontos > 2:
    situacao = 'CÚMPLICE'
elif pontos == 2:
    situacao = 'SUSPEITO'
else:
    situacao = 'LIBERADO'

print('Relatório do caso')
print(f'Conforme o questionário onde o suspeito obteve {pontos} pontos.')
print(f'Ele é considerado {situacao}')
