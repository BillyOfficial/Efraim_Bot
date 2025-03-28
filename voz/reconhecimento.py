"""Módulo para reconhecimento de voz."""

import speech_recognition as sr

def ouvir():
    """Escuta o microfone e tenta reconhecer a fala."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo... (você tem 10 segundos pra começar a falar)")
        r.adjust_for_ambient_noise(source, duration=1.5)  # Calibra o ruído
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("⏰ Ninguém falou a tempo.")
            return None

    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"🗣️ Você disse: \033[1;36m{texto}\033[0m\n")
        confirmar = input("Está correto? (s/n): ").strip().lower()
        if confirmar == 's':
            return texto
        else:
            print("⏪ Vamos tentar de novo...")
            return None
    except sr.UnknownValueError:
        print("❌ Não entendi.")
        return None
    except sr.RequestError:
        print("❌ Erro no serviço de reconhecimento.")
        return None
