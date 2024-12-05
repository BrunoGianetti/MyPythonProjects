from Dividir_Audio import dividir_audio
from Transcrever_Partes import transcrever_audio
from Salvar_Pdf import salvar_pdf

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