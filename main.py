Lista=[]
Concluidas=[]

VERMELHO = '\033[31m'
RESET = '\033[m'

print(f"{VERMELHO} este texto vai aparecer vermelho.{RESET}")

def adicionar_tarefa():
    adicionar=str(input('Adicione a tarefa desejada: '))
    print('Sua tarefa ', adicionar, 'foi adicionada.')
    Lista.append(adicionar)



def listar_tarefas():
    print('Tarefas Pendentes:')
    for i, tarefa in enumerate(Lista, 1):
        print(f"{i}-{tarefa}")

def tarefa_concluida(): 
    print('Qual tarefa você deseja marcar como concluida? ')
    listar_tarefas()
    numero=int(input('Digite o número da tarefa já concluida: '))
    iindice= numero-1
    tarefa=Lista.pop(iindice)
    print(f'Sua tarefa {numero} foi concluida.')
    Concluidas.append(tarefa)
    print(f'Suas tarefas concluidas são: {Concluidas}')

def remover_tarefas():
    listar_tarefas()
    
    ast=int(input('Qual tarefa você deseja remover? '))
    numero= ast -1
    Lista.pop(numero)
    print(f'Sua tarefa foi removida com sucesso')
    
def lista_para_o_usuario(): 
    print("Tarefas Pendentes:")
    for i, tarefa in enumerate(Lista, 1):
        print(f"{i}- {tarefa}")
    
    print("Tarefas Concluídas:")
    for i, tarefa in enumerate(Concluidas, 1):
        print(f"{i}- {tarefa}")

while True: 
    print('Menu'.center(20))
    print('1- Adicionar tarefas')
    print('2- Listar tarefas')
    print('3- Concluir tarefas')
    print('4- Remover Tarefas-')
    print('5- Lista de todas as tarefas')
    print('6- Sair') 

    opcao=int(input('Escolha uma das opções acima: '))


    
    
    if opcao ==1:
        adicionar_tarefa()
    elif opcao ==2:
        listar_tarefas()
    elif opcao ==3:
        tarefa_concluida()
    elif opcao ==4:
        remover_tarefas()
    elif opcao ==5:
        lista_para_o_usuario()
    elif opcao ==6:
        print('Até a próxima!') 
    else:
        print('Erro, tente novamente.')
        break


