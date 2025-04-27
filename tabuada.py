#!/usr/bin/env python3
"""Tabuada do 1 ao 10

Imprime a tabuada do 1 ao 10
"""
__version__ = "0.1.1"
__author__ = "VChagas"
__license__ = "Unlicense"

numeros = list(range(1, 11))

for numero in numeros:
    print("{:-^18}".format(f"Tabuada do {numero}"))
    print()
    for numero_tab in numeros:
       resultado = numero * numero_tab
       print("{:^18}".format(f"{numero} x {numero_tab} = {resultado}"))
    print("#" * 18)