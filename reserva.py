#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Família,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado,
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
import sys
import logging

# Configurar logger
log = logging.Logger("hotel")

# Dicionários principais
ocupados = {}
quartos = {}

# Ler reservas existentes
try:
    with open("reservas.txt", encoding="utf-8") as file:
        for linha in file:
            nome, num_quarto, dias = linha.strip().split(",")
            ocupados[int(num_quarto)] = {
                "nome": nome,
                "dias": int(dias)
            }
except FileNotFoundError:
    log.warning("Arquivo reservas.txt não existe, continuando sem reservas antigas.")

# Ler quartos disponíveis
try:
    with open("quartos.txt", encoding="utf-8") as file:
        for linha in file:
            codigo, nome, preco = linha.strip().split(",")
            codigo = int(codigo)
            preco = float(preco)
            quartos[codigo] = {
                "nome": nome,
                "preco": preco,
                "disponivel": False if codigo in ocupados else True
            }
except FileNotFoundError:
    log.error("Arquivo quartos.txt não existe")
    sys.exit(1)

# Verificar se o hotel está lotado
if all(not dados["disponivel"] for dados in quartos.values()):
    print("Hotel Lotado!")
    sys.exit(1)

# Loop principal
while True:
    print("\nReserva Hotel Pythonico")
    print("-" * 40)

    print("Lista de quartos:")
    for codigo, dados in quartos.items():
        nome_quarto = dados["nome"]
        preco = dados["preco"]
        status = "👍" if dados["disponivel"] else "⛔"
        print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {status}")
    print("-" * 40)

    nome_cliente = input("Nome do cliente: ").strip()

    try:
        num_quarto = int(input("Número do quarto: ").strip())

        if num_quarto not in quartos:
            print("O quarto escolhido não existe.")
            continue

        if not quartos[num_quarto]["disponivel"]:
            print(f"O quarto {num_quarto} já está ocupado.")
            continue
    except ValueError:
        logging.error("Número inválido, digite apenas dígitos.")
        continue

    try:
        dias = int(input("Quantos dias?: ").strip())
    except ValueError:
        logging.error("Número inválido, digite apenas dígitos.")
        continue

    nome_quarto = quartos[num_quarto]["nome"]
    preco_quarto = quartos[num_quarto]["preco"]
    total = preco_quarto * dias

    print(f"\n{nome_cliente} você escolheu o quarto {nome_quarto} e vai custar: R$ {total:.2f}")

    # Atualizar reserva no sistema
    quartos[num_quarto]["disponivel"] = False
    ocupados[num_quarto] = {
        "nome": nome_cliente,
        "dias": dias
    }

    # Gravar no arquivo de reservas
    with open("reservas.txt", "a", encoding="utf-8") as file:
        file.write(f"{nome_cliente},{num_quarto},{dias}\n")

    # Verificar se o hotel ficou lotado após esta reserva
    if all(not dados["disponivel"] for dados in quartos.values()):
        print("\nHotel agora está lotado. Todas as vagas foram preenchidas.")
        break

    # # Perguntar se deseja fazer outra reserva
    # continuar = input("\nDeseja fazer outra reserva? (s/n): ").strip().lower()
    # if continuar != "s":
    #     print("\nObrigado por usar o sistema de reservas!")
    break
