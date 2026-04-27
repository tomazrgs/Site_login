import os
import random

class Usuario: 
    def __init__(self,ID= '', login='', senha='',adm= False): 
        self._ID = ID 
        self.login = login 
        self._senha = senha
        self._adm = adm

    def to_dict(self): 
        return { 
            "ID": self._ID, 
            "login": self.login, 
            "senha": self._senha, 
            "adm":self._adm
            } 
    
    @classmethod 
    def from_dict(cls, dados): 
        return cls( 
            dados['ID'], 
            dados['login'], 
            dados['senha'],
            dados['adm'],
           
        )

    def __repr__(self): 
        return f'ID: {self._ID}, Usuario: {self.login}, Senha: {self._senha}' 
        
    @property 
    def ativar(self): 
        return 'Status da conta: ☑' if self._adm else 'Status da conta: ☐' 
        
    def promover(self): 
        self._adm = not self._adm 
            


class Contas: 
    def __init__(self): 
        self.lista = []

    def adduser(self,obj_usuario): 
        assert isinstance(obj_usuario, Usuario)
        self.lista.append(obj_usuario)
        
    def listar(self): 
        for u in self.lista: 
            print(u)

    def verifi_adm(self,usuario):
        for login in self.lista:
            if login.login == usuario.login and login.adm == True:
                return True
        return False

    def verifi_exist(self,user): 
        for login in self.lista: 
            if login.login == user: 
                return True
        return False
    
    def verifi_login(self, user, senha):
        for login in self.lista:
            if login.login == user and login.senha == senha:
                return True
        return False