import unidecode
import string

# ficha 1
# exercicio 1 - pergunta o nome e imprime em maiusculas

def ex1():
    nome = input("Insira o nome. ")
    print("Resultado:", nome.upper())

# exercicio 2 - recebe array de numeros e imprime pares

def pares(array):
    par = []
    for i in array:
        if i % 2 == 0:
            par.append(i)
    return par

def ex2():
    array = [int(array) for array in input("Insira vários números: ").split()]
    print("Números inseridos: ", array)

    par = pares(array)
    if len(par) == 0:        
        print("Não foram encontrados números pares.")
    else:
        for i in par:
            print("O número ", i, " é par.")

# exercicio 3 - recebe nome do ficheiro e imprime linhas do ficheiro em ordem inversa

def printLines(file):
    lines = file.readlines()
    string = ""
    for line in lines[::-1]:
        string = string + line
    return(string)

def ex3():
    file = open("teste.txt", "r", encoding="UTF8")
    print("Linhas em ordem inversa: " + printLines(file))
    file.close()

# exercicio 4 - recebe nome do ficheiro e imprime numero de ocorrencias das 10 palavras mais frequentes do ficheiro

def ordena(e):
    return e[1]

def numberOfOccurrences(file): 
    count = {}
    for line in file:
        words = line.split(" ")
        for word in words:
            if word not in count:
                count[word] = 1
            elif word in count:
                count[word] += 1
    count = sorted(count.items(), key = ordena, reverse=True)
    return count[:11]

def ex4():
    file = open("teste.txt", "r")
    for i in numberOfOccurrences(file):
        print("Palavra: ", i[0], " ocorre ", i[1], "vez(es) no ficheiro.")

# exercicio 5 - recebe texto e separa palavras e pontuação com espaços, converte para minusculas e remove acentuação de carateres

def cleanText(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, " " + i)
    return text

def ex5():
    text = input("Insira o texto a formatar. ")
    print(cleanText(text))

# exercicio 6 - criar uma função que imprime em ordem inversa, conta o numero de "a" ou "A", conta o numero de vogais, retorna tudo em maiusculas ou minusculas

def reverseString(string):
    return string[::-1]

def numberOfA(string):
    count = 0 
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "A":
            count += 1
    return count 

def numberOfVowels(string):
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            count += 1
    return count

def upperCaseString(string):
    return string.upper()

def lowerCaseString(string):
    return string.lower()

def ex6():
    string = input("Insira a string a formatar.")
    print("""Operações possiveis:
    1. Retornar a string em ordem inversa
    2. Retornar o número de carateres "a" ou "A" na string
    3. Retornar o número de vogais na string
    4. Retornar a string em maiusculas
    5. Retornar a string em minusculas.""")
    op = int(input("Operação a realizar:"))
    if op == 1:
        print(reverseString(string))
    elif op == 2:
        print(numberOfA(string))
    elif op == 3:
        print(numberOfVowels(string))
    elif op == 4:
        print(upperCaseString(string))
    elif op == 5:
        print(lowerCaseString(string))
    else:
        print("Opção inválida.")


# --------- Menu

print(""" #### Ficha 1 ####
1. Programa que pergunta ao utilizador o nome e imprime em maiúsculas.
2. Função que recebe array de números e imprime números pares.
3. Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa.
4. Função que recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro.
5. Função que recebe um texto como argumento e o "limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc.
6. Função que recebe uma string e a imprime em ordem inversa, conta o número de "a" ou "A", conta o número de vogais, retorna tudo em maiúsculas ou minúsculas.""")
op = int(input("Insira o número do exercício a resolver. "))

if op == 1:
    ex1()
elif op == 2:
    ex2()
elif op == 3:
    ex3()
elif op == 4:
    ex4()
elif op == 5:
    ex5()
elif op == 6:
    ex6()
else:
    print("Opção inválida.")

