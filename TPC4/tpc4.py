import json
import re
from unidecode import unidecode

# load do ficheiro json
with open("dicionario_medico.json", encoding="UTF8") as file:
    data = json.load(file)

# criação de um dicionário para guardar os dados recebidos do ficheiro json
dic = {unidecode(term.casefold()): description for term, description in data.items()}

# leitura do ficheiro txt do livro
with open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="UTF8") as file:
    lines = file.readlines()

# separação de linha a linha por palavras + retirar acentuação e capitalização de cada palavra
pattern = re.compile(r'\W+')
normalized_words = [unidecode(word.casefold()) for line in lines for word in pattern.split(line)]

# procura dos termos presentes no texto e no dicionário 
found_words = set()
for word in normalized_words:
    if word in dic.keys():
        found_words.add(word)

# leitura do ficheiro html
with open("LIVRO-Doenças-do-Aparelho-Digestivos.html", encoding="UTF8") as file:
    lines = file.readlines()

# substituição das palavras encontradas no html pelo termo + descrição do mesmo
for i, line in enumerate(lines):
    words = line.split()
    for j, word in enumerate(words):
        normalized_word = unidecode(word.casefold())
        if normalized_word in found_words:
            exp = f"<a title='{dic[normalized_word]}'>{word}</a>"
            words[j] = re.sub(word, exp, word)
    lines[i] = " ".join(words)

# escrita do novo texto noutro ficheiro html
with open('livro_anotado.html', 'w', encoding="UTF8") as file:
    file.writelines(lines)

    