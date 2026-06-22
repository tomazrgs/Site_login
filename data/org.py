class Usuario:
    def __init__(self, ID, login, senha, role = 'user'):
        self.ID = ID
        self.login = login
        self._senha = senha
        self._role = role

    def __repr__(self):
        return f'ID: {self.ID}, Usuario: {self.login}, Senha: {self._senha}, Role: {self._role}'
    
    def to_dict(self):
        return {
            "ID": self.ID,
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
                dados['role']
        )

    def troca_senha(self,user, senha):
        if self.login == user and self._senha == senha:
            nova_senha = input('Informe a senha')
            self._senha = nova_senha
            return True
        return False
    
    def promover(self, user):
        if user == True and self.login['role'] != 'adm':
            self.login['role'] = 'adm'
            return True
        else: return False 


    # @property
    # def ativar(self):
    #     return 'Status da conta: ☑' if self._role else 'Status da conta: ☐'
    


class Contas():
    def __init__(self,):
        self.lista = []

    def adduser(self,obj_usuario):
        assert isinstance(obj_usuario, Usuario)
        self.lista.append(obj_usuario)

    def listar(self):
        for u in self.lista:
            print(u)

    def verifica_existencia(self,user):
        for login in self.lista:
            if login.login == user:
                return True
        return False
    
    def informa_role(self,user):
        for login in self.lista:
            if login.login == user:
                return login._role
        
    
    def verifica_login(self, user , senha):
        for login in self.lista:
            if login.login == user and login._senha == senha:
                return login
        return False

if __name__ == '__main__':
    pass
