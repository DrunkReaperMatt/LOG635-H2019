from nltk import interpret_sents
import nltk

class Scenario:

    def text(self):
        sents = ['Fido barks at Mary']
        results = interpret_sents(sents, 'grammar.fcfg')

        for result in results:
            for (synrep, symrep) in result:
                print(symrep)
