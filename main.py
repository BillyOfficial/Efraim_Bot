"""Assistente de voz Efraim, usando a API do Llama e a biblioteca SpeechRecognition."""

from voz.fala import falar
from voz.reconhecimento import ouvir
from modelo.modelo import responder

# Loop principal
def main():
    """
    Função principal que escuta o usuário, confirma o que foi dito
    e responde com base no modelo de linguagem.
    """
    while True:
        entrada = ouvir()
        if entrada:
            print(f"\n🗣️ Você disse: \033[1;36m{entrada}\033[0m\n")
            confirmacao = input("Está certo? (s/n): ").strip().lower()
            if confirmacao not in ('s', 'sim'):
                print("⏭️ Pulando resposta, fale novamente.")
                continue

            resposta = responder(entrada)
            print(f"Efraim: {resposta}")
            falar(resposta)

if __name__ == "__main__":
    main()
