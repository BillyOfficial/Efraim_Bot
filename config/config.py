"""Configurações do programa."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho da pasta com as DLLs do llama-cpp
DLL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "modelo", "llama_cpp", "lib"))

# Caminho do modelo Mistral (.gguf) – agora dentro da pasta do projeto
MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "modelo", "mistral-7b-instruct-v0.1.Q4_0.gguf")
)

# Número de camadas da GPU (ajuste conforme sua placa de vídeo)
N_GPU_LAYERS = 100

# Velocidade da voz (quanto maior, mais rápido)
VELOCIDADE_VOZ = 170

# Idioma do reconhecimento de fala
IDIOMA = "pt-BR"

# Tempo de espera até começar a falar (em segundos)
TIMEOUT_ESPERA = 10

# Tempo máximo de fala (em segundos)
TEMPO_MAX_FALA = 15
