from tkinter import Menu

from conference_package.functions import Functions
from conference_package.dataframe_functions import DataframeFunctions


class Menus(DataframeFunctions):
        def menu(self):
                self.menubar = Menu(self.root, borderwidth=0 , bg="#20232A", fg = 'white')
                self.root.config(menu = self.menubar)
                self.option = Menu(self.menubar)
                self.fretes = Menu(self.menubar)
                self.functions = Menu(self.menubar)
                self.filters = Menu(self.menubar)
                self.nfe = Menu(self.menubar)
                self.dataframe = Menu(self.menubar)
                self.relatorios = Menu(self.menubar)

                def quit(): self.root.destroy()

                self.menubar.add_cascade(label = 'Opções', menu = self.option, background="#20232A", foreground = 'white')
                self.menubar.add_cascade(label = 'Fretes' , menu = self.fretes )
                self.menubar.add_cascade(label = 'Funções', menu = self.functions)
                self.menubar.add_cascade(label = 'Filtros', menu = self.filters)
                self.menubar.add_cascade(label = 'Notas Fiscais', menu = self.nfe)
                self.menubar.add_cascade(label = 'DataFrame' , menu = self.dataframe)
                self.menubar.add_cascade(label = 'Relatórios' , menu = self.relatorios)

                
                self.option.add_command(label = 'Importar XML', background="#20232A", foreground = 'white',activebackground='#8470ff', command =  self.importData)
                self.option.add_command(label = 'Importar XMLS', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.xmlfiles) 
                self.option.add_command(label = 'Renomear XMLS e Pastas', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.xmlRename)
                self.option.add_command(label = 'Identificar XML Já Importados', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.xmlNotImported)
                self.option.add_command(label = 'Inserir Referencia no EAN', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.insertReference)
                self.option.add_command(label = 'Deletar Dados Da Nota Fiscal Importada', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.deleteNfeData)
                self.option.add_command(label = 'Apagar Dados Preenchidos', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.clearData)
                self.option.add_command(label = 'Alterar Dados', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.updateData)
                self.option.add_command(label = 'Salvar Dados', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.saveDataInfo)
                self.option.add_command(label = 'Sair', background="#20232A", foreground = 'white',activebackground='#8470ff', command=quit)

                self.fretes.add_command(label = 'Nota Cheia', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.notacheia)
                self.fretes.add_command(label = 'Meia Nota', background="#20232A", foreground = 'white',activebackground='#8470ff', command=self.meiaNota)
                self.fretes.add_command(label = 'Nota x2', background="#20232A", foreground = 'white',activebackground='#8470ff', command=self.notax2)
                self.fretes.add_command(label = 'Inserir Valor do Frete', background="#20232A", foreground = 'white',activebackground='#8470ff', command =self.insert_frete_value)

                # self.filters.add_command(label = 'Notas de Entrada', background="#20232A", foreground = 'white',activebackground='#8470ff', command = Filter)
                # self.filters.add_command(label = 'Artsystem', background="#20232A", foreground = 'white',activebackground='#8470ff', command = ArtystemFilter)
        
                self.nfe.add_command(label = 'Salvar Status no Banco', background="#20232A", foreground = 'white',activebackground='#8470ff', command = self.insertValuesInDataFrame)
        
                # self.functions.add_command(label = 'Converter pdf para word' , background = '#20232A', foreground = 'white' , activebackground= '#8470ff', command = self.pdfConversion)
                self.functions.add_command(label = 'Inserir Eans com TXT' , background = '#20232A' , foreground = '#ffffff' , activebackground = '#8470ff', command = self.insertEanWithTxt)
                self.functions.add_command(label = 'Criar arquivo com Referencias' , background = '#20232A' , foreground = '#ffffff' , activebackground = '#8470ff' , command = self.createTxt)
        
                self.dataframe.add_command(label = 'Subir Bases', background = '#20232A' , foreground = '#ffffff' , activebackground = '#8470ff' , command = self.upload)
                # self.dataframe.add_command(label = 'Criar Tabelas SQL', background = '#20232A', foreground= '#ffffff', activebackground= '#8470ff', command= self.createTablesWithSQL)
                self.dataframe.add_command(label = 'Exportar base de dados' , background = '#20232A' , foreground = '#ffffff' , activebackground = '#8470ff', command = self.exportBase)

                # self.relatorios.add_command(label = 'Relatório', background="#20232A", foreground = 'white',activebackground='#8470ff', command=self.gerarRelatorio )
