#n = input('Digite algo: ')
#print(type(n), n.isalnum)

#n: str =  (input ('digite algo : '))
#print (type(n),' é um número :' , n.isnumeric() ,
#' é alpha :' , n.isalpha() ,
#' é alphanum :' , n.isalnum() ,
#' é supper :' , n.isupper())

#correto --->
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())















