from tkinter import END
from dataframes.dataframe import Dataframes

class Functions():
    def variables(self):
        self.descricao = self.descr_entry.get()
        self.referencia = self.ref_entry.get()
        self.ean = self.eans_entry.get()
        self.fornecedor = self.forn_entry.get()

class DataframeFunctions(Functions, Dataframes):
    def nfeQueryAp(self):
        Dataframes.connectSDB(self)
        self.main.delete(*self.main.get_children())
        self.variables()
        
        self.descricao = '%' + self.descricao +'%'
        self.referencia = '%' + self.referencia +'%'
        self.ean = '%' + self.ean +'%'
        self.fornecedor = '%' + self.fornecedor +'%'

        query = {
            '0' : "(fornecedor LIKE %s)",
            '1' : "(ean LIKE %s)",
            '2' : "(reference LIKE %s)",
            '3' : "(description LIKE %s)",
        }
        values = {
            '0' : self.fornecedor,
            '1' : self.ean,
            '2' : self.referencia,
            '3' : self.descricao,
        }
        valores = (self.fornecedor, self.ean, self.referencia, self.descricao)
        con = []
        for i in valores:
            if i != '%%' :
                j = True
            else :  
                j = False
            con.append(j)
        n = 0
        dictFinal = []
        for i in con:
            if i == True:
                dictFinal.append(n)
                n += 1
            else:
                n += 1

        if  len(dictFinal) == 4:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or "+ query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " or "+ query[str(dictFinal[3:4]).replace('[','').replace(']', '')]
        elif  len(dictFinal) == 3:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] 
        elif  len(dictFinal) == 2:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 1:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')]

        self.valores = []

        for i in dictFinal:
            self.valores.append(values[str(i)])
        try:        
            self.query = " SELECT * FROM nfedatainformations where " + string
            self.cursor.execute(self.query, list(self.valores))
        except:
            self.query = "SELECT * FROM nfedatainformations"
            self.cursor.execute(self.query)

        self.datalist = self.cursor.fetchall()
        self.count = 0
        for i in self.datalist:
            self.main.insert('', END, values = i)
            self.count += 1
        self.lb_count.configure(text = f'Produtos Retornados na Pesquisa -> {self.count}')
        Dataframes.disconnectSDB(self)

    def nfeQueryEx(self):
        Dataframes.connectSDB(self)
        self.main.delete(*self.main.get_children())
        self.variables()
        
        self.descricao = '%' + self.descricao +'%'
        self.referencia = '%' + self.referencia +'%'
        self.ean = '%' + self.ean +'%'
        self.fornecedor = '%' + self.fornecedor +'%'

        query = {
            '0' : "(fornecedor LIKE %s)",
            '1' : "(ean LIKE %s)",
            '2' : "(reference LIKE %s)",
            '3' : "(description LIKE %s)",
        }
        values = {
            '0' : self.fornecedor,
            '1' : self.ean,
            '2' : self.referencia,
            '3' : self.descricao,
        }
        valores = (self.fornecedor, self.ean, self.referencia, self.descricao)
        con = []
        for i in valores:
            if i != '%%' :
                j = True
            else :  
                j = False
            con.append(j)
        n = 0
        dictFinal = []

        for i in con:
            if i == True:
                dictFinal.append(n)
                n += 1
            else:
                n += 1

        if  len(dictFinal) == 4:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and "+ query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " and "+ query[str(dictFinal[3:4]).replace('[','').replace(']', '')]
        elif  len(dictFinal) == 3:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] 
        elif  len(dictFinal) == 2:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 1:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')]
    
        self.valores = []

        for i in dictFinal:
            self.valores.append(values[str(i)])
        try:
            self.query = " SELECT * FROM nfedatainformations where " + string
            self.cursor.execute(self.query, list(self.valores))
        except:
            self.query = " SELECT * FROM nfedatainformations"
            self.cursor.execute(self.query)
        
        self.datalist = self.cursor.fetchall()
        self.count = 0
        for i in self.datalist:
            self.main.insert('', END, values = i)
            self.count += 1 
        self.lb_count.configure(text = f'Produtos Retornados na Pesquisa -> {self.count}')
        Dataframes.disconnectSDB(self)



