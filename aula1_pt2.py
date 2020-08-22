# continuação da lista de exercícios 
# 11 - Ler velocidade em m/s e apresentar em km / h
vel_ms = float(input("Entre uma velocidade em m/s => "))
print(f"A velocidade em m/s  é {vel_ms * 3.6: .2f} km/h ")
print("")

# 12 - Ler a distância em milhas e transformar em kilometros
dist_milhas = float(input("Entre a distância em milhas => "))
print(f"A distância em kilometros é {1.61 * dist_milhas: .2f} km")
print("")

# 13 - Ler a distância em kilometros e transformar em milhas
dist_km = float(input("Entre a distância em kilometros => "))
print(f"A distância em kilometros é {dist_km / 1.61: .2f} km")
print("")

# 14 - Ler um ângulo em graus e converta em radianos
graus = float(input("Entre o ângulo em graus => "))
pi = 3.14
print(f"O ângulo em radianos é de {graus * pi / 180: .2f} radianos")
print("")

# 15 - Ler em radianos e apresente em graus
radi = float(input("Entre o ângulo em radianos => "))
print(f"O ângulo em graus é de {radi * 180 / pi: .2f}° graus")
print("")

# 16 - Ler comprimento em polegadas e converta em centimetros
pole = float(input("Entre um valor em polegadas => "))
print(f"O valor em centimetros é de {pole * 2.54: .2f} cm")
print("")

# 17 - Ler em centimetros e mostrar em polegadas
cent = float(input("Entre o valor em centimetros => "))
print(f"O valor em polegadas é de {cent / 2.54: .2f} polegadas")
print("")

# 18 - Volume em metros cúbicos para litros
m3 = float(input("Entre o valor em metros cúbicos => "))
print(f"O valor em litros é de {1000 * m3: .2f} l")
print("")

# 19 - Litros para metros cúbicos
ltrs = float(input("Entre o volume em litros => "))
print(f"O valor em metros cúbicos é {ltrs / 1000: .4f} m³")
print("")

# 20 - Massa em kilogramas para libras
massa = float(input("Entre o valor de massa em kilogramas => "))
print(f"O valor da massa em libras é de {massa / 0.45: .2f} lbs")
print("")



