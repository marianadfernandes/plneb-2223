import json
import re

with open("termos_traduzidos.txt", encoding="UTF8") as file:
    text = file.read()

words = re.findall(r'(.+)(?:@)(.+)', text)

dic = {}

for tuple in words:
    dic[tuple[0].strip()] = tuple[1].strip()

print(dic)

with open("dicionario_translation.json", "w", encoding="UTF8") as file:
    json.dump(dic, file, ensure_ascii=False, indent=4)