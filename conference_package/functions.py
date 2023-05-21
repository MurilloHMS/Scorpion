from webbrowser import open as web_open
from tkinter import END
from pyperclip import copy as py_copy
from tkinter.filedialog import askopenfilename, askopenfilenames
import os

class Functions():
    def link(self):
        web_open('https://github.com/MurilloHMS')
    
    def clearData(self):
        self.id_entry.delete(0, END)
        self.ean_entry.delete(0, END)
        self.ref_entry.delete(0, END)
        self.eanTrib_entry.delete(0, END)
        self.quant_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.unitValue_entry.delete(0, END)
        self.unitValueTotal_entry.delete(0, END)
        self.cfop_entry.delete(0, END)
        self.ncm_entry.delete(0, END)

    def onDoubleClick(self, event):
        self.clearData()
        self.mainInfo.selection()
        for n in self.mainInfo.selection():
            col = self.mainInfo.item(n, 'values')
            self.id_entry.insert(END, col[0])
            self.ean_entry.insert(END, col[2])
            self.ref_entry.insert(END, col[1])
            self.eanTrib_entry.insert(END, col[3])
            self.quant_entry.insert(END, col[5])
            self.description_entry.insert(END, col[4])
            self.unitValue_entry.insert(END, col[8])
            self.unitValueTotal_entry.insert(END, col[9])
            self.cfop_entry.insert(END, col[11])
            self.ncm_entry.insert(END, col[12])
            py_copy(self.ean_entry.get())
    
    def onEnterEvent(self, event):
        self.mainInfo.selection()
        for i in self.mainInfo.selection():
            col  = self.mainInfo.item(i , 'values')
            py_copy(col[4])
    
    def clearData(self):
        self.id_entry.delete(0, END)
        self.ean_entry.delete(0, END)
        self.ref_entry.delete(0, END)
        self.eanTrib_entry.delete(0, END)
        self.quant_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.unitValue_entry.delete(0, END)
        self.unitValueTotal_entry.delete(0, END)
        self.cfop_entry.delete(0, END)
        self.ncm_entry.delete(0, END)

    def openfilename(self):
        self.filename = askopenfilename()
        return self.filename
    
    def importXMLS(self):
        self.xml_files = askopenfilenames() 
        for i in self.xml_files:
            self.filename = i
            self.colectData(0)
            self.saveDataInfo()
            self.deleteNfeData()
            self.clearSuppliers()

    def importData(self):
        self.deleteNfeData()
        self.clearSuppliers()
        self.openfilename()
        self.colectData(0)

    def xmlfiles(self):
        self.deleteNfeData()
        self.clearSuppliers()
        self.importXMLS() 

    def xmlRename(self):
        self.deleteNfeData()
        self.clearSuppliers()
        self.xml_files = askopenfilenames()
        for i in self.xml_files:
            self.filename = i
            self.colectData(0)
            self.renameFiles()
            self.deleteNfeData()
            self.clearSuppliers()

    def xmlNotImported(self):
        self.deleteNfeData()
        self.clearSuppliers()
        self.xml_files = askopenfilenames()
        for n in self.xml_files:
            self.filename = n 
            self.colectData(0)
            self.identified()
            self.deleteNfeData()
            self.clearSuppliers()

    def clearSuppliers(self):
        self.supplierCnpj_entry.delete(0, END) 
        self.supplier_entry.delete(0, END)
        self.acessKey_entry.delete(0, END)
        self.nfenum_entry.delete(0, END)
        self.emissDate_entry.delete(0, END)
        self.loja_entry.delete(0, END)
        self.lojaCNPJ_entry.delete(0 , END)
        self.baseicms_entry.delete(0, END)
        self.valoricms_entry.delete(0, END)
        self.basest_entry.delete(0, END)
        self.valuest_entry.delete(0, END)
        self.basest_entry.delete(0, END)
        self.valuest_entry.delete(0, END)
        self.vnfe_entry.delete(0, END)
        self.vFrete_entry.delete(0, END)
        self.vSeguros_entry.delete(0, END)
        self.vdiscount_entry.delete(0, END)
        self.outherDispences_entry.delete(0, END)
        self.vipi_entry.delete(0, END)
        self.vtotalnfe.delete(0, END)
    
    def variables(self):
        self.id = self.id_entry.get()
        self.ref = self.ref_entry.get()
        self.eanvalor = self.ean_entry.get()
        self.eantributado = self.eanTrib_entry.get()
        self.quantidade = self.quant_entry.get()
        self.descriçao = self.description_entry.get()
        self.cfop1 = self.cfop_entry.get()
        self.valorunitario = self.unitValue_entry.get()
        self.valortotal = self.unitValueTotal_entry.get()
    
    def variablesSupplierInformation(self):
        self.frete = self.vFrete_entry.get()
        self.totalnota = self.vtotalnfe.get()
        self.forn = self.supplier_entry.get()
        self.cnpjfor = self.supplierCnpj_entry.get()
        self.acess = self.acessKey_entry.get()
        self.loja = self.loja_entry.get()
        self.cnpjloja = self.lojaCNPJ_entry.get()
        self.nfenum = self.nfenum_entry.get()
        self.emissdate = self.emissDate_entry.get()
        self.nfevalue = self.vnfe_entry.get()
        self.valuefrete = self.vFrete_entry.get()
        self.valuettnfe = self.vtotalnfe.get()
        self.baseicm = self.baseicms_entry.get()
        self.vicm = self.valoricms_entry.get()
        self.bst = self.basest_entry.get()
        self.vst = self.valuest_entry.get()
        self.security =  self.vSeguros_entry.get()
        self.discount = self.vdiscount_entry.get()
        self.odis = self.outherDispences_entry.get()
        self.vipi = self.vipi_entry.get()


    def renameFiles(self):
        self.mainInfo.delete(*self.mainInfo.get_children())
        self.variablesSupplierInformation()

        self.fretevalue =  self.vFrete_entry.get()
        self.supplier = self.supplier_entry.get()

        self.forn = self.forn.replace('/', '.')
        self.month = self.acessKey[4:6]
        self.year = self.acessKey[2:4]

        self.store_values()

        self.month = str(self.month)
        self.month = self.monthName[self.month]
        self.year = "20" + str(self.year)

        self.pathName = self.month[:4] + " - " + self.year 
        self.pathStore = self.storeName[self.cnpjloja] 
        self.dir_path = 'XML/NFe Finalizadas/'

        self.pathFiles()
        self.selectdata()

    def pathFiles(self):
        isExists = os.path.exists( self.dir_path + self.pathStore)
        if isExists == False:
            os.mkdir( self.dir_path + self.pathStore)
        elif isExists == True: 
            pass
        isExists = os.path.exists( self.dir_path + self.pathStore + '/' + self.forn )
        if isExists == False:
            os.mkdir( self.dir_path + self.pathStore + '/' + self.forn)
        elif isExists == True:
            pass
        isExists =  os.path.exists( self.dir_path + self.pathStore + '/' + self.forn + '/' + self.pathName)
        if isExists == False:
            os.mkdir( self.dir_path + self.pathStore + '/' + self.forn + '/' + self.pathName)
        elif isExists == True:
            pass
        try:
            os.rename(self.filename,  self.dir_path + self.pathStore + '/' + self.forn + '/' + self.pathName + '/' +  self.forn + ' Nº ' + self.nfenum + '.xml')
        except:
            os.remove(self.filename)

    def identified(self):
        self.mainInfo.delete(*self.mainInfo.get_children())
        self.variablesSupplierInformation()

        self.fretevalue =  self.vFrete_entry.get()
        self.supplier = self.supplier_entry.get()

        self.forn = self.forn.replace('/', '.')
        self.month = self.acessKey[4:6]
        self.year = self.acessKey[2:4]

        self.store_values()
        
        self.month = str(self.month)
        self.month = self.monthName[self.month]
        self.year = "20" + str(self.year)

        self.pathName = self.month[:4] + " - " + self.year 
        self.pathStore = self.storeName[self.cnpjloja] 
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.pathFiles()
        self.selectdata()