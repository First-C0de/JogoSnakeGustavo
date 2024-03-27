import pygame
from pygame.locals import *
import random

pygame.init()

# TELA
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo da Cobrinha')

ESQUERDA = K_LEFT
DIREITA = K_RIGHT
CIMA = K_UP
BAIXO = K_DOWN

# Passo
passo = 10

# COBRINHA
cobrinha_pos = [(300, 300)]
cobrinha_sup = pygame.Surface((10, 10))
cobrinha_sup.fill((255, 255, 255))
cobrinha_dir = ESQUERDA


# Função maçã
def gerar_posicao_aleatoria():
    x = random.randint(0, tamanho_tela[0] - passo) // passo * passo
    y = random.randint(0, tamanho_tela[1] - passo) // passo * passo
    return x, y

# Maçã
maca_pos = gerar_posicao_aleatoria()
maca_sup = pygame.Surface((10, 10))
maca_sup.fill((255, 0, 0))




while True:

    # Limitar a velocidade
    pygame.time.Clock().tick(10)

    # LIMPAR O DISPLAY
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        # Verificar o botão clicado para movimentar
        if event.type == KEYDOWN:
            if event.key in [ESQUERDA, DIREITA, CIMA, BAIXO]:
                cobrinha_dir = event.key

    # Criar a direção da cobrinha
    if cobrinha_dir == DIREITA:
        nova_posicao = (cobrinha_pos[0][0] + passo, cobrinha_pos[0][1])
    elif cobrinha_dir == ESQUERDA:
        nova_posicao = (cobrinha_pos[0][0] - passo, cobrinha_pos[0][1])
    elif cobrinha_dir == CIMA:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] - passo)
    elif cobrinha_dir == BAIXO:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] + passo)


    cobrinha_pos.insert(0, nova_posicao)
 
    # Desenha a cobrinha
    for posicao in cobrinha_pos:
        tela.blit(cobrinha_sup, posicao)
    
    cobrinha_pos.pop()

    tela.blit(maca_sup, maca_pos)

    pygame.display.update()
