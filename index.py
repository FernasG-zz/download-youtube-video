from tkinter import *
from tkinter import ttk
import downloader as core

root = Tk()
root.title("Youtube Video Downloader")
root.geometry("1280x720")
fontePadrao = ("Arial", "15")
master = None

# Funcões para Interação com "back-end"
def pesquisarVideo():
    link = root.link.get()

    if link.find("www.youtube.com/watch?") != -1:
        root.alert["text"] = ""
        root.alert["pady"] = 0

        streamList = core.downloaderManager(link)
        root.videoInfo["text"] = "[ " + streamList["title"] + " ] - " + streamList["author"] + " / " + str(streamList["views"])

    else: 
        root.alert["text"] = "Insira um link válido!"
        root.alert["pady"] = 10

# Seção Titulo 
tituloLabel = Label(master, text="Youtube Video Downloader", font=("Arial", "20", "bold"))
tituloLabel["pady"] = 15
tituloLabel.pack()

# Definição de Containers
root.containerConteudo = Frame(master)
root.containerConteudo["padx"] = 15
root.containerConteudo["pady"] = 15
root.containerConteudo.pack()

root.containerRodape = Frame(master)
root.containerRodape.pack()

# Conteudo do App

# Seção de Requisição
root.linkLabel = Label(root.containerConteudo, text="Link do Video:", font=fontePadrao)
root.linkLabel.pack()

root.link = Entry(root.containerConteudo)
root.link["width"] = 100
root.link["font"] = fontePadrao
root.link.pack()

root.alert = Label(root.containerConteudo, text="", font=("Arial", "10", "italic"))
root.alert["foreground"] = "red"
root.alert.pack()

root.botao = Button(root.containerConteudo)
root.botao["text"] = "Pesquisar"
root.botao["font"] = fontePadrao
root.botao["width"] = 15
root.botao["command"] = pesquisarVideo
root.botao.pack()

root.videoInfo = Label(root.containerConteudo, text="", font=("Calibri", "12"))
root.videoInfo["pady"] = 30
root.videoInfo.pack()

# Seção do Rodapé
root.info = ttk.Progressbar(root.containerRodape, orient=HORIZONTAL, length=300, mode="determinate")

root.mainloop()