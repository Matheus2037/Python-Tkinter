from tkinter import *

def teste_texto():
    Nome = "Matheus"
    Idade = 19

    texto_Nome["text"] = Nome
    texto_Idade["text"] = Idade

    return Nome, Idade


janela = Tk()
janela.title("Teste")
janela.geometry("400x400")

texto_titulo = Label(janela, text="Hello World!")
texto_titulo.grid(column=0, row=0)

botao = Button(janela, text="Clique aqui", command=teste_texto)
botao.grid(column=0, row= 2)

texto_Nome = Label(janela, text="")
texto_Nome.grid(column=0, row=3)

texto_Idade = Label(janela, text="")
texto_Idade.grid(column=0, row=5)

janela.mainloop()