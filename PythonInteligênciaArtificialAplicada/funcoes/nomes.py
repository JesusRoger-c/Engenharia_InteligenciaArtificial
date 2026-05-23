import random

#variáveis:
nome1 = "   aNa  bEaTrIz   SiLvA   "
nome2 = "cArLoS edUaRdO rOdRiGuEs"
nome3 = "MARIANA      costa      OLIVEIRA"
nome4 = "gAbRiEl sAnToS aLmEiDa"
nome5 = "  JuLiAnA sOuZa LiMa  "


#Definindo função (correção de espaços e letras) :
def corrige_texto(texto):
   nome =  " ".join(texto.upper().split())
   return nome

sala_de_aula = ["sala 1", "sala 2", "sala 3"]

def aloca_aluno(alunos, classe):
    sala = random.choice(classe)
    dict_sala_aluno = {
        "nome": alunos,
        "Sala": sala
    }
    print(dict_sala_aluno)
    return dict_sala_aluno



nome = corrige_texto(nome1)
aloca_aluno(nome, sala_de_aula)




