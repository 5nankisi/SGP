from functions import *


while True:
    tela()

    print("1 - Iniciar Todos Processos")
    print("2 - Selecionar Processos")
    print("3 - Lista de Processos")
    print("0 - Sair")
    print("======\n")
    op = input("Opção: ")
    os.system("cls") or None

    match op:
        case "1":
            initAllProcesses()
        case "2":
            selectProcess()
        case "3":
            listProcess()
        case "0":
            break
        case _:
            print("\033[0;31mOpção invalida!!!\033[m")
