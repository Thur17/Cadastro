import sqlite3
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
root = Tk()

class Funcs():
    def limpa_tela(self):
        self.Codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.Cidade_entry.delete(0, END)

from datetime import date

data_atual = date.today()
print('São Paulo - SP - ' + str(data_atual))

class Application(Funcs):

    def __init__(self):
        self.root = root   
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.Lista_frame2()
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
        self.bt_limpar=Button(self.frame_1,text="Limpar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ), command= self.limpa_tela)
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

        ###Label do codigo
        self.lb_Codigo=Label(self.frame_1, text="Código",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Codigo.place(relx=0.1, rely=0.1)
        
        self.Codigo_entry = Entry(self.frame_1)
        self.Codigo_entry.place(relx=0.05, rely=0.18, relwidth= 0.10)

        ###Label nome 
        self.lb_nome=Label(self.frame_1, text="Nome",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_nome.place(relx=0.1, rely=0.3)
        
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.4, relwidth= 0.85)

        ### Label Telefone
        self.lb_telefone=Label(self.frame_1, text="Telefone",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_telefone.place(relx=0.1, rely=0.5)
        
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.6, relwidth= 0.4)

        ###Label Cidade 
        self.lb_Cidede=Label(self.frame_1, text="Cidade",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Cidede.place(relx=0.5, rely=0.5)
        
        self.Cidade_entry = Entry(self.frame_1)
        self.Cidade_entry.place(relx=0.5, rely=0.6, relwidth= 0.4)
        
        self.lb_horas=Label(self.frame_1, text= ('São Paulo - SP - ' + str(data_atual)) ,bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_horas.place(relx=0.1, rely=0.7)

    def Lista_frame2(self):
        self.listCAD =ttk.Treeview(self.frame_2, height= 3,column= ("col1", "col2", "col3", "col4"))
        self.listCAD.heading("#0", text="")
        self.listCAD.heading("#1", text="Codigo")
        self.listCAD.heading("#2", text="Nome")
        self.listCAD.heading("#3", text="Telefone")
        self.listCAD.heading("#4", text="Cidade")
        
        self.listCAD.column("#0", width=1)
        self.listCAD.column("#1", width=50)
        self.listCAD.column("#2", width=200)
        self.listCAD.column("#3", width=125)
        self.listCAD.column("#4", width=125)
        
        self.listCAD.place(relx=0.01,rely=0.1, relwidth=0.96, relheight=0.85)
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listCAD.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.1, relwidth=0.02, relheight=0.85 )
        
        
Application()
