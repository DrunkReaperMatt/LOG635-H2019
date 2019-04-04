import nltk
from nltk import load_parser
from logic import *


def example(s1):
    ep = load_parser('./635/analysesyntaxique.fcfg')
    for tree in ep.parse(s1.split()):
        tree.draw()


sents = [
    'il faut une corde pour pendre personne',
    'il faut un couteau pour poignarder Black',
    'Black est à la cuisine',
    'Mustard est au salon',
    'Mustard saigne'
]


def printResults(results):
    for result in results:
        for (synrep, semrep) in result:
            # print(synrep)
            print(semrep)


noSolutionFound = True
clauses = []

clauses.append(expr("Loc(x,y) & Suspect(x) & Victime(v) & Access(x,z) & Mortpar(v,z) ==> Solution(x,y,z)"))
clauses.append(expr("Loc(x,y) & Loc(z,y) ==> Access(x,z)"))
clauses.append(expr("Saigne(x) & Instr(Couteau) ==> Mortpar(x,Couteau)"))
clauses.append(expr("Etouffer(x) & Instr(Corde) ==> Mortpar(x,Corde)"))

while noSolutionFound:
    clauses.append(expr("Victime(Mustard)"))
    clauses.append(expr("Loc(Black, Salon)"))
    clauses.append(expr("Loc(Couteau, Salon)"))
    clauses.append(expr("Saigne(Mustard)"))
    clauses.append(expr("Instr(Couteau)"))
    clauses.append(expr("Suspect(Black)"))

    crime_kb = FolKB(clauses)

    answer = fol_fc_ask(crime_kb, expr('Solution(x,y,z)'))

print('-------------------------------------------------------------------------------------')
printResults(nltk.interpret_sents(sents, './635/analysesyntaxique.fcfg'))

# example('Mustard est au salon')
print('end of program')