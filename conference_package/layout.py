from tkinter import Frame, Label, Button, Entry, ttk, Scrollbar, HORIZONTAL, VERTICAL, NO, Text

from conference_package.functions import Functions

class Layout(Functions):
    def mainWindow(self):
        self.root.title('Conferencia Casas Da Mamãe --> Criado por: Murillo HMS')
        self.root.configure(background='#160042')
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.window = str(self.width) + 'x' + str(self.height)
        self.root.geometry(self.window)
        self.root.resizable(True,True)
        self.root.state('zoomed')

    def windowframes(self):
        self.frame = Frame(self.root, bd = 4, bg='#353535', highlightbackground='#8470FF', highlightthickness=2)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight= 0.98)

    def labelsMainWindow(self):
        self.lb_id = Label(self.frame, text='ID', bg='#353535', fg='#ffffff', font=('verdana', 10) )
        self.lb_id.place(relx=0.05, rely=0.82)   
        
        self.lb_ref = Label(self.frame, text='Referência',  bg='#353535', fg='#ffffff', font=('verdana', 10))
        self.lb_ref.place(relx=0.16, rely = 0.82)
        
        self.lb_ean = Label(self.frame, text='EAN', bg='#353535', fg='#ffffff', font=('verdana', 10))
        self.lb_ean.place(relx=0.42, rely=0.82)
        
        self.lb_eantrib = Label(self.frame, text='EAN Tributado',  bg='#353535', fg='#ffffff', font=('verdana', 10))
        self.lb_eantrib.place(relx=0.58, rely=0.82)
        
        self.quant = Label(self.frame, text='Quantidade', bg='#353535', fg='#ffffff', font=('verdana', 10))
        self.quant.place(relx=0.82, rely=0.82)
        
        self.lb_description = Label(self.frame, text='Descrição', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_description.place(relx=0.27, rely=0.87)
        
        self.lb_cfop = Label(self.frame, text='CFOP',bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_cfop.place(relx=0.80, rely=0.87)
        
        self.lb_unitValue = Label(self.frame, text='Valor unitário', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_unitValue.place(relx=0.05, rely=0.93)
        
        self.lb_unitValueTotal = Label(self.frame, text='Valor Total', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_unitValueTotal.place(relx=0.23, rely=0.93)
        
        self.lb_ncm = Label(self.frame , text='NCM', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_ncm.place(relx= 0.47 , rely=0.93)
        
        self.lb_supplier = Label(self.frame, text='Fornecedor', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_supplier.place(relx=0.03, rely=0.01)
        
        self.lb_supplierCnpj = Label(self.frame, text='CNPJ Fornecedor', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_supplierCnpj.place(relx=0.43, rely=0.01)
        
        self.lb_acessKey = Label(self.frame, text='Chave de Acesso', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_acessKey.place(relx=0.70 , rely= 0.01)
        
        self.lb_loja = Label(self.frame, text='Razão social loja', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_loja.place(relx=0.03, rely=0.07)      
        
        self.lb_cnpjLoja = Label(self.frame, text='CNPJ Loja', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_cnpjLoja.place(relx=0.4, rely=0.07)
        
        self.lb_nfenum = Label(self.frame, text='Numero NFe', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_nfenum.place(relx=0.6, rely=0.07)
        
        self.lb_emissDate = Label(self.frame, text='Data de Emissão', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_emissDate.place(relx=0.80, rely = 0.07)
        
        self.lb_baseicms = Label(self.frame, text='Base ICMS', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_baseicms.place(relx=0.03, rely= 0.12)
        
        self.lb_valueICMS = Label(self.frame, text='Valor icms', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_valueICMS.place(relx=0.15, rely=0.12)
        
        self.lb_basest = Label(self.frame, text='Base ST', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_basest.place(relx=0.28, rely=0.12)
        
        self.lb_valueBaseSt = Label(self.frame, text='Valor ICM ST', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_valueBaseSt.place(relx=0.4, rely= 0.12)
        
        self.lb_nfe = Label(self.frame, text='Valor Total Produtos', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_nfe.place(relx=0.55, rely=0.12)
        
        self.lb_vfrete = Label(self.frame, text='Valor Frete', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_vfrete.place(relx= 0.03, rely= 0.167)
        
        self.lb_security = Label(self.frame, text='Valor Seguro', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_security.place(relx=0.15, rely=0.167)
        
        self.lb_discount = Label(self.frame, text= 'Valor Desconto', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_discount.place(relx= 0.27, rely= 0.167)
        
        self.lb_dispences = Label(self.frame, text='Outras Dispesas', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_dispences.place(relx=0.4, rely=0.167)
        
        self.lb_ipi = Label(self.frame, text='Valor Ipi', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_ipi.place(relx=0.56, rely= 0.167)
        
        self.lb_totalnfe = Label(self.frame, text= 'Valor Total NFe', bg='#353535', fg = '#ffffff', font=('verdana', 10))
        self.lb_totalnfe.place(relx=0.7, rely = 0.167)      

    def entrysMainWindow(self):
        self.id_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.id_entry.place(relx=0.04, rely=0.85, relwidth = 0.05, relheight=0.02)

        self.ref_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.ref_entry.place(relx=0.12, rely=0.85, relwidth = 0.20, relheight=0.02)

        self.ean_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.ean_entry.place(relx=0.35, rely=0.85, relwidth = 0.18, relheight=0.02)

        self.eanTrib_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.eanTrib_entry.place(relx=0.56, rely= 0.85, relwidth= 0.18, relheight= 0.02)

        self.quant_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.quant_entry.place(relx=0.8 , rely= 0.85, relwidth=0.15, relheight=0.02)

        self.description_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.description_entry.place(relx=0.04,rely=0.90,relwidth=0.60, relheight=0.02)

        self.cfop_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.cfop_entry.place(relx=0.75, rely=0.90, relwidth= 0.15, relheight=0.02)

        self.unitValue_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.unitValue_entry.place(relx=0.04, rely=0.96, relwidth=0.13, relheight=0.02)

        self.unitValueTotal_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.unitValueTotal_entry.place(relx=0.22, rely=0.96, relwidth= 0.13, relheight=0.02)

        self.ncm_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.ncm_entry.place(relx=0.43, rely= 0.96, relwidth= 0.13 , relheight=0.02)

        self.supplier_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.supplier_entry.place(relx=0.02, rely = 0.05, relwidth=0.35, relheight=0.02)

        self.supplierCnpj_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.supplierCnpj_entry.place(relx=0.39 , rely=0.05, relwidth=0.18, relheight=0.02)

        self.acessKey_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.acessKey_entry.place(relx=0.6 , rely=0.05, relwidth=0.38, relheight= 0.02)

        self.loja_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.loja_entry.place(relx=0.02, rely=0.1, relwidth = 0.35 , relheight=0.02)

        self.lojaCNPJ_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.lojaCNPJ_entry.place(relx=0.39, rely=0.1, relwidth=0.18 , relheight=0.02)

        self.nfenum_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.nfenum_entry.place(relx=0.60, rely = 0.1, relwidth=0.15, relheight=0.02)

        self.emissDate_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.emissDate_entry.place(relx=0.8, rely=0.1, relwidth=0.18, relheight=0.02)

        self.baseicms_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.baseicms_entry.place(relx=0.02, rely= 0.15, relwidth=0.12, relheight=0.02)

        self.valoricms_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.valoricms_entry.place(relx=0.15, rely=0.15, relwidth= 0.11, relheight=0.02)

        self.basest_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.basest_entry.place(relx=0.27, rely=0.15, relwidth=0.11, relheight=0.02)

        self.valuest_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.valuest_entry.place(relx= 0.4, rely=0.15, relwidth=0.13, relheight=0.02)

        self.vnfe_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vnfe_entry.place(relx=0.55, rely=0.15, relwidth=0.15, relheight=0.02)

        self.vFrete_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vFrete_entry.place(relx=0.02, rely=0.195, relwidth=0.12, relheight=0.02)

        self.vSeguros_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vSeguros_entry.place(relx= 0.15 , rely=0.195, relwidth=0.11, relheight=0.02)

        self.vdiscount_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vdiscount_entry.place(relx=0.27, rely=0.195, relwidth=0.11, relheight=0.02)

        self.outherDispences_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.outherDispences_entry.place(relx=0.4, rely= 0.195, relwidth=0.12, relheight=0.02)

        self.vipi_entry = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vipi_entry.place(relx=0.55, rely= 0.195, relwidth=0.12, relheight=0.02)

        self.vtotalnfe = Entry(self.frame, bg = '#808080' , fg = '#ffffff')
        self.vtotalnfe.place(relx=0.70, rely=0.195, relwidth=0.12, relheight=0.02)

    def buttons(self):
        self.btn_git = Button(self.frame, text = 'Created by: Murillo HMS', background= '#353535', activebackground='#353535', activeforeground='#8470ff', foreground= '#ffffff' , bd= 0, cursor = 'hand2', font=('yu gothic ui', 12, 'bold italic underline') , command = self.link)
        self.btn_git.place(relx = 0.85 , rely= 0.19)

    def mainData(self):
        colunas = []
        for i in range(1,30):
            vlr = 'col' + str(i)
            colunas.append(vlr)
        self.mainInfo = ttk.Treeview(self.frame, height=2,column=(colunas))
        values = ['','ID','Referência','EAN','EAN Tributado','Descrição','Quant', 'Custo + Imp + Frete','Custo + impostos',
                  'V. Unit','V. Total','Tipo','CFOP','NCM','CST','ICM Base','Aliq ICMS','Valor ICMS','Aliq IPI','Valor IPI',
                  'Valor IVA/MVA','Aliq ICM ST','Base ICM ST', 'Valor ICM ST','Aliq Pis','Valor Pis','Aliq Coffins','Valor Coffins',
                  'Pecent Frete','Valor Frete']
        for n in range(0,len(values)):
            n = str(n)
            self.mainInfo.heading('#' + n , text = values[int(n)])
        
        for n in range(0, len(values)):
            if n == 0:
                self.mainInfo.column('#' + str(n), width=5, minwidth=5, anchor= 'center', stretch=NO)
            elif n in [2,20,27,29]:
                self.mainInfo.column('#' + str(n), width=80, minwidth=80, anchor= 'center', stretch=NO)
            elif n in [3,4]:
                self.mainInfo.column('#' + str(n), width=100, minwidth=100, anchor= 'center', stretch=NO)
            elif n in [5]:
                self.mainInfo.column('#' + str(n), width=300, minwidth=300, stretch=NO)
            elif n in [21,26,28]:
                self.mainInfo.column('#' + str(n), width=70, minwidth=70, anchor= 'center', stretch=NO)
            elif n in [1]:
                self.mainInfo.column('#' + str(n), width=30, minwidth=30, anchor= 'center', stretch=NO)
            elif n in [7,8]:
                self.mainInfo.column('#' + str(n), width=120, minwidth=120, anchor= 'center', stretch=NO)
            else:
                self.mainInfo.column('#' + str(n), width=60, minwidth=60, anchor= 'center', stretch=NO)       
        
        self.mainInfo.tag_configure("evenrow",background='white',foreground='black')
        self.mainInfo.place(relx=0.01, rely= 0.23, relwidth=0.975, relheight=0.57)

        self.widget = Text(self.root, height=10)
        self.scrollx = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scrolly =Scrollbar(self.frame, orient=VERTICAL)
        self.scrolly.place(relx=0.985, rely=0.23, relwidth=0.012, relheight=0.57)
        self.scrollx.place(relx=0.01, rely=0.80, relwidth=0.985, relheight=0.015)
        self.mainInfo.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set, selectmode='extended')
        self.scrollx.configure(command= self.mainInfo.xview)
        self.scrolly.configure(command = self.mainInfo.yview)

        self.mainInfo.bind('<Double-1>', self.onDoubleClick)
        self.mainInfo.bind('<Return>', self.onEnterEvent)