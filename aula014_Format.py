a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

string = '{nome2} {nome1} {nome2} {nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)
print()
print()

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(idade, nome))