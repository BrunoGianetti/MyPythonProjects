import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    #nome
    pyautogui.click(1127,263, duration=1)
    pyautogui.write(linha[0].value)
    #produto
    pyautogui.click(1130,302, duration=1)
    pyautogui.write(linha[1].value)orenzo da Mota
    #quantidade
    pyautogui.click(1134,338, duration=1)
    pyautogui.write(str(linha[2].value))
    #categoria
    pyautogui.click(1128,381, duration=1)
    pyautogui.write(linha[3].value)
    #botão
    pyautogui.click(1223,423, duration=1)