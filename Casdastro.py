import sqlite3
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
import sqlite3

from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class Relatorios():
    def printCadastro(self):
        webbrowser.open("Cadastro.pdf")
    def geraRelatorioCad(self):
        self.c = canvas.Canvas("Cadastro.pdf")
        
        self.codRel = self.cod_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        

class Funcs():
    def limpa_tela(self):
        self.cod_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("cadastro.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados") 
    def desconecta_bd(self):
        self.conn.close(); print("Desconecta ao banco de dados") 
    def montaTabelas(self):
        self.conecta_bd()
        ###Criação da tabela 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastro (
                cod INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                telefone INTEGER(20),
                Cidade CHAR(40)                
            );
        """)         
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.cod = self.cod_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cadastro(self):
        self.variaveis()
        self.conecta_bd()
        
        self.cursor.execute(""" INSERT INTO cadastro (nome, telefone, cidade)
            VALUES(?, ?, ?)""",(self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_list()
        self.limpa_tela()
    def select_list(self):
        self.listCAD.delete(*self.listCAD.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome, telefone, cidade FROM cadastro 
            ORDER BY nome ASC """)
        for i in lista: 
            self.listCAD.insert("", END, values=i)
        self.desconecta_bd()
    def OnDoubleleClick(self, event):
        self.limpa_tela()
        self.listCAD.selection()
        
        for n in self.listCAD.selection():
            col1, col2, col3, col4 = self.listCAD.item(n,'values')
            self.cod_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cadastro(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM cadastro WHERE cod = ? """,(self.cod))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_list()
    def alterar_cadastro(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE cadastro SET nome = ?, telefone = ?, cidade = ? 
            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.cod))
        self.conn.commit()
        self.desconecta_bd()
        self.select_list()
        self.limpa_tela()


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
        self.montaTabelas()
        self.select_list()
        self.Menus()
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
        self.bt_novo=Button(self.frame_1,text="Novo",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ), command= self.add_cadastro)
        self.bt_novo.place(relx=0.4,rely=0.1,relwidth=0.1,relheight=0.15)

        ###botão alterar
        self.bt_alterar=Button(self.frame_1,text="Alterar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ), command= self.alterar_cadastro)
        self.bt_alterar.place(relx=0.5,rely=0.1,relwidth=0.1,relheight=0.15)

        ###botão apagar
        self.bt_apagar=Button(self.frame_1,text="Apagar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ),command = self.deleta_cadastro)
        self.bt_apagar.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)      

        ###Label do codigo
        self.lb_cod=Label(self.frame_1, text="Código",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_cod.place(relx=0.1, rely=0.1)
        self.cod_entry = Entry(self.frame_1)
        self.cod_entry.place(relx=0.05, rely=0.18, relwidth= 0.10)

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
        self.lb_cidede=Label(self.frame_1, text="Cidade",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_cidede.place(relx=0.5, rely=0.5)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.6, relwidth= 0.4)

        ###Data
        self.lb_horas=Label(self.frame_1, text= ('São Paulo - SP - ' + str(data_atual)) ,bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_horas.place(relx=0.1, rely=0.7)
    def Lista_frame2(self):
        self.listCAD =ttk.Treeview(self.frame_2, height= 3,column= ("col1", "col2", "col3", "col4"))
        self.listCAD.heading("#0", text="")
        self.listCAD.heading("#1", text="Código")
        self.listCAD.heading("#2", text="Nome")
        self.listCAD.heading("#3", text="Telefone")
        self.listCAD.heading("#4", text="Cidade")

        self.listCAD.column("#0", width=1)
        self.listCAD.column("#1", width=25)
        self.listCAD.column("#2", width=200)
        self.listCAD.column("#3", width=125)
        self.listCAD.column("#4", width=125)

        self.listCAD.place(relx=0.01,rely=0.1, relwidth=0.96, relheight=0.85)
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listCAD.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.1, relwidth=0.02, relheight=0.85 )
        self.listCAD.bind("<Double-1>", self.OnDoubleleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.root.destroy()
        
        menubar.add_cascade(label = "Opções ", menu = filemenu)
        menubar.add_cascade(label = "Sobre ", menu = filemenu2)
        
        filemenu.add_command(label= "Sair", command= Quit)
        filemenu.add_command(label= "limpa Cadastro", command= self.limpa_tela )
        
Application()
