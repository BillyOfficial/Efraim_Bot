"""Módulo que fornece a função de reproduzir o texto (falar)."""

import pyttsx3 # pip install pyttsx3

# Inicia o motor de voz
voz = pyttsx3.init()
voz.setProperty("rate", 170)

def falar(texto):
    """Função de reprodução do texto."""
    voz.say(texto)
    voz.runAndWait()
