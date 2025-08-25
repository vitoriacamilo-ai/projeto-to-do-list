# To_do_list_Junior.py
# Desenvolvedor: Júnior
# Data: 25/08/2025
# Versão: 1.0

# Descrição: Sistema de lista de tarefas (To-Do List) simples para adicionar, listar, concluir e remover tarefas.
# Funcionalidades adicionais incluem a visualização de tarefas concluídas e removidas.
#
# Instruções de uso:
# 1. Execute o script.
# 2. Siga as instruções do menu para gerenciar suas tarefas.
# 3. Digite o número correspondente à ação desejada.
# 4. Para sair do programa, escolha a opção '0'.
#  
# Observações:
# - O sistema armazena tarefas em listas na memória durante a execução do programa. 
# - As tarefas não são persistidas em um arquivo ou banco de dados.
# - O sistema trata entradas inválidas com mensagens de erro apropriadas.
# - Cores são usadas para diferenciar tipos de tarefas na exibição.
# - Comentários foram adicionados para melhor compreensão do código.
# - Testes foram realizados para garantir o funcionamento correto das funcionalidades.
# - Documentação foi incluída para facilitar o entendimento e manutenção do código.
# - Futuras melhorias podem incluir a adição de persistência de dados e uma interface gráfica.
# - Feedbacks são bem-vindos para aprimorar o sistema.
# - Obrigado por usar o sistema de To-Do List!
# - Desenvolvido com dedicação por Júnior.
# - DOCUMENTAÇÃO:
# - Função add_tarefa: Adiciona uma nova tarefa à lista de tarefas pendentes.
# - Função listar_tarefas_pendentes: Exibe todas as tarefas pendentes.
# - Função marcar_concluidas: Marca uma tarefa como concluída, movendo-a para a lista de tarefas concluídas.
# - Função remover_tarefa: Remove uma tarefa da lista de tarefas pendentes, movendo-a para a lista de tarefas removidas.
# - Função listar_tarefas_concluidas: Exibe todas as tarefas que foram concluídas.
# - Função listar_tarefas_removidas: Exibe todas as tarefas que foram removidas.
# - Estrutura de controle principal: Um loop que exibe o menu e chama as funções apropriadas com base na escolha do usuário.


# Listas para armazenar tarefas
lista_tarefas = []
lista_tarefas_concluidas = []
tarefas_removidas = []

# Cores para formatação no terminal
VERMELHO = '\033[31m'
RESET = '\033[m'
VERDE = '\033[32m'

# Funções do sistema de To-Do List
# Função para adicionar tarefa
def add_tarefa():
    tarefa = str(input("Qual tarefa você deseja adicionar: ")).lower().strip()
    lista_tarefas.append(tarefa)
    print("Tarefa salva com sucesso!")
    print("\n")

# Função para listar tarefas pendentes
def listar_tarefas_pendentes():
    print(f"{VERDE} TAREFAS PENDENTES {RESET}")
    for i, valor in enumerate(lista_tarefas):
        print(f"{VERDE}{i} - {valor}.{RESET}")
    print("\n")

# Função para marcar tarefas como concluídas
def marcar_concluidas():
    listar_tarefas_pendentes()
    concluir_tarefa = int(input("Qual tarefa você concluiu: "))
    if (lista_tarefas[concluir_tarefa] in lista_tarefas):
        lista_tarefas_concluidas.append(lista_tarefas[concluir_tarefa])
        lista_tarefas.remove(lista_tarefas[concluir_tarefa])
    else:
        print("Registro não econtrado!")
    print("\n")

# Função para remover tarefa
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

# Função para listar tarefas concluídas
def listar_tarefas_concluidas():
    print(f"{VERDE}TAREFAS CONCLUÍDAS{RESET}")
    for i, valor in enumerate(lista_tarefas_concluidas):
        print(f"{VERDE}{i} - {valor}.{RESET}")
    print("\n")

# Função para listar tarefas removidas
def listar_tarefas_removidas():
    print(F"{VERMELHO}TAREFAS REMOVIDAS{RESET}")
    for i, valor in enumerate(tarefas_removidas):
        print(f"{VERMELHO}{i} - {valor}.{RESET}")
    print("\n")

# Loop principal do sistema
# Tratamento de exceções para entradas inválidas
try:
    # Estrutura de controle do menu com loop while
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

        # Entrada do usuário para escolha da opção
        escolha = int(input("Escolha uma opção: "))

        # Estrutura condicional para chamar as funções com base na escolha do usuário
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

# Tratamento de exceção para entradas que não são inteiros
except ValueError:
    print("Erro! Digite um número inteiro, ou 0 para sair.")
    print("Até a próxima!")
# Fim do código do sistema de To-Do List