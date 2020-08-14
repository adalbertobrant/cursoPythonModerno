bin = list(input("Entre o número binário:> "))
strl = ""
for x in bin:
    strl += x

valor = 0

for i in range(len(bin)):
    digito = bin.pop()
    if digito == '1':
       valor = valor + pow(2, i)

print(f" Numero decimal de ({strl})2 = ({valor})10")
