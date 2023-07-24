from tkinter import ttk
from tkinter import *
import datetime 
import tkinter

from .functions import DataframeFunctions , DataframefunctionsArt

class Layout(DataframeFunctions):
    def filtroWindow(self):
        self.root.title('Filtro Banco de dados')
        self.root.configure(background='#160042')
        self.root.geometry('1550x720')
        self.root.resizable(True, True)

    def frameFiltro(self):
        self.frameFiltro = Frame(self.root, bd = 4, bg='#353535', highlightbackground='#8470FF', highlightthickness=2)
        self.frameFiltro.place(relx= 0.01, rely = 0.01, relwidth=0.98, relheight= 0.98)

    def labelsFrame(self):
        self.lb_reference = Label(self.frameFiltro, text='Referência',bg = '#353535', fg='#ffffff', font=('verdana', 10))
        self.lb_reference.place(relx=0.03, rely=0.03) 
        self.lb_description = Label(self.frameFiltro, text='Descrição',bg= '#353535' ,fg='#ffffff', font=('verdana', 10))
        self.lb_description.place(relx=0.2, rely=0.03) 
        self.lb_ean = Label(self.frameFiltro, text='Código de Barras', bg= '#353535',fg='#ffffff', font=('verdana', 10))
        self.lb_ean.place(relx=0.45, rely=0.03)
        self.lb_forn = Label(self.frameFiltro, text='Fornecedor', bg = '#353535' ,fg='#ffffff', font = ('verdana', 10))
        self.lb_forn.place(relx = 0.6 , rely = 0.03)
        self.lb_count = Label(self.frameFiltro , text = '',  bg = '#353535' , fg = '#ffffff', font = ('verdana', 10))
        self.lb_count.place(relx = 0.45 , rely = 0.09 ) 

    def entrysFrame(self):
        self.ref_entry = Entry(self.frameFiltro)
        self.ref_entry.place(relx= 0.03, rely=0.06, relwidth=0.12, relheight=0.02)
        self.descr_entry = Entry(self.frameFiltro)
        self.descr_entry.place(relx=0.2, rely=0.06, relwidth=0.22, relheight=0.02)
        self.eans_entry = Entry(self.frameFiltro)
        self.eans_entry.place(relx=0.45, rely=0.06, relwidth=0.12, relheight=0.02)
        self.forn_entry = Entry(self.frameFiltro)
        self.forn_entry.place(relx = 0.60 , rely=0.06 , relwidth = 0.20 , relheight = 0.02 )

    def buttons(self):
        self.bt_queryap = Button(self.frameFiltro, text = 'Pesquisa Aproximada', bg= '#353535', fg = '#ffffff', font=('verdana', 10), command = self.nfeQueryAp)
        self.bt_queryap.place(relx = 0.7, rely = 0.09, relwidth = 0.12, relheight = 0.03)
        self.bt_queryex = Button(self.frameFiltro, text = 'Pesquisa Exata', bg= '#353535', fg = '#ffffff', font=('verdana', 10), command = self.nfeQueryEx)
        self.bt_queryex.place(relx = 0.85, rely = 0.09, relwidth = 0.12, relheight = 0.03)
        
    def maindata(self):
        colunas = []
        for i in range(1,37):
            col = 'col' + str(i)
            colunas.append(col)
        self.main = ttk.Treeview(self.frameFiltro, height=2, column= (colunas))
        
        values = [ '', 'ID', 'Referência', 'EAN', 'EAN Tributado', 'Descrição', 'Quant', 'Custo + Imp + Frete', 'Custo + impostos', 'V. Unit', 'V. Total', 'Tipo', 'CFOP', 'NCM', 'CST', 'ICM Base', 'Aliq ICMS', 'Valor ICMS',
                   'Aliq IPI', 'Valor IPI', 'Valor IVA/MVA', 'Aliq ICM ST' , 'Base ICM ST', 'Valor ICM ST' , 'Aliq Pis', 'Valor Pis', 'Aliq Coffins', 'Valor Coffins', 'Pecent Frete', 'Valor Frete', 'NFe Nº', 'Fornecedor',
                     'CNPJ Fornecedor', 'Loja Entrada', 'CNPJ Loja Entrada', 'Chave de acesso', 'Valor do frete inserido']     
        
        for n in range(0,len(values)):
            n = str(n)
            self.main.heading('#' + n , text = values[int(n)])
        
        for n in range(0, len(values)):
            if n == 0:
                self.main.column('#' + str(n), width=5, minwidth=5, anchor= 'center', stretch=NO)
            elif n in [2,20,27,29]:
                self.main.column('#' + str(n), width=80, minwidth=80, anchor= 'center', stretch=NO)
            elif n in [3,4]:
                self.main.column('#' + str(n), width=100, minwidth=100, anchor= 'center', stretch=NO)
            elif n in [5]:
                self.main.column('#' + str(n), width=300, minwidth=300, stretch=NO)
            elif n in [21,26,28]:
                self.main.column('#' + str(n), width=70, minwidth=70, anchor= 'center', stretch=NO)
            elif n in [1]:
                self.main.column('#' + str(n), width=30, minwidth=30, anchor= 'center', stretch=NO)
            elif n in [7,8]:
                self.main.column('#' + str(n), width=120, minwidth=120, anchor= 'center', stretch=NO)
            else:
                self.main.column('#' + str(n), width=60, minwidth=60, anchor= 'center', stretch=NO) 
        
        self.main.place(relx= 0.01 , rely = 0.12, relwidth= 0.97, relheight= 0.85)

        self.widget = Text(self.root, height=10)
        self.scrollx = Scrollbar(self.frameFiltro, orient=HORIZONTAL)
        self.scrolly =Scrollbar(self.frameFiltro, orient=VERTICAL)
        self.scrolly.place(relx=0.98, rely=0.12, relwidth=0.012, relheight=0.85)
        self.scrollx.place(relx=0.01, rely=0.97, relwidth=0.985, relheight=0.015)
        self.main.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.main.configure(selectmode='extended')

        self.scrollx.configure(command= self.main.xview)
        self.scrolly.configure(command = self.main.yview)


