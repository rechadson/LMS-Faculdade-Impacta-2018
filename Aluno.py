class Aluno:
    def __init__(self, nome="", email="", ra="", celular="",desconto=0.0):
        self.__nome=nome
        self.__email=email
        self.__ra=ra
        self.__desconto=desconto
        self.__disciplina = []

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email = email

    def getRa(self):
        return self.__ra

    def setRa(self,ra):
        self.__ra = ra

    def getCelular(self):
        return self.__celular

    def setCelular(self,celular):
        self.__celular = celular
    def getDesconto(self):
        return self.__desconto

    def setDesconto(self,desconto):
        self.__desconto = desconto
    
    def getDisciplina(self):
        return self.__disciplina

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])
    
    def adicionaDiciplina(self,disciplina):
        self.__disciplina.append(disciplina)

    def aumentarDesconto(self,desconto):
        if desconto > self.__desconto:
            self.__desconto = desconto
        else:
            return print("Desconto inserido é menor que desconto atual")
    def diminuiDesconto(self,desconto):
        if desconto < self.__desconto:
            self.__desconto = desconto
        else:
            return print("Desconto inserido é maior que desconto atual")
    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplina:
            soma_carga += d.getCargaHoraria()
        return soma_carga

    def retornaValorMensalidade(self):
        soma_mensalidade = 0
        for m in self.__disciplina:
            soma_mensalidade += m.getMensalidade()
        return soma_mensalidade-(soma_mensalidade*(self.__desconto/100))

        