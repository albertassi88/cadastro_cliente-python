

class Dados:
    def __init__(self, nome, endereco, email, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def editar(self, nome, endereco, email, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone

    def consulta(self):
        return f'{self.__nome} {self.__endereco} {self.__email} {self.__telefone}'






