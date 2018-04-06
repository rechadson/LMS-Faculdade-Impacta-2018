class Disciplina:
    def __init__(self, nome="", cargaHoraria=0,mensalidade=0.0,professor=""):
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__mensalidade = mensalidade
        self.__professor = professor
    
    
    def getNome(self):
        return self.__nome

    def getMensalidade(self):
        return self.__mensalidade

    def getCargaHoraria(self):
        return self.__cargaHoraria 
    
    def getProfessor(self):
        return self.__professor

    def setCargaHoraria(self,cargaHoraria):
        if self.__cargaHoraria>=0 and self.__cargaHoraria<=40:
            if cargaHoraria >=0 and cargaHoraria <=0:
                self.nova_cargaHoraria=cargaHoraria
                self.__cargaHoraria=self.nova_cargaHoraria
    
    def setNome(self,nome):
        self.__nome=nome
    
    def setMensalidade(self,mensalidade):
        self.__mensalidade = mensalidade
    
    def setProfessor(self,professor):
        self.__professor = professor
    
    def retornaValorHora(self):
        valor = self.__mensalidade * 6 / self.__cargaHoraria
        return valor