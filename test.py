import downloader
from tkinter import *

class Application:
    def __init__(self, master=None):
        # Seção de Variaveis
        self.fontePadrao = ("Arial", "12")

        # Seção do Containers
        self.containerTitulo = Frame(master)
        self.containerTitulo["pady"] = 30
        self.containerTitulo["padx"] = 30
        self.containerTitulo.pack()

        self.containerLink = Frame(master)
        self.containerLink["pady"] = 10
        self.containerLink["padx"] = 15
        self.containerLink.pack()

        self.containerResultado = Frame(master)
        self.containerResultado["pady"] = 10 
        self.containerResultado.pack()

        # Seção Titulo
        self.titulo = Label(self.containerTitulo, text="Youtube Video Downloader")
        self.titulo["font"] = ("Arial", "15")
        self.titulo.pack()

        # Seção Inserção de Link
        self.linkEtiqueta = Label(self.containerLink, text="Link do Video:", font=self.fontePadrao)
        self.linkEtiqueta.pack()

        self.link = Entry(self.containerLink)
        self.link["width"] = 50
        self.link["font"] = self.fontePadrao
        self.link.pack()

        self.alerta = Label(self.containerLink, text="", font=("Arial", "10", "italic"))
        self.alerta["foreground"] = "red"
        self.alerta.pack()

        # Seção Resultado
        self.pesquisaBotao = Button(self.containerResultado)
        self.pesquisaBotao["text"] = "BAIXAR"
        self.pesquisaBotao["font"] = self.fontePadrao
        self.pesquisaBotao["width"] = 15
        self.pesquisaBotao["command"] = self.fazerRequisicao
        self.pesquisaBotao.pack()

    def fazerRequisicao(self):
        link = self.link.get()

        if link.find("www.youtube.com/watch?") != -1:
            self.alerta["text"] = ""

            downloader.startDownload(link)
        else: 
            self.alerta["text"] = "Insira um link válido!"


        

root = Tk()
root.title("Youtube Video Downloader")
Application(root)
root.mainloop()