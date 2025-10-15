import os
from datetime import datetime

def limpar():
    os.system('cls')  # Limpar

# Cores ANSI
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'

while True:  # Loop principal
    limpar()
    pessoas = []

    print(f"{AZUL}=== CADASTRO DE 5 PESSOAS ==={RESET}")

    # Cadastro das 5 pessoas
    for i in range(5):
        print(f"\n{AMARELO}Pessoa {i+1}:{RESET}")
        nome = input("Digite o nome: ").strip().title()  # Primeira letra maiúscula
        data = input("Digite a data de nascimento (formato DD/MM/AAAA): ").strip()
        limpar()

        # Converter a data para o formato datetime
        data_nasc = datetime.strptime(data,"%d/%m/%Y")

        # Adicionar à lista
        pessoas.append({"nome": nome, "data_nasc": data_nasc})

    # Ordenar (mais velho primeiro)
    pessoas.sort(key=lambda p: p["data_nasc"])

    # Mostrar resultado
    print(f"\n{VERDE}Pessoas em ordem do mais velho para o mais novo:{RESET}\n")
    for p in pessoas:
        print(f"{AZUL}{p['nome']}{RESET} - {p['data_nasc'].strftime('%d/%m/%Y')}")

    # Pergunta se quer tentar novamente
    print()
    opcao = input(f"\n{AMARELO}Deseja tentar novamente? (S/N): {RESET}").strip().upper()
    if opcao != 'S':
        print(f"\n{VERMELHO}Programa encerrado!{RESET}")
        break