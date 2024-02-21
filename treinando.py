print('................treinamento.....................') 


numero = int(input('DIGITE UM NUMERO INTEIRO: '))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10 
soma = centena + dezena + unidade

print (f'A SOMA DE TUDO E IGUAL A {soma}')