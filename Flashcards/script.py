import Flashcard
import Busca
import Banco_De_Palavras
import Menus

Menus.cabecalho()
menu = ''
while menu != 'sair':
   Menus.menu_principal()
   menu = input('Digite a opção desejada: ')
   if menu == "1":
       Menus.menu_flashcards()
       submenu_flashcards = input('\nEscolha a sua opção: ')
       if submenu_flashcards == "1":
           Flashcard.randomizar_palavra()
           Menus.submenu()
           sub_menu = input('Escolha a sua opção: ')
           if sub_menu == 'voltar':
               print(' ')
               continue
           else:
               break
       elif submenu_flashcards == "2":
           Flashcard.randomizar_expressao()
           Menus.submenu()
           sub_menu = input('Escolha a sua opção: ')
           if sub_menu == 'voltar':
               print(' ')
               continue
           else:
               break
       elif submenu_flashcards == "3":
           Flashcard.randomizar_sinonimo()
           Menus.submenu()
           sub_menu = input('Escolha a sua opção: ')
           if sub_menu == 'voltar':
               print(' ')
               continue
           else:
               break

   elif menu == "2":
       Menus.menu_consulta()
       submenu_consulta = input('\nEscolha a sua opção: ')
       if submenu_consulta == "1":
           Busca.Busca_Palavra()
           Menus.submenu()
           sub_menu = input('Escolha a sua opção: ')
           if sub_menu == 'voltar':
               print(' ')
               continue
           else:
               break
       elif submenu_consulta == "2":
               Busca.Busca_Expressao()
               Menus.submenu()
               sub_menu = input('Escolha a sua opção: ')
               if sub_menu == 'voltar':
                   print(' ')
                   continue
               else:
                   break
       elif submenu_consulta == "3":
               Busca.Busca_Sinonimo()
               Menus.submenu()
               sub_menu = input('Escolha a sua opção: ')
               if sub_menu == 'voltar':
                   print(' ')
                   continue
               else:
                   break

   elif menu == "3":
       Menus.menu_contem_palavra()
       while True:
           verifica_palavra = input('\nDigite a palavra a ser verficada: ')
           if verifica_palavra in Banco_De_Palavras.palavras:
               print(f'\nA palavra >>>[{verifica_palavra}]<<< está no dicionário.')
           else:
               print('\nPalavra inexistente no dicionário.')
           continuar = input('\nDeseja pesquisar outra expressão? [s/n]').strip().lower()
           if continuar == 's':
               continue
           else:
               break
       Menus.submenu()
       sub_menu = input('Escolha a sua opção: ')
       if sub_menu == 'voltar':
           print(' ')
           continue
       else:
           break

