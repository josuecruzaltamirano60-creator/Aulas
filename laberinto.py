# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# 2 variáveis para definir a altura e a largura da tela 
largura, altura = 400, 400

# 1 variável que atribuida a ela a função que cria a tela 
tela = pygame.display.set_mode((largura, altura))

# Chamada do módulo acompanhado da função que add um título a tela  
pygame.display.set_caption("Labirinto")

# 3  variáveis que atribui a elas o rgb da cores  
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# 1  variável que atrbui a ela o largura/ altura da celula 

tamanho_celula = 40

# lista bidimensional que esta definindo o tabuleiro 

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 2 variáveis posicionandi as celulas 
x, y = 1 * tamanho_celula, 1 * tamanho_celula


# 1  variável que defini a velocidade da celula
velocidade = 40


# criação de uma função, para criar o labirinto 

def desenhar_labirinto():
    # acessando a primeira dimensão da lista, [0-9]
    for linha in range(len(labirinto)):
        # caessando a segunda dimensão da lista trazendo os indices
        # atribuidos a variavel coluna 