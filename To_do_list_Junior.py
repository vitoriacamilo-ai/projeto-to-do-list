lista_tarefas = []
lista_tarefas_concluidas = []
tarefas_removidas = []

VERMELHO = '\033[31m'
RESET = '\033[m'


def add_tarefa():
    tarefa = str(input("Qual tarefa você deseja adicionar: ")).lower().strip()
    lista_tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")

def listar_tarefas_pendentes():
    print(f"{VERMELHO} TAREFAS PENDENTES {RESET}")
    for i, valor in enumerate(lista_tarefas):
        print(f"{VERMELHO}{i} - {valor}.{RESET}")

def marcar_concluidas():
    listar_tarefas_pendentes()
    concluir_tarefa = int(input("Qual tarefa você concluiu: "))
    if (lista_tarefas[concluir_tarefa] in lista_tarefas):
        lista_tarefas_concluidas.append(lista_tarefas[concluir_tarefa])
        lista_tarefas.remove(lista_tarefas[concluir_tarefa])
    else:
        print("Registro não econtrado!")

def remover_tarefa():
    tarefa_remover = str(input("Qual tarefa você deseja remover: ")).lower().strip()

    if (tarefa_remover not in lista_tarefas):
        print("Registro não encontrado!")
    else:
        print("Registro removido com sucesso!")
        tarefas_removidas.append(tarefa_remover)
        lista_tarefas.remove(tarefa_remover)

def listar_tarefas_concluidas():
    print("TAREFAS CONCLUÍDAS".center(20, '*'))
    for i, valor in enumerate(lista_tarefas_concluidas):
        print(f"{i} - {valor}.")

def listar_tarefas_removidas():
    print("TAREFAS REMOVIDAS".center(20, '*'))
    for i, valor in enumerate(tarefas_removidas):
        print(f"{i} - {valor}.")

while True:
    print("****** MENU TO-DO LIST - BFD ******")
    print("*" * 35)
    print("1 - Adicionar tarefa")
    print("2 - Mostrar tarefas pendentes")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Mostrar tarefas concluídas")
    print("6 - Mostrar tarefas removidas")
    print("0 - Sair")
    print('*' * 35)

    escolha = int(input("Escolha uma opção: "))

    if (escolha < 0 or escolha > 6):
        print("Escolha inválida, tente novamente.")
        continue
    if (escolha == 1):
        add_tarefa()
        continue
    if (escolha == 2):
        listar_tarefas_pendentes()
        continue
    if (escolha == 3):
        marcar_concluidas()
        continue
    if (escolha == 4 ):
        remover_tarefa()
    if (escolha == 5):
        listar_tarefas_concluidas()
    if escolha == 6:
        print("TAREFAS REMOVIDAS".center(20, '*'))
        listar_tarefas_removidas()
        continue
    if (escolha == 0):
        print("Saindo...")
        break

#FALTA COMENTAR
#TESTAR TRY - EXCEPTION
#TESTAR SWITCH CASE
#FALTA DOCUMENTAÇÃO
#REMOVER AS CONCLUIDAS DA LISTA