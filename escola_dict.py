#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

from pprint import pprint

sala1 = {
    "nome": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
}

sala2 = {
    "nome": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

#listar alunos em cada atividade por sala

for materias in aulas:
    print()
    pprint(f"Alunos que fazem aula de {materias}")
    print('-'*30)

    atividade_sala1 = [aluno for aluno in sala1["nome"] if aluno in aulas[materias]]
    atividade_sala2 = [aluno for aluno in sala2["nome"] if aluno in aulas[materias]]

    pprint(atividade_sala1)
    pprint(atividade_sala2)
    print('#'*30)
    