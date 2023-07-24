import mysql.connector
import psycopg2
from sqlalchemy import create_engine

from dados.data import Data

class Dataframes(Data):
    def connectSDB(self):
        return self.connect()
         
    
    def disconnectSDB(self):
        self.conn.close() 
    
    def createUserTable(self):
        self.connectSDB()
        self.cursor.execute(''' 
         CREATE TABLE IF NOT EXISTS users(
            id serial,
            name varchar(255) NOT NULL,
            username varchar(255) NOT NULL PRIMARY KEY  ,
            password varchar(12) NOT NULL);''')
        self.conn.commit()

    def createTables(self):
            self.connectSDB()
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS nfedata(
                id serial,
                referenceARCHAR(100) NOT NULL,
                ean VARCHAR(20) NOT NULL,
                eantributed VARCHAR(20) NOT NULL,
                description VARCHAR (255) NOT NULL,
                amount VARCHAR(20) NOT NULL,
                realcost DOUBLE NOT NULL,
                costcalculate DOUBLE NOT NULL,
                unitvalue DOUBLE NOT NULL,
                totalvalue DOUBLE NOT NULL,
                tipe VARCHAR(20) NOT NULL,
                cfop VARCHAR(20) NOT NULL,
                ncm VARCHAR(25) NOT NULL,
                cst VARCHAR(10) NOT NULL,
                icmsbase DOUBLE NOT NULL,
                aliqicms DOUBLE NOT NULL,
                icmsvalue DOUBLE NOT NULL,
                aliqipi DOUBLE NOT NULL,
                ipivalue DOUBLE NOT NULL,
                ivamvavalue DOUBLE NOT NULL,
                aliqicmst DOUBLE NOT NULL,
                icmstbase DOUBLE NOT NULL,
                icmstvalue DOUBLE NOT NULL,
                aliqpis DOUBLE NOT NULL,
                pisvalue DOUBLE NOT NULL,
                aliqcoffins DOUBLE NOT NULL,
                coffinsvalue DOUBLE NOT NULL,
                aliqfrete DOUBLE NOT NULL,
                fretevalue DOUBLE NOT NULL);
            ''')
            self.conn.commit(); 

    def createSuppliersTable(self):
        self.connectSDB()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers_information(
            id serial,
            supplier CHAR(255) NOT NULL,
            cnpj_supplier CHAR(100) NOT NULL ,
            access_Key CHAR(100) NOT NULL,
            nfe_num CHAR(100) NOT NULL,
            emission_date DATE NOT NULL,
            icmsbase DOUBLE NOT NULL,
            icmsvalue DOUBLE NOT NULL ,
            basest DOUBLE NOT NULL, 
            stvalue DOUBLE NOT NULL,
            fretevalue DOUBLE NOT NULL , 
            securityvalue DOUBLE NOT NULL,
            discontvalue DOUBLE NOT NULL,
            otherDispenses DOUBLE NOT NULL,
            extradispenses DOUBLE NOT NULL,
            ipivalue DOUBLE NOT NULL,
            productsvalue DOUBLE NOT NULL,
            nfevalue DOUBLE NOT NULL,
            nfevaluewithfrete DOUBLE NOT NULL,
            cnpjloja char(100) NOT NULL,
            loja char(255) NOT NULL,
            duplicates char(100) NOT NULL);
        ''' )
        self.conn.commit()

    def createNFeInfoTables(self):
        self.connectSDB()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS NFINFO(
            NFINDEX VARCHAR(255) NOT NULL PRIMARY KEY,
            NFFORS VARCHAR(255) NOT NULL,
            NFFOCNPJ VARCHAR(255) NOT NULL,
            NFNUM VARCHAR(255) NOT NULL,
            NFRSLOJ VARCHAR(255) NOT NULL,
            NFLOJCNPJ VARCHAR(255) NOT NULL,
            NFBICMS DOUBLE NOT NULL,
            NFVICMS DOUBLE NOT NULL,
            NFBST DOUBLE NOT NULL,
            NFVST DOUBLE NOT NULL,
            NFVFRETE DOUBLE NOT NULL,
            NFVSEG DOUBLE NOT NULL,
            NFVDES DOUBLE NOT NULL,
            NFODES DOUBLE NOT NULL,
            NFVIPI DOUBLE NOT NULL,
            NFKEY VARCHAR(255) NOT NULL,
            NFDENT TIMESTAMP,
            NFDLIB TIMESTAMP,
            NFDEMI DATE,
            NFVTOTPROD DOUBLE NOT NULL,
            NFVTOTNFE DOUBLE NOT NULL,
            NFIDOP VARCHAR(255),
            NFSTATUS VARCHAR(255) NOT NULL);
        ''')
        self.conn.commit()

    def createTablefiltro(self):
        self.connectSDB()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS nfedatainformations(
            id CHAR(255) NOT NULL,
            reference char(100) NOT NULL,
            ean char(20) NOT NULL,
            eantributed char(20) NOT NULL,
            description char (255) NOT NULL,
            amount char(20) NOT NULL,
            realcost DOUBLE NOT NULL,
            costcalculate DOUBLE NOT NULL,
            unitvalue DOUBLE NOT NULL,
            totalvalue DOUBLE NOT NULL,
            tipe char(20) NOT NULL,
            cfop char(20) NOT NULL,
            ncm char(25) NOT NULL,
            cst char(10) NOT NULL,
            icmsbase DOUBLE NOT NULL,
            aliqicms DOUBLE NOT NULL,
            icmsvalue DOUBLE NOT NULL,
            aliqipi DOUBLE NOT NULL,
            ipivalue DOUBLE NOT NULL,
            ivamvavalue DOUBLE NOT NULL,
            aliqicmst DOUBLE NOT NULL,
            icmstbase DOUBLE NOT NULL,
            icmstvalue DOUBLE NOT NULL,
            aliqpis DOUBLE NOT NULL,
            pisvalue DOUBLE NOT NULL,
            aliqcoffins DOUBLE NOT NULL,
            coffinsvalue DOUBLE NOT NULL,
            aliqfrete DOUBLE NOT NULL,
            fretevalue DOUBLE NOT NULL,
            nfenum char(255) NOT NULL, 
            fornecedor CHAR(255) NOT NULL, 
            cnpjforn CHAR(255) NOT NULL, 
            lojaentrada CHAR(255) NOT NULL, 
            cnpjlojaentrada CHAR(255) NOT NULL,
            keynfe char(255) NOT NULL,
            frete_value DOUBLE NOT NULL);
        ''')
        self.conn.commit()

    def createTable(self):
        self.connectSDB()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sngc(
            empresas CHAR(255) PRIMARY KEY NOT NULL,
            vendas_totais real NOT NULL,
            valor_sat real NOT NULL,
            declarado real NOT NULL,
            falta_declarar real NOT NULL,
            valor_declarado_a_mais real NOT NULL
        ); ''')
        self.conn.commit()


    def tableArtsysSQL(self):
        self.connectSDB()
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS sdbartsystem(
            plu INTEGER,
            descriptions varchar(255), 
            ncm varchar(255),
            ean varchar(255),
            department varchar(255),
            cost DOUBLE,
            cost_and_taxes DOUBLE,
            sale DOUBLE,
            suppliers_code varchar(255),
            suppliers varchar(255));
        ''')
        self.conn.commit()



    def createTablesWithSQL(self):
        self.createTables()
        self.createSuppliersTable()
        self.createNFeInfoTables()
        self.createTablefiltro()
        self.createTable()
        self.tableArtsysSQL()
        self.createUserTable()
