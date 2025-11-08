# Janela -> 500x500
# Título -> "Conversor de Moedas"
# Campos de selecionar moedas de origem e destino (Campo de lista), com labels "Selecione a moeda de origem!"
# Botão de para converter as moedas, "Converter"
# Lista de exibição com nome das moedas

import customtkinter

# Fontes
font_title = ("Poppins", 20, "bold")
font_label = ("Inter", 14)
font_button = ("Inter", 14, "bold")

# Criação e configuração da janela
customtkinter.set_appearance_mode("dark") # Setar tema do customtkinter
customtkinter.set_default_color_theme("green") # Setar tema de cores dos elementos

janela = customtkinter.CTk()
janela.geometry("500x500")

# Criação dos botões, textos e os demais elementos
titulo = customtkinter.CTkLabel(janela, text="💰 Conversor de Moedas 💰", font=font_title)
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Seleciona a moeda de origem", font=font_label)
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])

texto_moeda_destino = customtkinter.CTkLabel(janela, text="Seleciona a moeda de destino", font=font_label)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])

def converter_moeda():
    print("Convertendo moeda...")
botao_converter = customtkinter.CTkButton(janela, text="Converter",font=font_button, command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moedas_disponiveis = ["BRL: Real brasileiro", "USD: Dólar americano", "BTC: Bitcoin"]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()


# Inserir todos elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=0)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=0)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


# Roda a janela
janela.mainloop()