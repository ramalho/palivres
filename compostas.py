#!/usr/bin/env python3

"""
compostas.py: explodir palavras compostas com ou sem hífen
"""

import pyuca
ordenador = pyuca.Collator()

with open('pt_BR.dic', encoding='cp1252') as infile:
    estimativa = infile.readline().rstrip()
    linhas = infile.readlines()

entradas = [l.split('/')[0].rstrip() for l in linhas]
conj_entradas = set(entradas)

vistas = set()
for entrada in entradas:
    if '-' in entrada or ' ' in entrada:
        partes = entrada.replace('-', ' ').split()
        novas = {p for p in partes if (p not in conj_entradas) and (p not in vistas)}
        if novas:
            #print(entrada + ':', ' '.join(novas))
            vistas.update(novas)

todas = conj_entradas | vistas
for palavra in sorted(todas, key=ordenador.sort_key):
    print(palavra)

#print(len(vistas), 'novas')
#print(len(entradas), 'entradas')
#print(len(todas), 'palavras')