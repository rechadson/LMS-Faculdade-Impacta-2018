
class Professor:
    def __init__(self, nome="", email="", ra="", celular=""):
        self.__nome=nome
        self.__email=email
        self.__ra=ra
        self.__celular=celular
        self.__disciplinas=[]

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.novo_nome=nome
        self.__nome=self.novo_nome

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.novo_email=email
        self.__email=self.novo_email

    def getRa(self):
        return self.__ra

    def setRa(self,ra):
        self.novo_ra=ra
        self.__ra=self.__ra

    def getCelular(self):
        return self.__celular

    def setCelular(self,celular):
        self.novo_celular=celular
        self.__celular=self.novo_celular

    
    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def adicionaDiciplina(self,disciplina):
        if disciplina.getProfessor().getRa()==self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return "Professor não associado a disciplina"
    
    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()/20
        return soma_carga
        