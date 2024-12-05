import speech_recognition as sr


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