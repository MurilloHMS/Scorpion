from tkinter import END , messagebox
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from dbfread import DBF
import datetime
import os
import pandas as pd

from dataframes.dataframe import Dataframes
from conference_package.functions import Functions
from dados.data import Data

class DataframeFunctions(Functions, Data):
    def selectMainData(self):
        self.mainInfo.delete(*self.mainInfo.get_children())
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT * FROM nfedata''')
        self.data = self.cursor.fetchall()   
        for i in self.data:
            self.mainInfo.insert('', END, values = i)  
        Dataframes.disconnectSDB(self)  
    
    def deleteNfeData(self):
        Dataframes.connectSDB(self)
        self.cursor.execute(''' DELETE FROM nfedata''' )  
        self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.clearData()
        self.selectMainData()
    
    def updateData(self):
        self.variables()
        Dataframes.connectSDB(self)
        self.cursor.execute('''UPDATE nfedata SET reference = %s, ean = %s, eantributed = %s, description = %s, amount = %s, unitvalue = %s, totalvalue = %s, cfop = %s WHERE id = %s ''',
                                (self.ref, self.eanvalor, self.eantributado,self.descriçao, self.quantidade, self.valorunitario,self.valortotal, self.cfop1 , self.id))
        self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.selectMainData()
        self.clearData()

    def notacheia(self):
        self.deleteNfeData()
        self.clearSuppliers()
        self.colectData(0)

    def meiaNota(self):
        self.Frete(1)
    
    def notax2(self):
        self.vFrete_entry.delete(0, END)
        self.vFrete_entry.insert(END, self.valuenfe)
        self.Frete(2)

    def insert_frete_value(self):
        self.Frete(1)
    
    def Frete(self, num):
        self.fretevalue =  self.vFrete_entry.get()
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT id, costcalculate, unitvalue  FROM nfedata''')
        self.data = self.cursor.fetchall() 
        self.variablesSupplierInformation()
        self.fretevalue = float(self.fretevalue)
        self.fretevalue = self.fretevalue * num
        for i  in self.data:
            prodid = int(i[0])
            custo = str(i[-1])
            custocomimpostos = float(i[1])
          
            self.frete = float(custo) * (float(self.fretevalue) / float(self.valuenfe))
            self.realcostcalculate = custocomimpostos + self.frete
            self.cursor.execute(''' UPDATE nfedata SET realcost = %s WHERE id = %s;''' , 
                                ('{:.2f}'.format(self.realcostcalculate), prodid))
            self.conn.commit()
        
        Dataframes.disconnectSDB(self)
        self.selectMainData()
    
    def colectData(self, frete):
        Dataframes.connectSDB(self)
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.file = f.read()
        except:
            with open(self.filename, 'r', encoding= "ISO-8859-1") as f:
                self.file = f.read()
        
        bs = BeautifulSoup(self.file, 'xml')
        
        self.supplierListInformation = []
        self.lista = []

        n = 1

        for i in bs.find_all('emit'):
            self.suppliers = i.xNome.getText() if i.xNome.getText() != "" else 'Sem Razão Social'
            self.supplier_entry.insert(END,self.suppliers)
            
            self.suppliersCNPJ = i.CNPJ.getText() if i.CNPJ.getText() != "" else 'Sem CNPJ'
            self.supplierCnpj_entry.insert(END, self.suppliersCNPJ)

        for i in bs.find_all('protNFe'):
            self.acesskey = i.chNFe.getText() if i.chNFe.getText() != "" else ''
            self.acessKey_entry.insert(END, self.acesskey)

        for i in bs.find_all('ide'):
            self.numnfe = i.nNF.getText() if i.nNF.getText() != "" else "Sem número de nota"
            self.nfenum_entry.insert(END, self.numnfe)

            self.emissDate = i.dhEmi.getText() if i.dhEmi.getText() != "" else datetime.datetime.now()
            self.emissDate = self.emissDate[:10].replace('-', '/')
            self.emissDate_entry.insert(END, self.emissDate)

            self.uf = i.cUF.getText() if i.cUF.getText() != "" else "NaN"
            
        for i in bs.find_all('dest'):
            self.loja = i.xNome.getText() if i.xNome.getText() != '' else 'Sem Loja de entrada' 
            self.loja_entry.insert(END,self.loja)

            self.lojaCNPJ = i.CNPJ.getText() if i.CNPJ.getText() != '' else 'Sem CNPJ da Loja'
            self.lojaCNPJ_entry.insert(END,self.lojaCNPJ)
        
        for i in bs.find_all('total'):
            self.vbaseicms = i.vBC.getText() if i.vBC.getText() != '' else 0
            self.vbaseicms = '{:.2f}'.format(float(self.vbaseicms))
            self.baseicms_entry.insert(END, self.vbaseicms)

            self.valueBaseICMS = i.vICMS.getText() if i.vICMS.getText() != '' else 0
            self.valueBaseICMS = '{:.2f}'.format(float(self.valueBaseICMS))
            self.valoricms_entry.insert(END, self.valueBaseICMS)

            self.vbasest = i.vBCST.getText() if i.vBCST.getText() != '' else 0
            self.vbasest = '{:.2f}'.format(float(self.vbasest))
            self.basest_entry.insert(END, self.vbasest)

            self.vicmst = i.vST.getText() if i.vST.getText() != '' else 0
            self.valuest_entry.insert(END, self.vicmst)

            self.valuenfe = i.vProd.getText() if i.vProd.getText() != '' else 0
            self.vnfe_entry.insert(END, self.valuenfe)

            self.valFrete = i.vFrete.getText() if i.vFrete.getText() != '' else 0 
            self.vFrete_entry.insert(END, self.valFrete)

            self.vseguros = i.vSeg.getText() if i.vSeg.getText() != '' else 0 
            self.vSeguros_entry.insert(END, self.vseguros)

            self.vdiscount = i.vDesc.getText() if i.vDesc.getText() != '' else 0
            self.vdiscount_entry.insert(END, self.vdiscount)

            self.outrasdespesas = i.vOutro.getText() if i.vOutro.getText() != '' else 0
            self.outherDispences_entry.insert(END, self.outrasdespesas)

            self.valoripi = i.vIPI.getText() if i.vIPI.getText() != '' else 0
            self.vipi_entry.insert(END, self.valoripi)

            self.valortotalnfe = i.vNF.getText() if i.vNF.getText() != '' else 0
            self.vtotalnfe.insert(END, self.valortotalnfe)

        for i in bs.find_all('det'):
            self.id = n
            
            self.ean = i.cEAN.getText() if i.cEAN.getText() != '' else '0'
           
            self.ref = i.cProd.getText() if i.cProd.getText() != '' else '0'
           
            self.quant = i.qCom.getText() if i.qCom.getText() != '' else '0'
            
            self.eanTributed = i.cEANTrib.getText() if  i.cEANTrib.getText() != '' else '0'
            
            self.unTrib = i.vUnTrib.getText() if i.vUnTrib.getText() != '' else '0'
            
            self.vTotal = i.vProd.getText() if i.vProd.getText() != '' else '0'
            
            self.des = i.xProd.getText() if i.xProd.getText() != '' else '0'
            
            self.un = i.vUnCom.getText() if i.vUnCom.getText() != '' else '0'
            
            self.tipo = i.uCom.getText() if i.uCom.getText() != '' else '0'
            
            self.cfop = i.CFOP.getText() if i.CFOP.getText() != '' else '0'
            
            self.ncm = i.NCM.getText() if i.NCM.getText() != '' else '0'
            
            self.cst = i.CST.getText() if i.CST.getText() != '' else '0'
            
            try: self.icmsBase = i.vBC.getText() if i.vBC.getText() != '' else '0'
            except: self.icmsBase = 0

            try: self.vICMS = i.vICMS.getText() if i.vICMS.getText() != '' else 0    
            except: self.vICMS = 0

            try: self.aliqICMS = i.pICMS.getText() if i.pICMS.getText() != '' else 0
            except: self.aliqICMS = 0

            try: self.aliqIpi = i.pIPI.getText() if i.pIPI.getText() != '' else 0
            except: self.aliqIpi = 0

            try: self.vIva = i.pMVAST.getText() if i.pMVAST.getText() != '' else 0
            except: self.vIva = 0
            
            try: self.pICMSt =  i.pICMS.getText() if i.pICMS.getText() != '' else 0
            except: self.pICMSt = 0 
            
            try: self.vBicmSt = i.vBCST.getText() if i.vBCST.getText() != '' else 0 
            except: self.vBicmSt = 0

            try: self.vICMSt = i.vICMS.getText() if i.vICMS.getText() != '' else 0 
            except: self.vICMSt = 0 

            try: self.aliqPis = i.pPIS.getText() if i.pPIS.getText() != '' else 0 
            except: self.aliqPis = 0

            try: self.vPis = i.vPIS.getText() if i.vPIS.getText() != '' else 0 
            except: self.vPis = 0

            try: self.aliqCoffins = i.pCOFINS.getText() if i.pCOFINS.getText() != '' else 0
            except: self.aliqCoffins = 0

            try: self.vCoffins = i.vCOFINS.getText() if i.vCOFINS.getText() != '' else 0
            except: self.vCoffins = 0 

            try: self.ipivalue = i.vIPI.getText() if i.vIPI.getText() != '' else 0 
            except: self.ipivalue = 0 
            
            if self.uf == "35":
                self.acress = 0
            else:
                self.aliqICMS = float(self.aliqICMS)
                self.acress = 18 - self.aliqICMS
                self.acress = float(self.acress)
                self.un = float(self.un)
                self.acress = float(self.vTotal) * (self.acress / 100)
            
            self.vIva = float(self.vIva)
            self.vIva = (self.vIva/100)
            self.vIva = float(self.vTotal) * self.vIva

            self.costcalculated =  (float(self.vTotal)  + float(self.acress) + float(self.ipivalue) ) / float(self.quant) #+ float(self.vICMSt) + float(self.vIva) + 
            
            if frete != 0:
                self.frete = float(self.un) * (float(frete) / float(self.valuenfe))
            else:
                self.frete = 0

            self.realcost = +  self.costcalculated + self.frete
            self.cursor.execute(''' INSERT INTO nfedata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                                (self.id, self.ref, self.ean, self.eanTributed, self.des ,self.quant,'{:.2f}'.format(self.realcost) ,'{:.2f}'.format(self.costcalculated), '{:.2f}'.format(float(self.un)), self.vTotal, self.tipo , self.cfop, self.ncm, self.cst, self.icmsBase,self.aliqICMS,
                                 self.vICMS, self.aliqIpi, self.ipivalue, self.vIva, self.pICMSt, self.vBicmSt,  self.vICMSt, self.aliqPis, self.vPis, self.aliqCoffins, self.vCoffins, self.frete ,  self.frete))
            n = n+ 1 

        self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.selectMainData()
        self.clearData()

    def deleteAnalise(self):
        Dataframes.connectSDB(self)
        self.cursor.execute('''DELETE FROM dbanalise''')
        self.conn.commit()
        Dataframes.disconnectSDB(self)        

    def createTxt(self):
        self.variablesSupplierInformation()
        lista = []  
        Dataframes.connectSDB(self)
        self.cursor.execute(''' SELECT reference FROM nfedata''')
        self.data = self.cursor.fetchall()
        
        for i in self.data:
            string = "," + i[0] +"\n"
            lista.append(string)

        self.file_name = 'coletores/' + self.forn + ' Nº ' +self.nfenum + '.txt'
        isExists = os.path.exists(self.file_name)

        if isExists == False:
            try:
                f = open(self.file_name , 'w')
                f.writelines(lista) 
                f.close
                messagebox.showinfo(tittle = 'Arquivo com Referências', message = 'Arquivo com Referências criado com sucesso!')
            except:
                messagebox.showinfo(tittle= 'ERROR', message = 'Ocorreu um erro ao criar o arquivo txt')
        else: 
            messagebox.showinfo(tittle='Arquivo Duplicado', message= 'já existe um arquivo criado com os dados desta nota fiscal!')
        Dataframes.disconnectSDB(self)
        

    def exportBase(self):
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT * FROM nfedatainformations''')
        self.data = self.cursor.fetchall()
        df = pd.DataFrame(self.data)
        df.to_csv('base.csv' , sep =',' , index = False)
        messagebox.showinfo(title="exportação de dados", message='Banco de dados exportado com sucesso')

    def insertEanWithTxt(self):
        Dataframes.connectSDB(self)
        self.fileEan = askopenfilename()
        self.cursor.execute('''SELECT id, reference FROM nfedata''')
        self.dados = pd.read_table(self.fileEan, sep = ',' ,names = ['Produtos',  ' '])
        self.dados = pd.DataFrame(self.dados)
        self.codigosEans = [] 
        
        for j in self.dados['Produtos']:
            self.codigosEans.append(j)
       
        vlr = 0

        self.data = self.cursor.fetchall() 
        for i  in self.data:
            prodid = int(i[0])
            try:
                Ean = self.codigosEans[vlr]
            except:
                break
            self.cursor.execute(''' UPDATE nfedata SET ean = %s, eantributed = %s WHERE id = %s;''' , (Ean, Ean, prodid))
            self.conn.commit() 
            vlr += 1
        
        Dataframes.disconnectSDB(self)
        self.selectMainData()

    def upload(self):
        self.createEngine()
        for num in range(1,14):
            if num < 10:
                num = '0' + str(num)
            else:
                num = str(num)

            self.df = DBF('sdb/ESTOQ0' + num + '.dbf' , encoding='latin1')
            self.df = pd.DataFrame(self.df)
            table = 'estoq0' + num
            self.df.to_sql(table, self.engine, if_exists='replace')
       
    
    def insertValuesInDataFrame(self):
        Dataframes.connectSDB(self)
        self.variablesSupplierInformation()
        self.index = self.forn + self.nfenum
        self.dataEntrada  = datetime.datetime.now()
        self.cursor.execute('''INSERT INTO nfinfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                            (self.index, self.forn, self.cnpjfor, self.nfenum, self.loja, self.cnpjloja,self.baseicm, self.vicm, self.bst, self.vst, self.valuefrete, self.security,
                            self.discount, self.odis, self.vipi, self.acess,self.dataEntrada, self.emissdate,self.nfevalue, self.valuettnfe,'NÃO LIBERADO'))
        self.conn.commit()
        Dataframes.disconnectSDB(self)

    def insertReference(self):
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT id, reference FROM nfedata''')
        self.data = self.cursor.fetchall() 
        for i  in self.data:
            prodid = int(i[0])
            referencia = str(i[1])
            self.cursor.execute(''' UPDATE nfedata SET ean = %s WHERE id = %s;''' , (referencia, prodid))
            self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.selectMainData()

    def saveDataInfo(self):
        self.mainInfo.delete(*self.mainInfo.get_children())
        self.variablesSupplierInformation()
        self.fretevalue =  self.vFrete_entry.get()
        self.supplier = self.supplier_entry.get()
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT reference, ean, eantributed, description, amount, realcost, costcalculate, unitvalue, totalvalue,tipe, cfop, ncm, cst, icmsbase, aliqicms, icmsvalue, aliqipi, ipivalue, ivamvavalue, aliqicmst,
                                icmstbase, icmstvalue, aliqpis, pisvalue, aliqcoffins, coffinsvalue,aliqfrete ,fretevalue FROM nfedata''') 
        self.data = self.cursor.fetchall()   
        for i in self.data:
            chave_primaria = i[0] + i[1] + i [3]
            self.cursor.execute('''INSERT INTO nfedatainformations VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                                (chave_primaria,i[0],i[1], i[2],i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27],self.nfenum, self.forn, self.cnpjfor, self.loja, self.cnpjloja, self.acess, self.fretevalue))
            self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.forn = self.forn.replace('/', '.')
        self.month = self.acess[4:6]
        self.year = self.acess[2:4]

        self.store_values()

        self.month = str(self.month)
        self.month = self.monthName[self.month]
        self.year = "20" + str(self.year)

        self.pathName = self.month[:4] + " - " + self.year 
        self.pathStore = self.storeName[self.cnpjloja] 
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        isExists = os.path.exists( 'XML/NFe Finalizadas/' + self.pathStore)

        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore)
        elif isExists == True: 
            pass
        isExists = os.path.exists('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn )
        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn)
        elif isExists == True:
            pass
        isExists =  os.path.exists('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName)
        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName)
        elif isExists == True:
            pass
        try:
            os.rename(self.filename, 'XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName + '/' +  self.forn + ' Nº ' + self.nfenum + '.xml')
        except:
            os.remove(self.filename)
        self.selectMainData()

    def store_values(self):
        self.store_data()


    def saveDataInfo(self):
        self.mainInfo.delete(*self.mainInfo.get_children())
        self.variablesSupplierInformation()
        self.fretevalue =  self.vFrete_entry.get()
        self.supplier = self.supplier_entry.get()
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT reference, ean, eantributed, description, amount, realcost, costcalculate, unitvalue, totalvalue,tipe, cfop, ncm, cst, icmsbase, aliqicms, icmsvalue, aliqipi, ipivalue, ivamvavalue, aliqicmst,
                                icmstbase, icmstvalue, aliqpis, pisvalue, aliqcoffins, coffinsvalue,aliqfrete ,fretevalue FROM nfedata''') 
        self.data = self.cursor.fetchall()   
        for i in self.data:
            chave_primaria = i[0] + i[1] + i [3]
            self.cursor.execute('''INSERT INTO nfedatainformations VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                                (chave_primaria,i[0],i[1], i[2],i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27],self.nfenum, self.forn, self.cnpjfor, self.loja, self.cnpjloja, self.acess, self.fretevalue))
            self.conn.commit()
        Dataframes.disconnectSDB(self)
        self.forn = self.forn.replace('/', '.')
        self.month = self.acess[4:6]
        self.year = self.acess[2:4]

        self.store_values()

        self.month = str(self.month)
        self.month = self.monthName[self.month]
        self.year = "20" + str(self.year)

        self.pathName = self.month[:4] + " - " + self.year 
        self.pathStore = self.storeName[self.cnpjloja] 
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        isExists = os.path.exists( 'XML/NFe Finalizadas/' + self.pathStore)

        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore)
        elif isExists == True: 
            pass
        isExists = os.path.exists('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn )
        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn)
        elif isExists == True:
            pass
        isExists =  os.path.exists('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName)
        if isExists == False:
            os.mkdir('XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName)
        elif isExists == True:
            pass
        try:
            os.rename(self.filename, 'XML/NFe Finalizadas/' + self.pathStore + '/' + self.forn + '/' + self.pathName + '/' +  self.forn + ' Nº ' + self.nfenum + '.xml')
        except:
            os.remove(self.filename)
        self.selectMainData()

    def store_values(self):
        self.monthName = {
            '01' : 'Jan',
            '02' : 'Feb',
            '03' : 'Mar',
            '04' : 'Apr',
            '05' : 'May',
            '06' : 'Jun',
            '07' : 'Jul',
            '08' : 'Aug',
            '09' : 'Sep',
            '10' : 'Oct',
            '11' : 'Nov',
            '12' : 'Dec', 
        }
        self.storeName = {
            '22272400000199' : 'MAGAZINE E ARMARINHO CASA DA MAMAE LTDA - ME',
            '28333270000133' : 'LED IN BRASIL ARTIGOS DE ILUMINACAO LTDA',
            '34561404000176' : 'LEDIBRASIL DIGITAL LOJA VIRTUAL EIRELI',
            '36030378000185' : 'CASA DA MAMAE II MAGAZINES EIRELI',
            '38135337000189' : 'LOJA DEPTO SBC CASA DA MAMAE',
            '38247636000105' : 'LOJA DEPTO SBC MERCADINHO',
            '36534263000128' : 'VILA LINDA CASA DA MAMAMAE EIRELI',
            '38135394000168' : 'VILA LINDA II CASA DA MAMAE LOJA DE DEP',
            '42902895000108' : 'VILA LINDA III CASA DA MAMAE',
            '34408066000137' : 'CASA DA MAMAE LOJA DE DEPARTAMENTO VAREJISTA EIREL',
            '45727265000124' : 'VICTORIA SAO MATEUS LOJAS DE DEPARTAMENTOS LTDA',
            '69156479000156' : 'CASA DA MAMAE TABOAO',
            '20675646000186' : 'QBABS PRESENTES  E VARIADES',
            '48651659000134' : 'MAGAZINE E ARMARINHO MELHOR DAS CASAS RJ',
            '37578616000154' : 'CENTRAL CASA DA MAMAE EIRELI' 
        }