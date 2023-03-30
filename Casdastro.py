import sqlite3
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
root = Tk()

from datetime import date

data_atual = date.today()
print('São Paulo - SP - ' + str(data_atual))

class Application():

    def __init__(self):
        self.root = root   
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro")
        self.root.configure(background="#F4A460")
        self.root.geometry("1000x800")
        self.root.wm_resizable(True,True)
        self.root.maxsize(width=1000, height=900)
        self.root.minsize(width=400, height=300)      
    def frames_da_tela(self):
        self.frame_1=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)
        self.frame_2=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)    
    def widgets_frame1(self):
        ###botão limpar 
        self.bt_limpar=Button(self.frame_1,text="Limpar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão Busacar
        self.bt_buscar=Button(self.frame_1,text="Buscar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_buscar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão novo
        self.bt_novo=Button(self.frame_1,text="Novo",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_novo.place(relx=0.4,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão alterar
        self.bt_alterar=Button(self.frame_1,text="Alterar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_alterar.place(relx=0.5,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão apagar
        self.bt_apagar=Button(self.frame_1,text="Apagar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_apagar.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)      

        ###Label de Entradas
        self.lb_Codigo=Label(self.frame_1, text="Código",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Codigo.place(relx=0.1, rely=0.1)
        
        
        
        
        
Application()
