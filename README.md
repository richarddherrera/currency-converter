# 💱 Conversor de Moedas

Um simples **Conversor de Moedas** desenvolvido em **Python**, que permite converter entre diferentes moedas utilizando dados de câmbio em tempo real.

## 🧩 Funcionalidades
- Interface gráfica moderna feita com **CustomTkinter**
- Busca de taxas de câmbio em tempo real com **Requests**
- Leitura e tratamento de dados em XML usando **xmltodict**
- Lógica de validação para conferir quais moedas podem ser convertidas
- Estrutura organizada em pacotes, facilitando manutenção e expansão

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.12** | Linguagem principal 
- **CustomTkinter** | Criação da interface gráfica moderna 
- **Requests** | Requisições HTTP para buscar dados de câmbio 
- **xmltodict** | Leitura e conversão de arquivos XML 
- **APIAwesome** | Api consumida


---

## 📁 Estrutura do Projeto
```
currency-converter/
├── arquivos_xml/
│   ├── conversoes.xml
│   └── moedas.xml
├── core/
│   ├── pegar_cotacao.py
│   └── pegar_moedas.py
└── ui/
    └── main.py
```

## ⚙️ Instalação
### - Clone este repositório:
   ```bash
   git clone https://github.com/richarddherrera/currency-converter.git
   
   ```
### - Acesse a pasta do projeto:

### - Instalar as dependências (Terminal)
```bash
    pip install customtkinter # Para visualização

    pip install xmltodict # Para receber os dados XML

    pip install requests # Para receber a requisição da cotação
```
## 📸 Prévia da Interface
<p align="center">
  <img src="ui/image.png" alt="Tela principal do app" width="500"/>
</p>



## 👨‍💻 Autor
### Desenvolvido por Richard Herrera

