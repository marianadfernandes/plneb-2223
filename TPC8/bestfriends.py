#! /usr/bin/env python3

import spacy 
import re
from collections import Counter
import sys

nlp = spacy.load('pt_core_news_md')
nlp.max_length = 1300000

file = sys.argv[1]

file = open(file, 'r', encoding='utf8')

book = file.read()

av = nlp(book)

names = []
for s in av.sents:
    for ent in s.ents:
        if ent[0].ent_type_ == 'PER':
            names.append((ent.text))

pairs = []
for i in range(len(names)):
    for j in range(i+1, len(names)):
        if names[i] != names[j]:
            pairs.append((names[i], names[j]))

personagens = Counter(pairs)
for pair, freq in personagens.items():
    if freq > 2:
        print(pair, freq)
