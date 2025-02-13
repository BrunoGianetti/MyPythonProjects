# Randomização dos dicionários
import Banco_De_Palavras
import Menus
import random


def randomizar_palavra():
    Menus.submenu_flashcards_palavras()
    while True:
        chave_escolhida = random.choice(list(Banco_De_Palavras.palavras.keys()))
        print(f'\nA palavra escolhida aleatoriamente foi >>>[{chave_escolhida}]<<<.')
        resposta = input('\nDeseja ver o significado da palavra? [s/n]: ').strip().lower()
        if resposta == 's':
            print(f'\n>>>[Resposta]<<<: {Banco_De_Palavras.palavras[chave_escolhida]}')
        elif resposta == 'n':
            continuar = input('\nDeseja continuar jogando Flashcards? [s/n]: ').strip().lower()
            if continuar == 's':
                continue
            else:
                break


def randomizar_expressao():
    Menus.submenu_flashcards_expressoes()
    while True:
        chave_escolhida = random.choice(list(Banco_De_Palavras.expressoes.keys()))
        print(f'\nA palavra escolhida aleatoriamente foi >>>[{chave_escolhida}]<<<.')
        resposta = input('\nDeseja ver o significado da palavra? [s/n]: ').strip().lower()
        if resposta == 's':
            print(f'\n>>>[Resposta]<<<: {Banco_De_Palavras.expressoes[chave_escolhida]}')
        elif resposta == 'n':
            continuar = input('\nDeseja continuar jogando Flashcards? [s/n]: ').strip().lower()
            if continuar == 's':
                continue
            else:
                break


def randomizar_sinonimo():
    Menus.submenu_flashcards_sinonimos()
    while True:
        chave_escolhida = random.choice(list(Banco_De_Palavras.sinonimos.keys()))
        print(f'\nA palavra escolhida aleatoriamente foi >>>[{chave_escolhida}]<<<.')
        resposta = input('\nDeseja ver o significado da palavra? [s/n]: ').strip().lower()
        if resposta == 's':
            print(f'\n>>>[Resposta]<<<: {Banco_De_Palavras.sinonimos[chave_escolhida]}')
        elif resposta == 'n':
            continuar = input('\nDeseja continuar jogando Flashcards? [s/n]: ').strip().lower()
            if continuar == 's':
                continue
            else:
                break

