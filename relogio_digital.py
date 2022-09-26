from tkinter import *
import tkinter
from datetime import datetime
import pyglet

pyglet.font.add_file('digital-7.ttf')           # Adicionando fontes externas

# ---------- cores ----------
cor_preta = '#3d3d3d'
cor_branca = '#fafcff'
cor_verde = '#21c25c'
cor_vermelha = '#eb463b'
cor_cinza = '#dedcdc'
cor_azul = '#3080f0'

janela = Tk()
janela.title('Relógio')
janela.geometry('400x180')
janela.resizable(width=False, height=False)
janela.config(bg=cor_preta)


def relogio():
    tempo = datetime.now()                 # Pega a hora atual da minha maquina

    # Define como sera apresentado o horario
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')

    label_1.config(text=hora)
    label_1.after(200, relogio)            # depois de 200ms ele vai chamar a função novamente
    label_2.config(text=dia_semana + '  ' + str(dia) + '/' + str(mes) + '/' + str(ano))


label_1 = Label(janela, text = '', font = ('digital-7 100'), bg = cor_preta, fg = cor_branca)
label_1.grid(row=0, column=0, sticky=NW, padx=5)

label_2 = Label(janela, text = '', font = ('digital-7 17'), bg = cor_preta, fg = cor_branca)
label_2.grid(row=2, column=0, sticky=NW, padx=5)
relogio()

janela.mainloop()
