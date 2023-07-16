# Coordenadas X e Y (1854, 42) para Minimização
# Coordenadas X e Y (397, 1025) para Maximização 1
# Coordenadas X e Y (393, 1005) para Maximização 2

import Seguranca_Aberturas
import Seguranca_Ptax

print(' ')
print(' ')
print(' ','X'*66)
print(' ')
print('     O robô de segurança operacional está ativo. Minimize a tela.')
print('     Você está protegido da volatilidade das Aberturas e da Ptax.')
print('       >>> Sistema criado pelo trader/dev Bruno Gianetti <<<')
print('            https://www.linkedin.com/in/brunogianetti/')
print('                 https://github.com/BrunoGianetti')
print(' ')
print(' ','X'*66)

while True:
    Seguranca_Aberturas.mini_br()
    Seguranca_Aberturas.maxi_br()
    Seguranca_Aberturas.mini_us()
    Seguranca_Aberturas.maxi_us()
    Seguranca_Ptax.mini_ptax_2()
    Seguranca_Ptax.maxi_ptax_2()
    Seguranca_Ptax.mini_ptax_3()
    Seguranca_Ptax.maxi_ptax_3()
    Seguranca_Ptax.mini_ptax_4()
    Seguranca_Ptax.maxi_ptax_4()


