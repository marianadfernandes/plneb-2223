# exercício para definir expressões regulares

import re

def findT(text):
    return re.findall(r't', text, flags=re.IGNORECASE)

def findLetters(text):
    return re.findall(r'[a-zA-Z]+', text)

def findDigits(text):
    return re.findall(r'[0-9]+', text)

def findDecimalNumbers(text):
    return re.findall(r'[0-9]+\.[0-9]+', text)

def findWordsBiggerThan3(text):
    return re.findall(r'[a-zA-Z]{3,}', text)

def findM(text):
    return re.findall(r'(M)+', text)

def findCharacterRepeatedTwice(text):
    return re.findall(r'(.)\1', text)

def findCharacterRepeatedManyTimes(text):
    return re.findall(r'(.)\1+', text)

def putAllWordsBetweenBrackets(text):
    return re.sub(r'\b(\w+)\b', r'{\1}', text)

# -------- Menu

print(""" #### Ficha 2 ####
Definir expressões regulares que deem match a strings que:
1. Tenham um t minúsculo ou maiúsculo.
2. Tenham uma letra.
3. Tenham um digito.
4. Tenham um número decimal.
5. Tenham comprimento maior que três carateres.
6. Tenham um M mas não um m.
7. Tenham um carater repetido duas vezes.
8. Tenham apenas um carater repetido várias vezes.
9. Coloquem todas as palavras entre \{\}""")

text = input("Insira o texto a analisar.\n")

op = int(input("Insira a opção pretendida.\n"))

if op == 1:
    print(findT(text))
elif op == 2:
    print(findLetters(text))
elif op == 3:
    print(findDigits(text))
elif op == 4:
    print(findDecimalNumbers(text))
elif op == 5:
    print(findWordsBiggerThan3(text))
elif op == 6:
    print(findM(text))
elif op == 7:
    print(findCharacterRepeatedTwice(text))
elif op == 8:
    print(findCharacterRepeatedManyTimes(text))
elif op == 9:
    print(putAllWordsBetweenBrackets(text))
else:
    print("Opção inválida.")