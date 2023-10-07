from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import openpyxl


numero_oab = 47856

driver = webdriver.Chrome()
driver.get("https://esaj.tjsp.jus.br/cpopg/open.do")
sleep(1)

dropdown_oab = driver.find_element(By.XPATH, '//*[@id="cbPesquisa"]')
opcoes_consulta = Select(dropdown_oab)
opcoes_consulta.select_by_visible_text('OAB')
sleep(1)

campo_oab = driver.find_element(By.XPATH, '//*[@id="campo_NUMOAB"]')
campo_oab.send_keys(numero_oab)
sleep(1)

botao_consultar = driver.find_element(By.XPATH, '//*[@id="botaoConsultarProcessos"]')
botao_consultar.click()
sleep(3)

links_extraidos = []
processos = driver.find_elements(By.CLASS_NAME, 'linkProcesso')

for i in range(0, len(processos)):
    link = processos[i].get_attribute('href')
    links_extraidos.append(link)

lista_numero_processo = []
lista_valor_acao = []
lista_foro = []
lista_assunto = []
lista_situacao = []
lista_area = []
lista_vara = []
lista_juiz = []
lista_movimentacoes = []

for url_processo in links_extraidos:

    driver.get(url_processo)
    sleep(3)
    driver.find_element(By.CLASS_NAME, 'unj-link-collapse').click()

    try:
        numero_processo = driver.find_element(By.ID, 'numeroProcesso')
        numero_processo = numero_processo.text
        lista_numero_processo.append(numero_processo)
    except Exception as error:
        numero_processo = 'Não Informado'
        lista_numero_processo.append(numero_processo)
        pass

    try:
        valor_acao = driver.find_element(By.ID, 'valorAcaoProcesso')
        valor_acao = valor_acao.text
        lista_valor_acao.append(valor_acao)
    except Exception as error:
        valor_acao = 'Não Informado'
        lista_valor_acao.append(valor_acao)
        pass

    try:
        foro = driver.find_element(By.ID, 'foroProcesso')
        foro = foro.text
        lista_foro.append(foro)
    except Exception as error:
        foro = 'Não Informado'
        lista_foro.append(foro)
        pass

    try:
        assunto = driver.find_element(By.ID, 'assuntoProcesso')
        assunto = assunto.text
        lista_assunto.append(assunto)
    except Exception as error:
        assunto = 'Não Informado'
        lista_assunto.append(assunto)
        pass

    try:
        situacao = driver.find_element(By.ID, 'labelSituacaoProcesso')
        situacao = situacao.text
        lista_situacao.append(situacao)
    except Exception as error:
        situacao = 'Não Informado'
        lista_situacao.append(situacao)
        pass

    try:
        area = driver.find_element(By.ID, 'areaProcesso')
        area = area.text
        lista_area.append(area)
    except Exception as error:
        area = 'Não Informado'
        lista_area.append(area)
        pass

    try:
        area = driver.find_element(By.ID, 'areaProcesso')
        area = area.text
        lista_area.append(area)
    except Exception as error:
        area = 'Não Informado'
        lista_area.append(area)
        pass

    try:
        vara = driver.find_element(By.ID, 'varaProcesso')
        vara = vara.text
        lista_vara.append(vara)
    except Exception as error:
        vara = 'Não Informado'
        lista_vara.append(vara)
        pass

    try:
        juiz = driver.find_element(By.ID, 'juizProcesso')
        juiz = juiz.text
        lista_juiz.append(juiz)
    except Exception as error:
        juiz = 'Não Informado'
        lista_juiz.append(juiz)
        pass

    movimentacoes = driver.find_elements(By.ID, 'tabelaUltimasMovimentacoes')

    for data in movimentacoes:
        datas = data.find_element(By.CLASS_NAME, 'dataMovimentacao')
        datas = datas.text
        lista_movimentacoes.append(datas)

    botao_voltar = driver.find_element(By.ID, 'setaVoltar')
    botao_voltar.click()
sleep(3)

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Dados"

sheet["A1"] = "Número do Processo"
sheet["B1"] = "Valor da Ação"
sheet["C1"] = "Foro"
sheet["D1"] = "Assunto"
sheet["E1"] = "Situação"
sheet["F1"] = "Área"
sheet["G1"] = "Vara"
sheet["H1"] = "Juiz"
sheet["I1"] = "Movimentações"

for i in range(len(lista_numero_processo)):
    row = i + 2
    sheet[f"A{row}"] = lista_numero_processo[i]
    sheet[f"B{row}"] = lista_valor_acao[i]
    sheet[f"C{row}"] = lista_foro[i]
    sheet[f"D{row}"] = lista_assunto[i]
    sheet[f"E{row}"] = lista_situacao[i]
    sheet[f"F{row}"] = lista_area[i]
    sheet[f"G{row}"] = lista_vara[i]
    sheet[f"H{row}"] = lista_juiz[i]
    sheet[f"I{row}"] = lista_movimentacoes[i]

workbook.save("Dados.xlsx")

driver.quit()
