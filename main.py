from Disciplina import Disciplina
from Professor import Professor
from Aluno import Aluno

p1= Professor(nome="fernando",ra="123456")
d1 = Disciplina(nome="LP2",cargaHoraria=80,mensalidade=200,professor=p1)
d2 = Disciplina(nome="LP3",cargaHoraria=80,mensalidade=200,professor=p1)
a1=Aluno(nome="Rechadson silva",email="joasjdo",ra="54321",celular="12342412",desconto=40)
a1.adicionaDiciplina(d1)
a1.adicionaDiciplina(d2)
p1.adicionaDiciplina(d1)
a1.diminuiDesconto(45)
print("valor / hora disciplina:", d1.retornaValorHora())
print("carga horaria professor",p1.retornaCargaHoraria())
print("sobrenome",a1.retornaSobrenome())
print("valor mensalidade:",a1.retornaValorMensalidade())
print("carga horaria",a1.retornaCargaHoraria())
