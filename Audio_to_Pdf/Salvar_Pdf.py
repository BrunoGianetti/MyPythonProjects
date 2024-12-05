from fpdf import FPDF


def salvar_pdf(texto, nome_arquivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for linha in texto.split("\n"):
        pdf.multi_cell(w=190, h=10, txt=linha, border=0)
    pdf.output(nome_arquivo)