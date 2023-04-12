from random import randint
from typing import List

MAX_EIXO_X = 15
MAX_EIXO_Y = 15
QUANTIDADE_BOMBAS = 20


def iniciar_tabuleiro():
    return [[''] * MAX_EIXO_X for _ in range(MAX_EIXO_Y)]


def preencher_bombas_no_tabuleiro(quantidade_bombas, tabuleiro):
    while sum(linha.count('B') for linha in tabuleiro) < quantidade_bombas:
        posicao_x = randint(0, MAX_EIXO_X - 1)
        posicao_y = randint(0, MAX_EIXO_Y - 1)
        tabuleiro[posicao_x][posicao_y] = 'B' if tabuleiro[posicao_x][posicao_y] == '' else ''
    return tabuleiro


tabuleiro = iniciar_tabuleiro()
tabuleiro = preencher_bombas_no_tabuleiro(QUANTIDADE_BOMBAS, tabuleiro)
print(tabuleiro)
