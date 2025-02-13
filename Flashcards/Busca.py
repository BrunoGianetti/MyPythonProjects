# Verificações dos dicionários

import Menus
import Banco_De_Palavras


def Busca_Palavra():
    Menus.submenu_consulta_palavras()
    while True:
        palavra_escolhida = input('\nConsulte a palavra: ')
        if palavra_escolhida in Banco_De_Palavras.palavras:
            print(f'\nO significado de >>>[{palavra_escolhida}]<<< é: {Banco_De_Palavras.palavras[palavra_escolhida]}')
            continuar = input('\nDeseja pesquisar outra palavra? [s/n]').strip().lower()
            if continuar == 's':
                continue
            else:
                break
        else:
            print('\nPalavra não existe no Bando de Palavras!')

def Busca_Expressao():
    Menus.submenu_consulta_expressoes()
    while True:
        palavra_escolhida = input('\nConsulte a expressão: ')
        if palavra_escolhida in Banco_De_Palavras.expressoes:
            print(f'\nExpressões com >>>[{palavra_escolhida}]<<< podem ser: {Banco_De_Palavras.expressoes[palavra_escolhida]}')
            continuar = input('\nDeseja pesquisar outra expressão? [s/n]').strip().lower()
            if continuar == 's':
                continue
            else:
                break
        else:
            print('\nExpressão não existe no Bando de Palavras!')

def Busca_Sinonimo():
    Menus.submenu_consulta_sinonimos()
    while True:
        palavra_escolhida = input('\nConsulte o sinônimo: ')
        if palavra_escolhida in Banco_De_Palavras.expressoes:
            print(f'\nSinônimos de >>>[{palavra_escolhida}]<<< podem ser: {Banco_De_Palavras.sinonimos[palavra_escolhida]}')
            continuar = input('\nDeseja pesquisar outra expressão? [s/n]').strip().lower()
            if continuar == 's':
                continue
            else:
                break
        else:
            print('\nSinônimo não existe no Bando de Palavras!')