# Ex: frase.len[] # len --> comprimento
# count --> conte ,contagem
# replace --> trocar ,repor
# upper --> pra cima, o que for minusculo ele troca o que já tem ele mantem
# lower --> mantem o que tem em minusco e troca o que é maiusculo pra minusculo
# capitaliza --> joga tudo para minusculo e deixa apenas a 1 em maiusculo
# title --> tranforma todoas as letras em maiusculo de cada palavra , apenas a 1 letra
# strip --> remover espaços que sobra entre uma palvra e outra
# rstrip --> remove os ultimos espaços, apenas estes, todos da direita
# lstrip --> remove todos os espaços da esquerda
# split --> divide os espaços, considerando eles como uma divisão
# join --> ele junta a frase Ex: '-'.join(frase)

frase = 'Curso em Vídeo Python'
print(frase[3:13])
print(frase[3:15:2])
print(frase[::2])
print("""Olá test python orbite""")
print(frase.count('o'))
print(frase.count('P'))
print(len(frase))
print(frase.replace('Curso', 'Orbitex'))
