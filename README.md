# Efraim Bot 🤖

Efraim é um assistente virtual offline com reconhecimento de voz, síntese de fala e integração com um modelo de linguagem natural local (LLM), usando a biblioteca `<span>llama-cpp-python</span>`. Tudo roda no seu computador, sem precisar da internet ou servidores externos!

> O nome "Efraim" foi escolhido por Arthur Ferreira, inspirado na Bíblia. Efraim significa "frutífero" ou "duplamente produtivo", refletindo o desejo de ter um assistente útil, inteligente e confiável.

---

## 🧠 Funcionalidades

* 🎙️ Reconhecimento de voz (speech-to-text)
* 🗣️ Respostas por voz (text-to-speech)
* 🧾 Interação com modelo LLM local (Mistral 7B via GGUF)
* 🔁 Confirmação manual do que foi ouvido - Beta, será retirado após os testes
* 🔒 100% local, sem envio de dados para a nuvem

### Futuras melhorias planejadas:

* 💾 Memória persistente (lembrar informações)
* 📜 Logs de conversa
* ⌨️ Comandos por voz (ex: abrir navegador)
* 🪟 Interface gráfica opcional

---

## 🗂️ Estrutura do Projeto

```
Efraim Bot/
├── comandos/           # (planejado) Comandos especiais por voz
├── config/             # Configurações globais
├── formatacao/         # (planejado) Funções auxiliares de formatação
├── logger/             # (planejado) Armazenamento de logs
├── main.py             # Arquivo principal (executa o assistente)
├── memoria/            # (planejado) Memória do assistente
├── modelo/             # Carregamento do modelo LLM (contém o .gguf)
│   └── mistral-7b-instruct-v0.1.Q4_0.gguf
├── reconhecimento/     # Funções de reconhecimento de voz
├── voz/                # Voz: fala (TTS)
└── README.md
```

---

## 🚀 Como Rodar

1. Instale as dependências:

```
pip install -r requirements.txt
```

2. Execute o script:

```
python main.py
```

---

## ⚙️ Configuração

No arquivo `<span>config/config.py</span>`:

```
DLL_PATH = "modelo/llama_cpp_dlls"  # Caminho para as DLLs da llama-cpp
MODEL_PATH = "modelo/mistral-7b-instruct-v0.1.Q4_0.gguf"
N_GPU_LAYERS = 100
```

---

## 👤 Desenvolvedor

* **Arthur Ferreira (Billy)**
* 💻 GitHub: [BillyOfficial](https://github.com/BillyOfficial)
* 📧 Contato: (21) 97593-119# (Você tem 10 tentativas kkkkkk)

---

## 📝 Licença

⚠️ Ainda será definida.

---

> “Duplamente frutífero”, na vida e nos projetos. Que Efraim te ajude tanto quanto me ajudou a aprender, rir (após quebrar a cabeça para entender) e superar seus desafios. 🙌
>
> Que este projeto reflita a sabedoria, a criatividade e a graça concedida por Deus. Toda honra e glória sejam dadas a Ele, que nos capacita para criar, sonhar e realizar. ✝️✨
