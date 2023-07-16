import pyautogui
import datetime
import time

hora_minimizacao_ptax_2 = '10:55'
hora_maximizacao_ptax_2 = '11:05'
hora_minimizacao_ptax_3 = '11:55'
hora_maximizacao_ptax_3 = '12:05'
hora_minimizacao_ptax_4 = '12:55'
hora_maximizacao_ptax_4 = '13:05'


def mini_ptax_2():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_minimizacao_ptax_2:
            pyautogui.moveTo(1854, 42)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi MINIMIZADO pelo robô de automação. \n'
                                 '\nAguarde pela MAXIMIZAÇÃO automática.',
                            title='AVISO', button='OK')
            break


def maxi_ptax_2():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_maximizacao_ptax_2:
            pyautogui.moveTo(397, 1025)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(393, 1005)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi restaurado', title='AVISO', button='OK')
            break


def mini_ptax_3():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_minimizacao_ptax_3:
            pyautogui.moveTo(1854, 42)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi MINIMIZADO pelo robô de automação. \n'
                                 '\nAguarde pela MAXIMIZAÇÃO automática.',
                            title='AVISO', button='OK')
            break


def maxi_ptax_3():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_maximizacao_ptax_3:
            pyautogui.moveTo(397, 1025)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(393, 1005)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi restaurado', title='AVISO', button='OK')
            break


def mini_ptax_4():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_minimizacao_ptax_4:
            pyautogui.moveTo(1854, 42)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi MINIMIZADO pelo robô de automação. \n'
                                 '\nAguarde pela MAXIMIZAÇÃO automática.',
                            title='AVISO', button='OK')
            break


def maxi_ptax_4():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_maximizacao_ptax_4:
            pyautogui.moveTo(397, 1025)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(393, 1005)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi restaurado', title='AVISO', button='OK')
            break
