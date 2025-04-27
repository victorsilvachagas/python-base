#!/usr/bin/env python3

"""
Programa que imprime números pares de 1 a 200

ex:
$ ./numeros_pare.py 
2
4
6
8
10
...
"""

__version__ = "0.1.0"

result = [n for n in range(1, 201) if n % 2 == 0]
print(*result, sep="\n")