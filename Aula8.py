#Exercicios con condicionais
# 1
numero =  int(input('Digite un numero'))
if numero > 0:
    print("é Positivo.")
elif numero < 0:
    print('é Negativo')
else:
    print("é Zero.")

#2
idade = int(input('Digite sua idade'))
if idade >= 18:
    print('Você pode votar.')
else:
    print('Você não pode votar.')

#3
numero1 =  int(input('Digite un numero'))
if numero1 % 2 == 0:
    print("O número não é par.")
else:
    print("O número impar.")

#4
print('Digite os três lados do triângulo')
a = int(input('Lado 1:'))
b = int(input('Lado 2:'))
c = int(input('Lado 3:'))

if a + b <= c:
    prin('Não forma triângulo')
elif a + c <=b:
    print('Não forma triângulo')
elif b + c <= a:
    print('Não forma triângulo')
else:
    if a == b:
        print('equilatero')
    elif a == c:
        print('isoceles')
    elif b == c:
        print('isoceles')
    else:
        print('escaleno')

#5
numero2 = int(input('digite un numero'))
if numero2 % 5 == 0:
    if numero2 % 7 == 0:
        print('é multiplo de 5 e 7') 
    else:
        print('não e multiplo de 5 e 7')

#6
numero3 = int(input('Digite un numero'))
if numero3 > 10:
    print('e maior que 10')
else:
    print('Não e maoir que 10')

#7
numero4 = int(input('digite un numero'))
if numero4 % 3 == 0:
    print('é divisivel por 3') 
elif numero4 % 5 == 0:
        print('é divisivel por 5') 
else:
        print('Não é divisivel por 3 nen por 5')





    







    
