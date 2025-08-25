Lista = []
Concluidas = []

VERMELHO = '\033[31m'
RESET = '\033[m'

print(f"{VERMELHO} este texto vai aparecer vermelho.{RESET}\n")

def adicionar_tarefa():
    adicionar = str(input('Adicione a tarefa desejada: '))
    Lista.append(adicionar)
    print(f"Sua tarefa '{adicionar}' foi adicionada.\n")

def listar_tarefas():
    print('\nTarefas Pendentes:')
    for i, tarefa in enumerate(Lista, 1):
        print(f"{i}- {tarefa}")
    print()  

def tarefa_concluida(): 
    print('\nQual tarefa você deseja marcar como concluída? ')
    listar_tarefas()
    numero = int(input('Digite o número da tarefa já concluída: '))
    iindice = numero - 1
    tarefa = Lista.pop(iindice)
    Concluidas.append(tarefa)
    print(f"\nTarefa '{tarefa}' concluída com sucesso!\n")

def remover_tarefas():
    print()
    listar_tarefas()
    ast = int(input('Qual tarefa você deseja remover? '))
    numero = ast - 1
    tarefa = Lista.pop(numero)
    print(f"\nTarefa '{tarefa}' foi removida com sucesso.\n")
    
def lista_para_o_usuario(): 
    print("\nTarefas Pendentes:")
    if Lista:
        for i, tarefa in enumerate(Lista, 1):
            print(f"{i}- {tarefa}")
    else:
        print("Nenhuma tarefa pendente.")

    print("\nTarefas Concluídas:")
    if Concluidas:
        for i, tarefa in enumerate(Concluidas, 1):
            print(f"{i}- {tarefa}")
    else:
        print("Nenhuma tarefa concluída.")
    print()

while True: 
    print("="*30)
    print("Menu".center(30))
    print("="*30)
    print('1- Adicionar tarefas')
    print('2- Listar tarefas')
    print('3- Concluir tarefas')
    print('4- Remover Tarefas')
    print('5- Lista de todas as tarefas')
    print('0- Sair\n') 

    opcao = int(input('Escolha uma das opções acima: '))
    print()  

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        tarefa_concluida()
    elif opcao == 4:
        remover_tarefas()
    elif opcao == 5:
        lista_para_o_usuario()
    elif opcao == 0:
        print('Até a próxima!\n') 
        break
    else:
        print('Erro, tente novamente.\n')
        break
