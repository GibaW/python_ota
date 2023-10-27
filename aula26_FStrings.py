"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >53}')
print(f'{variavel: <10}.')
print(f'{variavel:^33}.')
print(f'{-1001.4873648123746:+,.3f}') #.6f define o numero de casas decimais que quer se mostrar no ex sao 3
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')