class DataframefunctionsArt(Dataframes):
    def artsytem(self):
        self.artsystem.delete(*self.artsystem.get_children())
        Dataframes.connectSDB(self)
        self.cursor.execute('''SELECT * FROM sdbartsystem''')
        self.datalist = self.cursor.fetchall()
        self.count = 0
        for i in self.datalist:
            self.artsystem.insert('', END, values = i)  
            self.count += 1
        self.lb_countArt.configure(text = f'Produtos Retornados na Pesquisa -> {self.count}') 
        Dataframes.disconnectSDB(self)

    def variablesArt(self):
        self.fornecedorArt = self.fornArt_entry.get() 
        self.eanArt = self.eanArt_entry.get()
        self.descriptionArt = self.descrArt_entry.get()
        self.pluArt = self.plu_entry.get()
        self.supplierArt = self.fornArt_entry.get()
        self.departmentsArt = self.departments_entry.get()
        self.refArt = self.refArt_entry.get()

    def artsytemQueryAp(self):
        self.artsystem.delete(*self.artsystem.get_children())
        Dataframes.connectSDB(self)
        self.variablesArt()

        self.fornecedorArt =  '%' + self.fornecedorArt + '%'
        self.eanArt = '%' + self.eanArt + '%'
        self.descriptionArt = '%' + self.descriptionArt + '%'
        self.pluArt = '%' + self.pluArt + '%'
        self.supplierArt = '%' + self.supplierArt + '%'
        self.departmentsArt = '%' + self.departmentsArt + '%'
        self.refArt = '%' + self.refArt + '%'

        query = {
            '0' : "(plu != '' and plu LIKE %s)",
            '1' : "(ean != '' and ean LIKE %s)",
            '2' : "(descriptions != '' and descriptions LIKE  %s)",
            '3' : "(suppliers != '' and suppliers LIKE %s)",
            '4' : "(suppliers_code != '' and suppliers_code LIKE %s)",
            '5' : "(department != '' and department LIKE %s)"
        }
        values = {
            '0' : self.pluArt,
            '1' : self.eanArt,
            '2' : self.descriptionArt,
            '3' : self.supplierArt,
            '4' : self.refArt,
            '5' : self.departmentsArt
        }
        valores = (self.pluArt , self.eanArt, self.descriptionArt, self.supplierArt, self.refArt , self.departmentsArt)
        con = []
        for i in valores:
            if i != '%%' :
                j = True
            else :
                j = False
            con.append(j)
        n = 0
        dictFinal = []

        for i in con:
            if i == True:
                dictFinal.append(n)
                n += 1
            else:
                n += 1
        
        if len(dictFinal)  == 6:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[3:4]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[4:5]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[5:6]).replace('[','').replace(']', '')] 
        elif  len(dictFinal)== 5:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[3:4]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[4:5]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 4:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or "+ query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " or "+ query[str(dictFinal[3:4]).replace('[','').replace(']', '')]
        elif  len(dictFinal) == 3:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " or " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] 
        elif  len(dictFinal) == 2:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " or " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 1:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')]  

        self.valores = []
        for i in dictFinal:
            self.valores.append(values[str(i)])
        try:
            self.query = " SELECT * FROM sdbartsystem where " + string
            self.cursor.execute(self.query, list(self.valores))
        except:
            self.query = "SELECT * FROM sdbartsystem"
            self.cursor.execute(self.query)

        self.datalist = self.cursor.fetchall()
        
        self.count = 0
        for i in self.datalist:
            self.artsystem.insert('', END, values = i)
            self.count += 1
        self.lb_countArt.configure(text = f'Produtos Retornados na Pesquisa -> {self.count}')
        Dataframes.disconnectSDB(self)

    def artsytemQueryEx(self):
        self.artsystem.delete(*self.artsystem.get_children())
        Dataframes.connectSDB(self)
        self.variablesArt()

        self.fornecedorArt =  '%' + self.fornecedorArt + '%'
        self.eanArt = '%' + self.eanArt + '%'
        self.descriptionArt = '%' + self.descriptionArt + '%'
        self.pluArt = '%' + self.pluArt + '%'
        self.supplierArt = '%' + self.supplierArt + '%'
        self.departmentsArt = '%' + self.departmentsArt + '%'
        self.refArt = '%' + self.refArt + '%'

        query = {
            '0' : "(plu != '' and plu LIKE %s)",
            '1' : "(ean != '' and ean LIKE %s)",
            '2' : "(descriptions != '' and descriptions LIKE  %s)",
            '3' : "(suppliers != '' and suppliers LIKE %s)",
            '4' : "(suppliers_code != '' and suppliers_code LIKE %s)",
            '5' : "(department != '' and department LIKE %s)"
        }
        values = {
            '0' : self.pluArt,
            '1' : self.eanArt,
            '2' : self.descriptionArt,
            '3' : self.supplierArt,
            '4' : self.refArt,
            '5' : self.departmentsArt
        }
        valores = (self.pluArt , self.eanArt, self.descriptionArt, self.supplierArt, self.refArt , self.departmentsArt)
        con = []
        for i in valores:
            if i != '%%' :
                j = True
            else :
                j = False
            con.append(j)
        n = 0
        dictFinal = []
        for i in con:
            if i == True:
                dictFinal.append(n)
                n += 1
            else:
                n += 1

        if len(dictFinal)  == 6:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[3:4]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[4:5]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[5:6]).replace('[','').replace(']', '')] 
        elif  len(dictFinal)== 5:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[3:4]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[4:5]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 4:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and "+ query[str(dictFinal[2:3]).replace('[','').replace(']', '')] + " and "+ query[str(dictFinal[3:4]).replace('[','').replace(']', '')]
        elif  len(dictFinal) == 3:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')] + " and " +query[str(dictFinal[2:3]).replace('[','').replace(']', '')] 
        elif  len(dictFinal) == 2:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')] + " and " + query[str(dictFinal[1:2]).replace('[','').replace(']', '')]  
        elif  len(dictFinal) == 1:
            string = query[str(dictFinal[:1]).replace('[','').replace(']', '')]  

        self.valores = []
        for i in dictFinal:
            self.valores.append(values[str(i)])
        try:
            self.query = " SELECT * FROM sdbartsystem where " + string
            self.cursor.execute(self.query, list(self.valores))
        except:
            self.query = "SELECT * FROM sdbartsystem"
            self.cursor.execute(self.query)

        self.datalist = self.cursor.fetchall()
        self.count = 0
        for i in self.datalist:
            self.artsystem.insert('', END, values = i)
            self.count += 1
        self.lb_countArt.configure(text = f'Produtos Retornados na Pesquisa -> {self.count}')
        Dataframes.disconnectSDB(self)