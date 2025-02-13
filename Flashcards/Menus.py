# Módulos dos Menus


def cabecalho():
    print('*' * 40)
    print('*' + '       ' + 'Escolha o que quer fazer' + '       ' + '*')
    print('*' * 40)
    print(' ')


def menu_principal():
    print('\033[7;33m [MENU PRINCIPAL] \033[m')
    print('\n[1] - Jogar Flashcard',
          '\n[2] - Consultar Palavras, Sinônimos e Expressões',
          '\n[3] - Verificar Banco de Palavras')
    print('\n[Digite "sair" para finalizar o programa.]')
    print(' ')


def submenu():
    print('\n[Digite "voltar" para voltar ao menu anterior.]')
    print('[Digite "sair" para finalizar o programa.]')
    print(' ')


def menu_flashcards():
    print('\n\033[7;34m Jogue Flashcards com... \033[m')
    print('\n[1] - Palavra',
          '\n[2] - Expressão',
          '\n[3] - Sinônimo')


def submenu_flashcards_palavras():
    print('\n\033[7;47m Flashcards de Palavras:  \033[m')


def submenu_flashcards_expressoes():
    print('\n\033[7;47m Flashcards de Expressões:  \033[m')


def submenu_flashcards_sinonimos():
    print('\n\033[7;47m Flashcards de Sinônimos:  \033[m')


def menu_consulta():
    print('\n\033[7;34m Busque por significado de... \033[m')
    print('\n[1] - Palavra',
          '\n[2] - Expressão',
          '\n[3] - Sinônimo')


def submenu_consulta_palavras():
    print('\n\033[7;47m Consulta de Palavras:  \033[m')


def submenu_consulta_expressoes():
    print('\n\033[7;47m Consulta de Expressões:  \033[m')


def submenu_consulta_sinonimos():
    print('\n\033[7;47m Consulta de Sinônimos:  \033[m')


def menu_contem_palavra():
    print('\n\033[7;34m Consulte a existência da palavra no Banco de Palavras:  \033[m')

