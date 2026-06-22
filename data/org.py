class Usuario:
    def __init__(self,ID, login, senha,role = 'user'):
        self._ID = ID
        self.login = login 
        self._senha = senha
        self._role = role

    def to_dict(self): 
        return { 
            "ID": self._ID, 
            "login": self.login, 
            "senha": self._senha, 
            "role":self._role
            } 
    
    @classmethod 
    def from_dict(cls, dados): 
        return cls( 
            dados['ID'], 
            dados['login'], 
            dados['senha'],
            dados['role'],
           
        )

    def __repr__(self): 
        return f'ID: {self._ID}, Usuario: {self.login}, Senha: {self._senha}' 
        
    @property 
    def ativar(self): 
        return 'Status da conta: ☑' if self._role else 'Status da conta: ☐'
        
    def promover(self): 
        self._role = not self._role
            


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
            if login.login == usuario.login and login.role == True:
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