class LayoutArt(DataframefunctionsArt):
    def artsystemWindow(self):
        self.rootArtsystem.title('Filtro Artsystem')
        self.rootArtsystem.configure(background = '#160042')
        self.rootArtsystem.geometry('1550x720')
        self.rootArtsystem.resizable(True, True)
    
    def ArtsystemFrame(self):
        self.frameArtsystem = Frame(self.rootArtsystem, bd = 4, bg='#353535', highlightbackground='#8470FF', highlightthickness=2)
        self.frameArtsystem.place(relx= 0.01, rely = 0.01, relwidth=0.98, relheight= 0.98)

    def ArtsytemLabel(self):
        self.lb_referenceArt = Label(self.frameArtsystem, text='Referência', bg = '#353535', fg='#ffffff', font = ('verdana', 10))
        self.lb_referenceArt.place(relx=0.03, rely=0.03)
        self.lb_descriptionArt = Label(self.frameArtsystem, text='Descrição', bg = '#353535' ,fg='#ffffff', font=('verdana' , 10))
        self.lb_descriptionArt.place(relx=0.15, rely= 0.03)
        self.lb_eanArt = Label(self.frameArtsystem, text='Código de barras', bg = '#353535', fg='#ffffff', font=('verdana', 10))
        self.lb_eanArt.place(relx=0.4, rely = 0.03)
        self.lb_fornArt = Label(self.frameArtsystem , text = 'Fornecedor ', bg = '#353535', fg= '#ffffff', font = ('verdana' , 10))
        self.lb_fornArt.place(relx=0.53 , rely = 0.03)
        self.lb_pluArt = Label(self.frameArtsystem, text = 'PLU', bg = '#353535', fg = '#ffffff', font= ('verdana', 10))
        self.lb_pluArt.place(relx = 0.70, rely = 0.03)
        self.lb_departmentsArt = Label(self.frameArtsystem , text = 'Departamentos', bg = '#353535' , fg = '#ffffff', font = ('verdana', 10))
        self.lb_departmentsArt.place(relx = 0.82, rely =0.03)
        self.lb_countArt = Label(self.frameArtsystem , text = '',  bg = '#353535' , fg = '#ffffff', font = ('verdana', 10))
        self.lb_countArt.place(relx = 0.7 , rely = 0.1 )

    def entrysFrameArtsystem(self):
        self.refArt_entry = Entry(self.frameArtsystem)
        self.refArt_entry.place(relx=0.03, rely=0.06, relwidth= 0.08, relheight=0.02)
        self.descrArt_entry = Entry(self.frameArtsystem)
        self.descrArt_entry.place(relx=0.15, rely=0.06, relwidth=0.22, relheight=0.02)
        self.eanArt_entry = Entry(self.frameArtsystem)
        self.eanArt_entry.place(relx=0.4, rely = 0.06, relwidth=0.08, relheight=0.02)
        self.fornArt_entry = Entry(self.frameArtsystem)
        self.fornArt_entry.place(relx =0.53 , rely =0.06 , relwidth= 0.12 , relheight = 0.02 )
        self.plu_entry = Entry(self.frameArtsystem)
        self.plu_entry.place(relx=0.70, rely = 0.06, relwidth = 0.08, relheight = 0.02)
        self.departments_entry = Entry(self.frameArtsystem)
        self.departments_entry.place(relx=0.82, rely = 0.06, relwidth = 0.12, relheight = 0.02)

    def ArtsytemButtons(self):
        self.bt_queryAp = Button(self.frameArtsystem, text = 'Pesquisa aproximada', bg = '#353535' , fg = '#ffffff' , activebackground='#8470ff', font = ('verdana' , 10), command = self.artsytemQueryAp)
        self.bt_queryAp.place(relx = 0.7 , rely = 0.15, relwidth = 0.12 , relheight = 0.03)
        self.bt_queryEx = Button(self.frameArtsystem, text = 'Pesquisa Exata', bg = '#353535' , fg = '#ffffff' ,activebackground = '#8470ff', font = ('verdana' , 10), command = self.artsytemQueryEx)
        self.bt_queryEx.place(relx = 0.83 , rely = 0.15, relwidth = 0.12 , relheight = 0.03)

    def maindataArtsystenfiltro(self):
        self.artsystem = ttk.Treeview(self.frameArtsystem, height = 2 , column = ('col1', 'col2', 'col3','col4', 'col5', 'col6' , 'col7','col8', 'col9', 'col10'))
        self.artsystem.heading('#0', text = '')
        self.artsystem.heading('#1', text = 'PLU')
        self.artsystem.heading('#2', text = 'Descrição')
        self.artsystem.heading('#3', text = 'NCM')
        self.artsystem.heading('#4', text = 'EAN')
        self.artsystem.heading('#5', text = 'Departamento')
        self.artsystem.heading('#6', text = 'Custo')
        self.artsystem.heading('#7', text = 'PMZ')
        self.artsystem.heading('#8', text = 'Venda')
        self.artsystem.heading('#9', text = 'Referência')
        self.artsystem.heading('#10', text = 'Fornecedores')

        self.artsystem.column('#0', width=5 , minwidth=5, anchor = 'center', stretch = NO)
        self.artsystem.column('#1', width= 80 , minwidth = 80 , anchor = 'center', stretch = NO)
        self.artsystem.column('#2', width= 300 , minwidth = 300 ,stretch = NO)
        self.artsystem.column('#3', width=80 , minwidth=80, anchor = 'center', stretch = NO)
        self.artsystem.column('#4', width= 120 , minwidth = 120 , anchor = 'center', stretch = NO)
        self.artsystem.column('#5', width=180 , minwidth=180, anchor = 'center', stretch = NO)
        self.artsystem.column('#6', width= 80 , minwidth = 80 , anchor = 'center', stretch = NO)
        self.artsystem.column('#7', width=80 , minwidth=80, anchor = 'center', stretch = NO)
        self.artsystem.column('#8', width= 80 , minwidth = 80 , anchor = 'center', stretch = NO)
        self.artsystem.column('#9', width=130 , minwidth=130, stretch = NO)
        self.artsystem.column('#10', width= 400 , minwidth = 400 , stretch = NO)

        self.artsystem.place(relx=0.01, rely=0.2 , relwidth=0.97 , relheight = 0.77)

        self.widget_art = Text(self.rootArtsystem , height = 10)
        self.scrollx_art = Scrollbar(self.frameArtsystem, orient = HORIZONTAL)
        self.scrolly_art = Scrollbar(self.frameArtsystem , orient = VERTICAL)
        self.scrolly_art.place(relx = 0.98, rely = 0.20 , relwidth= 0.012 , relheight= 0.77)
        self.scrollx_art.place(relx = 0.01, rely= 0.97, relwidth=0.985 , relheight= 0.015)
        self.artsystem.configure(yscrollcommand= self.scrolly_art.set , xscrollcommand= self.scrollx_art.set)
        self.artsystem.configure(selectmode = 'extended')

        self.scrollx_art.configure(command = self.artsystem.xview)
        self.scrolly_art.configure(command= self.artsystem.yview)