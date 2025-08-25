lista_tarefas = []
tarefas_removidas = []


def add_tarefa():
    tarefa = str(input("Qual tarefa você deseja adicionar: ")).lower().strip()
    lista_tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")

def listar_tarefas_pendentes():
    print(f"***** TAREFAS *****")
    print(lista_tarefas)

def marcar_concluidas():
    concluir_tarefa = str(input("Qual tarefa você concluiu: "))
    if (concluir_tarefa in lista_tarefas):
        lista_tarefas.remove(concluir_tarefa)
        lista_tarefas.append(concluir_tarefa + "- CONCLUIDO")
    else:
        print("Registro não econtrado!")

def remover_tarefa():
    tarefa_remover = str(input("Qual tarefa você deseja remover: ")).lower().strip()

    if (tarefa_remover not in lista_tarefas):
        print("Registro não encontrado!")
        print(lista_tarefas)
    else:
        print("Registro removido com sucesso!")
        tarefas_removidas.append(tarefa_remover)
        lista_tarefas.remove(tarefa_remover)
        print("***** LISTA ATUALIZADA *****")
        print(lista_tarefas)

while True:
    print("********** MENU TO-DO LIST - BFD **********")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas pendentes")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Enumerar tarefas")
    print("0 - Sair")

    escolha = int(input("Escolha uma opção: "))

    if (escolha < 0 or escolha > 5):
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
        for i,valor in enumerate(lista_tarefas):
            print(f"{i} - {valor}.")
        continue
    if (escolha == 0):
        print("Saindo...")
        break


#FALTA COMENTAR
#TESTAR TRY - EXCEPTION
#TESTAR SWITCH CASE
#FALTA DOCUMENTAÇÃO
#REMOVER AS CONCLUIDAS DA LISTA