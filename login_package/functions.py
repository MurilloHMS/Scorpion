from tkinter import messagebox
from conference_package.conference import Conference
from dataframes.dataframe import Dataframes

class functions(Dataframes):
     def login_authentication(self):
        user = self.login_entry.get()
        password = self.password_entry.get()
        Dataframes.connectSDB(self)
        self.query = f"SELECT * FROM users WHERE username LIKE '{user}'; "
        self.cursor.execute(self.query)
        self.data = self.cursor.fetchall()
        if len(self.data) > 0:
            self.user = self.data[0][2]
            self.password = self.data[0][3].strip()

            if (user == self.user) and (password == self.password):
                self.root.destroy()
                Conference()
            elif (user == self.user) and (password != self.password):
                messagebox.showinfo(title="Authentication", message='Senha incorreta!')
            elif (user != self.user) and (password != self.password):
                messagebox.showinfo(title="Authentication", message='Usuario e senha incorretos!')
            else:
                messagebox.showinfo(title="Authentication", message='Erro de Autenticação!')
        else: 
            messagebox.showinfo(title="Authentication", message = 'Usuario não existe!')
            
        # Dataframes.disconnectSDB(self)