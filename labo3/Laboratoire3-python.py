import nltk
from nltk import load_parser
from logic import *


def example(s1):
    ep = load_parser('./analysesyntaxique.fcfg')
    for tree in ep.parse(s1.split()):
        tree.draw()

sents = [
        'il faut une chandelier pour bruler',
        'il faut un chandelier pour bruler Black',
        'Black est à la chambre',
        'Mustard est au salon',
        'Mustard brule'
        ]

def printResults (results):
    for result in results:
        for (synrep, semrep) in result:
            #print(synrep)
            print(semrep)



noSolutionFound = True
clauses = []

clauses.append(expr("Ind(sus,pie) & Suspect(sus,a) & Victime(v) & Mortpar(v,a) ==> Solution(sus,pie,a)"))
clauses.append(expr("Ind(x,y) & Ind(a,y) ==> Suspect(sus,a))"))
clauses.append(expr("Saigne(x) & Instr(Couteau) ==> Mortpar(x,Couteau)"))
clauses.append(expr("Bruler(x) & Instr(Chandelier) ==> Mortpar(x,Chandelier)"))
clauses.append(expr("Etouffé(x) & Instr(Corde) ==> Mortpar(x,Corde)")

while noSolutionFound :

    clauses.append(expr("Victime(Mustard)"))
    clauses.append(expr("Ind(Black, Salon)"))
    clauses.append(expr("Ind(Couteau, Salon)"))
    clauses.append(expr("Bruler(Mustard)"))
    clauses.append(expr("Instr(Chandelier)"))
    clauses.append(expr("Suspect(Black)"))

    crime_kb = FolKB(clauses)

    answer = fol_fc_ask(crime_kb, expr('Solution(x,y,z)'))
  
    
   
print('-------------------------------------------------------------------------------------')
printResults(nltk.interpret_sents(sents, './analysesyntaxique.fcfg'))

#example('Mustard est au salon')
print('end of program')
