lista_tarefas = []
lista_tarefas_concluidas = []
tarefas_removidas = []

VERMELHO = '\033[31m'
RESET = '\033[m'
VERDE = '\033[32m'


def add_tarefa():
    tarefa = str(input("Qual tarefa você deseja adicionar: ")).lower().strip()
    lista_tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")
    print("\n")

def listar_tarefas_pendentes():
    print(f"{VERDE} TAREFAS PENDENTES {RESET}")
    for i, valor in enumerate(lista_tarefas):
        print(f"{VERDE}{i} - {valor}.{RESET}")
    print("\n")

def marcar_concluidas():
    listar_tarefas_pendentes()
    concluir_tarefa = int(input("Qual tarefa você concluiu: "))
    if (lista_tarefas[concluir_tarefa] in lista_tarefas):
        lista_tarefas_concluidas.append(lista_tarefas[concluir_tarefa])
        lista_tarefas.remove(lista_tarefas[concluir_tarefa])
    else:
        print("Registro não econtrado!")
    print("\n")

def remover_tarefa():
    listar_tarefas_pendentes()
    tarefa_remover = int(input("Qual tarefa você deseja remover: "))

    if (lista_tarefas[tarefa_remover] in lista_tarefas):
        tarefas_removidas.append(lista_tarefas[tarefa_remover])
        lista_tarefas.remove(lista_tarefas[tarefa_remover])
        print("Registro removido com sucesso!")
        print("\n")
    else:
        print("Registro não localizado!")
        print("\n")

def listar_tarefas_concluidas():
    print(f"{VERDE}TAREFAS CONCLUÍDAS{RESET}")
    for i, valor in enumerate(lista_tarefas_concluidas):
        print(f"{VERDE}{i} - {valor}.{RESET}")
    print("\n")

def listar_tarefas_removidas():
    print(F"{VERMELHO}TAREFAS REMOVIDAS{RESET}")
    for i, valor in enumerate(tarefas_removidas):
        print(f"{VERMELHO}{i} - {valor}.{RESET}")
    print("\n")

try:
    while True:
        print("****** MENU TO-DO LIST - BFD ******")
        print("*" * 35)
        print("1 - Adicionar tarefa")
        print("2 - Mostrar tarefas pendentes")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Mostrar tarefas concluídas")
        print("6 - Mostrar tarefas removidas")
        print("7 - Mostrar todas as tarefas")
        print("0 - Sair")
        print('*' * 35)

        escolha = int(input("Escolha uma opção: "))

        if (escolha < 0 or escolha > 7):
            print("Escolha inválida, tente novamente.")
        elif (escolha == 1):
            add_tarefa()
        elif (escolha == 2):
            listar_tarefas_pendentes()
        elif (escolha == 3):
            marcar_concluidas()
        elif (escolha == 4 ):
            remover_tarefa()
        elif (escolha == 5):
            listar_tarefas_concluidas()
        elif escolha == 6:
            listar_tarefas_removidas()
        elif (escolha == 7):
            print("Listar todas as tarefas")
            listar_tarefas_pendentes()
            listar_tarefas_concluidas()
            listar_tarefas_removidas()
        elif (escolha == 0):
            print("Saindo...")
            break

except ValueError:
    print("Erro! Digite um número inteiro, ou 0 para sair.")

#FALTA COMENTAR
#TESTAR SWITCH CASE
#FALTA DOCUMENTAÇÃO