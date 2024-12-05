from pydub import AudioSegment
import speech_recognition as sr
from fpdf import FPDF


def dividir_audio(arquivo, duracao_segundos):
    audio = AudioSegment.from_file(arquivo)
    duracao = len(audio)  # Duração total em milissegundos
    partes = []
    intervalo = duracao_segundos * 1000  # Converter para milissegundos
    for i in range(0, duracao, intervalo):
        parte = audio[i:i + intervalo]
        partes.append(parte)
    return partes


def transcrever_audio(arquivos):
    recognizer = sr.Recognizer()
    transcricao_completa = ""

    for i, arquivo in enumerate(arquivos):
        print(f"Transcrevendo parte {i + 1}...")
        with sr.AudioFile(arquivo) as source:
            audio_data = recognizer.record(source)
            try:
                texto = recognizer.recognize_google(audio_data, language="it-IT")
                transcricao_completa += texto + "\n"
            except sr.UnknownValueError:
                print(f"Não foi possível entender a parte {i + 1}.")
            except sr.RequestError as e:
                print(f"Erro na API ao transcrever a parte {i + 1}: {e}")

    return transcricao_completa


def salvar_pdf(texto, nome_arquivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for linha in texto.split("\n"):
        pdf.cell(200, 10, txt=linha, ln=True)
    pdf.output(nome_arquivo)


# Dividir o áudio em partes de 60 segundos
partes = dividir_audio("audio.wav", 60)

# Exportar cada parte como um arquivo separado
for i, parte in enumerate(partes):
    parte.export(f"parte_{i + 1}.wav", format="wav")
print(f"Áudio dividido em {len(partes)} partes.")

# Lista de arquivos gerados na divisão
arquivos_partes = [f"parte_{i + 1}.wav" for i in range(len(partes))]

# Transcrever todos os arquivos
texto_completo = transcrever_audio(arquivos_partes)

# Exibir o texto completo no console (ou salve em PDF)
print("Transcrição completa:")
print(texto_completo)

# Salvar a transcrição em um PDF
salvar_pdf(texto_completo, "transcricao_audio.pdf")
print("Transcrição salva em transcricao_audio.pdf")
