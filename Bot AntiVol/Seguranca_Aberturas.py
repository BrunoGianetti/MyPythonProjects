import pyautogui
import datetime
import time

hora_minimizacao_br = '09:55'
hora_maximizacao_br = '10:05'
hora_minimizacao_us = '10:25'
hora_maximizacao_us = '10:35'


def mini_br():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_minimizacao_br:
            pyautogui.moveTo(1854, 42)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi MINIMIZADO pelo robô de automação. \n'
                                 '\nAguarde pela MAXIMIZAÇÃO automática.',
                            title='AVISO', button='OK')
            break


def maxi_br():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_maximizacao_br:
            pyautogui.moveTo(397, 1025)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(393, 1005)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi restaurado', title='AVISO', button='OK')
            break


def mini_us():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_minimizacao_us:
            pyautogui.moveTo(1854, 42)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi MINIMIZADO pelo robô de automação. \n'
                                 '\nAguarde pela MAXIMIZAÇÃO automática.',
                            title='AVISO', button='OK')
            break


def maxi_us():
    while True:
        hora_sistema = datetime.datetime.now().strftime('%H:%M')
        if hora_sistema == hora_maximizacao_us:
            pyautogui.moveTo(397, 1025)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(393, 1005)
            pyautogui.click()
            time.sleep(2)
            pyautogui.alert(text='O Superdom foi restaurado',
                            title='AVISO', button='OK')
            break
