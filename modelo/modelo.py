"""Módulo que contém a classe do modelo de linguagem GPT-4 e a função de responder perguntas."""

import os
from llama_cpp import Llama
from config.config import DLL_PATH, MODEL_PATH, N_GPU_LAYERS

# Libera a pasta com as DLLs (pra Windows)
os.add_dll_directory(DLL_PATH)

# Carrega o modelo
modelo = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=N_GPU_LAYERS,
    chat_format="chatml"
)

def responder(pergunta: str) -> str:
    """
    Gera uma resposta baseada na pergunta do usuário usando o modelo de linguagem.

    Args:
        pergunta (str): Texto da pergunta feita pelo usuário.

    Returns:
        str: Resposta gerada pelo modelo.
    """
    prompt = (
        "<|system|>\nVocê é um assistente chamado Efraim, "
        "que responde sempre em português do Brasil.\n"
        f"<|user|>\n{pergunta}\n<|assistant|>\n"
    )
    resposta = modelo(prompt, max_tokens=150)
    texto = resposta["choices"][0]["text"].strip()
    return texto
