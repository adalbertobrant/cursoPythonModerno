def decBin(num):
   if num > 1:
      decBin(num // 2)
   print(num % 2, end='')

num = int(input("Entre o número inteiro decimal"))

decBin(num)





