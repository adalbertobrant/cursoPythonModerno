# 1- fazer programa que leia numero e imprima na tela
try:
	numero = int(input("Entre um número => "))
	print(f"Numero impresso  = ",numero)
	print("")
except ValueError:
	print("Não é válido, programa encerrado")

# 2 - fazer um programa que entre um número real e o imprima na tela

try:
	numero_real = float((input("Entre um número real => ")))
	print(f"Número real impresso = ", numero_real)
	print("")
except ValueError:
	print("Não é válido, programa encerrado")

# 3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles

try:
	valor_1 = int(input("Entre o valor 1° => "))
	valor_2 = int(input("Entre o valor 2° => "))
	valor_3 = int(input("Entre o valor 3° => "))
	print(f"A soma do {valor_1} + {valor_2} + {valor_3} é igual a {valor_1+valor_2+valor_3} ")
except ValueError:
	print("Erro")

# 4- Leia um número real e imprima o resultado do quadrado desse número

try:
	nr = float(input("Entre um número real => "))
	print(f"O quadrado de {nr} é {nr*nr}")
	print("")
except ValueError:
	print("Erro")

#5 - Leia um número real e imprima a quinta parte deste número.

try:
	numb_real = float(input("Entre um número real => "))
	print(f"A quinta parte de {numb_real} é ({numb_real}/5) => {numb_real/5} aproximadamente")
	print("")
except ValueError:
	print("Erro")

# 6- Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.

try: 
	temp_cel = float(input("Entre a temperatura em graus Celsius => "))
	print(f"A temperatura em Fahrenheit é {temp_cel * (9.0/5.0) +32.0 :.2f}° F")
	print("")
except ValueError:
	print("Erro")

# 7 - Leia a temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.

try: 
	temp_Fah = float(input("Entre a temperatura em graus Fahrenheit => "))
	print(f"A temperatura em Celsius é {5.0 * (temp_Fah - 32.0) / 9.0 : .2f}° C")
	print("")
except ValueError:
	print("Erro")

#8 - Leia uma temperatura em graus Kelvin e apresente em graus Celsius
try:
	temp_k = float(input("Entre uma temperatura em graus Kelvin => "))
	print(f"A temperatura em graus Celsius é {temp_k - 273.15 : .2f} °C ")
	print("")
except ValueError:
	print("Erro")

#9 - Leia a temperatura em Celsius e mostra a temperatura em Kelvin
try:
	temp_C = float(input("Entre uma temperatura em graus Celsius => "))
	print(f"A temperatura em graus kelvin é {temp_C + 273.15 : .2f} K ")
	print("")
except ValueError:
	print("Erro")

#10 - Ler velocidade em km/h e transformar para m/s 
try:
	vel_km = float(input("Entre uma velocidade em km/h => "))
	print(f"A velocidade em m/s  é {vel_km/3.6: .2f} m/s ")
	print("")
except ValueError:
	print("Erro")