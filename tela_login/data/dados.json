class Usuario:
    def __init__(self, userID, login, senha, email, role = 'user'):
        self.userID = userID
        self.login = login
        self._senha = senha
        self._email = email
        self._role = role


    def __repr__(self):
        return f'userID: {self.userID}, Usuario: {self.login}, Senha: {self._senha}, Role: {self._role}'
    
    def to_dict(self):
        return {
            "userID": self.userID,
            "login": self.login,
            "senha": self._senha,
            "email": self._email,
            "role":self._role
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
                dados['userID'],
                dados['login'],
                dados['senha'],
                dados['email'],
                dados['role']
        )

    def troca_senha(self,nova_senha):
        self._senha = nova_senha
        return self

    
    def promover(self, user):
        if user == True and self.login['role'] != 'adm':
            self.login['role'] = 'adm'
            return True
        else: return False 


    # @property
    # def ativar(self):
    #     return 'Status da conta: ☑' if self._role else 'Status da conta: ☐'
    
class Contas():
    def __init__(self):
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
                return login.login
        return False

    def coleta_objeto(self,user):
        for login in self.lista:
            if login.login == user:
                return login
        return False
    
    def informa_role(self,user):
        for login in self.lista:
            if login.login == user:
                return login._role

    def verifica_login(self, user, senha):
        for login in self.lista:
            if login.login == user and login._senha == senha:
                return True
        return False

if __name__ == '__main__':
    pass
