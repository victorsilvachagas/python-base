#!/usr/bin/env python3

"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
lista_palavras = []
vogais = "aeiou"

while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").lower().strip()

    if not palavra:
        print(*lista_palavras, sep="\n")
        break
    
    palavra = ''.join([letra*2 if letra in vogais else letra for letra in palavra])
    lista_palavras.append(palavra)

