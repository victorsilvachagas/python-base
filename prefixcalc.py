#!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso: 
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.0.1"
__author__ = "VChagas"
__license__ = "Unlicense"

import sys
import os
from datetime import datetime


def calc(op, a, b):
    if op == "sum":
        return a+b
    elif op == "sub":
        return a-b
    elif op == "mul":
        return a*b
    elif op == "div":
        return a/b
    else:
        return "Operação inválida, burro!"


def main():
    if len(sys.argv) == 4:
        op = sys.argv[1]
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    else:
        op = input("Operação: ")
        a = float(input("n1: "))
        b = float(input("n2: "))

    result = calc(op, a, b)
    print(result)

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('User', 'anonymous')
    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {op},{a},{b} = {result}\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()