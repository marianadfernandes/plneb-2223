#! /usr/bin/env python3

import spacy 
import re

doc = """A hipótese de Cristiano Ronaldo voltar ao futebol inglês pode não estar totalmente afastada, com o portal 'Football London' a associar o português ao Chelsea. Os rumores sobre a vontade de CR7 deixar o Al Nassr já no próximo verão têm subido de tom nas últimas semanas e, se em Espanha se especula sobre uma remota chance de voltar ao Real Madrid, em Inglaterra são os blues apontados como principais interessados."""

nlp = spacy.load('pt_core_news_md')

# árvore documental
av = nlp(doc)

# .sents - frases
# .ents - entidades

dic = {}

for s in av.sents:
    print(f'* {s}')
    for ent in s.ents:
        print(f'@ {ent} | ent_type: {ent[0].ent_type_}')

    for w in s:
        print(f'word: {w.text} | lemma: {w.lemma_} | POS: {w.pos_} | tag: {w.tag_} | ent_type: {w.ent_type_} | dep: {w.dep_}')

# ex: dado um texto, ir buscar os verbos e calcular a ocorrência do lema 
        if w.pos_ == "VERB":
            if w.lemma_ not in dic:
                dic[w.lemma_] = 1
            else:
                dic[w.lemma_] += 1

    for key in dic:
        print(f'verb: {key} | count: {dic[key]}')

