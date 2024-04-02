import re

class NaturalLanguageProcessor:
    def process_sentence(self, sentence):

        sentence = re.sub(r'[^\w\s]', '', sentence.lower())
        
        sentence = sentence.replace(" então ", " → ")

        sentence = sentence.replace(" implica em ", " → ")

        sentence = sentence.replace("é equivalente a", "≡")
        sentence = sentence.replace("se e somente se", "≡")
        sentence = sentence.replace("ou", "∨")
        sentence = sentence.replace("e", "∧")
        sentence = sentence.replace("não", "¬")

        return sentence

def main():
    nlp_processor = NaturalLanguageProcessor()

    while True:
        user_input = input("Digite uma sentença em linguagem natural (ou 'exit' para sair): ")
        if user_input.lower() == 'exit':
            break
        propositional_sentence = nlp_processor.process_sentence(user_input)
        print("Sentença proposicional equivalente:", propositional_sentence)

if _name_ == "_main_":
    main()
