primeiro = input('Digite um valor: ')
segundo = input('Digite outro valor: ')

if primeiro > segundo:
   print (f'{primeiro=} é maior que {segundo=}')
else:
   if primeiro == segundo:
      print (f'{primeiro=} é igual que {segundo=}')
   else:
      print (f'{segundo=} é maior que {primeiro=}')