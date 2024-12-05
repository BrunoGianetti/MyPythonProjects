from pydub import AudioSegment


def dividir_audio(arquivo, duracao_segundos):
    audio = AudioSegment.from_file(arquivo)
    duracao = len(audio)  # Duração total em milissegundos
    partes = []
    intervalo = duracao_segundos * 1000  # Converter para milissegundos
    for i in range(0, duracao, intervalo):
        parte = audio[i:i + intervalo]
        partes.append(parte)
    return partes
