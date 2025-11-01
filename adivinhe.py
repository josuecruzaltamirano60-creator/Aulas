import random

numero = random.randrange(1,10)
escolha = int(input('escolha un numero de 1 à 10'))

if numero == escolha:
    print('Voce ganhou o jogo')
    print('O numero aleatorio é'),(numero)
else:
    print('errour o numero é'),(numero)