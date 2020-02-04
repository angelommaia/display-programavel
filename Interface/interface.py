# -*- coding: utf-8 -*-
from tkinter import *
import subprocess

#a tela foi dividida em dois frames
root = Tk()				
root.iconbitmap('bolt.ico')		
frame = Frame(root,width=100, height=100)  
frame.pack()
bottomframe = Frame(root,width=100, height=100)
bottomframe.pack( side = BOTTOM )

#====Frame Layout====#
frame.option_add('*Font', 'tahoma 20 bold')
frame.master.title('Display LED')
frame.pack(expand = NO, fill = BOTH)

#display
#====Exibir Display====#
display = Entry(frame, bd = 5, justify='center', font="tahoma") #entry eh o widget usado para entrar com o texto
display.pack(padx=30, pady=1, side=TOP)

#obs: talvez seja necessario tratar melhor a entrada, impedindo o uso de caracteres nao interpretaveis 

#botão
#====Enviar Mensagem====#
#obs: lambda permite o uso de variaveis locais em outras partes do programa
SendButton = Button(bottomframe, text="Enviar Texto", font="tahoma", command = lambda: criar_arquivo(display) ) 
SendButton.pack(padx=10, pady=20, side=TOP)

#funcões
#====CRIANDO TXT===# 
def criar_arquivo(display):
	mensagem=open("msg_ard.txt","w") #criando arquivo para salvar o texto
	mensagem.write(display.get()) #escrevendo o texto no arquivo
	display.delete(0,"end") #limpando o widget entry
	subprocess.call(['open_explorer.bat']) #chamando script para rodar o .ino
                                           #talvez as tarefas executadas no script possam ser executadas aqui mesmo
	file.close() #fechando arquivo

root.mainloop()