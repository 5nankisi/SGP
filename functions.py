from classes import *
import os
import time
from random import randint


def tela():
    os.system("cls") or None
    print("=" * 20 + " Simulador de Gerência de Processador " + "=" * 20)


def initDesc_Livre():
    fila = Desc_Livre()
    fila.push(Process("Processo A0", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo B1", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo C2", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo D3", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo E4", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo F5", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo G6", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo H7", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo I8", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo J9", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo K10", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo L11", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo M12", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo N13", randint(1, 4), randint(1, 6), randint(1, 7)))
    fila.push(Process("Processo O14", randint(1, 4), randint(1, 6), randint(1, 7)))

    return fila


descLivre = initDesc_Livre()


def initAllProcesses():

    esperaCpu = Espera_Cpu()
    esperaDisco = Espera_Disco()
    esperaPrinter = Espera_Printer()

    state = False
    process = ""

    while True:
        if len(esperaCpu) < 15 and state is False:
            tela()

            print("\n\033[0;31mFila de Descritores Livres:\033[m")
            print(descLivre)

            print(f"\n\033[0;33mFila de Espera da C.P.U:\033[m")
            print(esperaCpu)

            if len(descLivre) != 0:
                process = descLivre.pop()

            esperaCpu.push(process)

            print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando o Disco:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando a Impressora:\033[m")
            print(" ")

            time.sleep(process.processTimeCpu)

        elif len(esperaCpu) >= 15 or state is True:
            state = True

            # time.sleep(1)
            process = esperaCpu.pop()

            tela()

            print("\n\033[0;31mFila de Descritores Livres:\033[m")
            print(descLivre)

            print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
            print(esperaCpu)

            print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
            print(process.processName)

            print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
            print(esperaDisco)

            print(f"\n\033[0;32mUsando o Disco:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando a Impressora:\033[m")
            print(" ")

            time.sleep(process.processTimeCpu)

            if process.processTimeCpu > 3:
                process.processTimeCpu = randint(1, 4)
                esperaCpu.push(process)

                input("O processo levou mais de 4 segundos para ser executado...")
            else:
                esperaDisco.push(process)

            if len(esperaDisco) == 15:
                tela()

                print("\n\033[0;31mFila de Descritores Livres:\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                print(esperaDisco)

                print(f"\n\033[0;32mUsando o Disco:\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando a Impressora:\033[m")
                print(" ")

                break

    time.sleep(1)

    while True:
        if len(esperaCpu) < 15 and state is True:
            # time.sleep(1)
            process = esperaDisco.pop()

            tela()

            print("\n\033[0;31mFila de Descritores Livres:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
            print(esperaCpu)

            print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
            print(esperaDisco)

            print(f"\n\033[0;32mUsando o Disco:\033[m")
            print(process.processName)

            print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando a Impressora:\033[m")
            print(" ")

            time.sleep(process.processTimeDisc)

            esperaCpu.push(process)
        else:
            state = False

            # time.sleep(1)
            if len(esperaCpu) != 0:
                process = esperaCpu.pop()

            tela()

            print("\n\033[0;31mFila de Descritores Livres:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
            print(esperaCpu)

            print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
            print(process.processName)

            print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando o Disco:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
            print(esperaPrinter)

            print(f"\n\033[0;32mUsando a Impressora:\033[m")
            print(" ")

            time.sleep(process.processTimeCpu)

            esperaPrinter.push(process)

            if len(esperaPrinter) == 15:
                tela()

                print("\n\033[0;31mFila de Descritores Livres:\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando o Disco:\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                print(esperaPrinter)

                print(f"\n\033[0;32mUsando a Impressora:\033[m")
                print(" ")

                break

    time.sleep(1)

    while True:
        if len(descLivre) < 15:

            if len(esperaPrinter) != 0:
                process = esperaPrinter.pop()

            tela()

            print("\n\033[0;31mFila de Descritores Livres:\033[m")
            print(descLivre)

            print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
            print(" ")

            print(f"\n\033[0;32mUsando o Disco:\033[m")
            print(" ")

            print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
            print(esperaPrinter)

            print(f"\n\033[0;32mUsando a Impressora:\033[m")
            print(process.processName)

            time.sleep(process.processTimePrinter)

            descLivre.push(process)

            if len(descLivre) == 15:
                tela()

                print("\n\033[0;31mFila de Descritores Livres:\033[m")
                print(descLivre)

                print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando o Disco:\033[m")
                print(" ")

                print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                print(" ")

                print(f"\n\033[0;32mUsando a Impressora:\033[m")
                print(" ")

                break

    i = input("Pressione qualquer tecla para fechar o programa: ")


def selectProcess():
    tela()
    print("===>>>" * 5 + " Lista de Todos os Processos " + "<<<===" * 5)

    for i in range(len(descLivre)):
        print(f"{i} - {descLivre[i].processName}")

    selected_desc = Desc_Livre()
    esperaCpu = Espera_Cpu()
    esperaDisco = Espera_Disco()
    esperaPrinter = Espera_Printer()

    state = False
    process = ""

    n = 0
    index = 0
    process = ""
    state = False

    while n <= 15:
        index = int(input("\nSelecione o Processo (Digite simplesmente o nº do Processo na Lista): "))

        if index < 0 or index > 14:
            print("\033[0;31mÍndice Invalido!\033[m")

            if int(input("Deseja Parar?(0-para sim): ")) == 0:
                break
            else:
                continue
        elif len(selected_desc) != 0 and selected_desc.exists(descLivre[index].processName):
            print("\033[0;33mProcesso já Selecionado!\033[m")

            if int(input("Deseja Parar?(0-para sim): ")) == 0:
                break
            else:
                continue
        else:
            selected_desc.push(Process(descLivre[index].processName, descLivre[index].processTimeCpu, descLivre[index].processTimePrinter, descLivre[index].processTimeDisc))
            state = True

            print("\033[0;32mProcesso Selecionado com Sucesso!\033[m")

            if int(input("Deseja Parar?(0-para sim): ")) == 0:
                break

            n += 1

    if state:
        print(selected_desc)

        lenSelectedList = len(selected_desc)

        execute = int(input("\nDesejar executar os Processos selecionados?(1-para sim): "))

        if execute == 1:
            state = False
            i = 0

            while True:
                if i < lenSelectedList and state is False:
                    tela()

                    print("\n\033[0;31mFila de Descritores Livres:\033[m")
                    print(selected_desc)

                    print(f"\n\033[0;33mFila de Espera da C.P.U:\033[m")
                    print(esperaCpu)

                    if len(selected_desc) != 0:
                        process = selected_desc.pop()

                    esperaCpu.push(process)

                    print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando o Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando a Impressora:\033[m")
                    print(" ")

                    time.sleep(process.processTimeCpu)

                    i += 1

                elif len(esperaCpu) >= lenSelectedList or state is True:
                    state = True

                    # time.sleep(1)
                    process = esperaCpu.pop()

                    tela()

                    print("\n\033[0;31mFila de Descritores Livres:\033[m")
                    print(selected_desc)

                    print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                    print(esperaCpu)

                    print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                    print(process.processName)

                    print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                    print(esperaDisco)

                    print(f"\n\033[0;32mUsando o Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando a Impressora:\033[m")
                    print(" ")

                    time.sleep(process.processTimeCpu)

                    if process.processTimeCpu > 3:
                        process.processTimeCpu = randint(1, 4)
                        esperaCpu.push(process)

                        input("O processo levou mais de 4 segundos para ser executado...")
                    else:
                        esperaDisco.push(process)

                    if len(esperaDisco) == lenSelectedList:
                        tela()

                        print("\n\033[0;31mFila de Descritores Livres:\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                        print(esperaDisco)

                        print(f"\n\033[0;32mUsando o Disco:\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando a Impressora:\033[m")
                        print(" ")

                        break

            time.sleep(1)

            while True:
                if len(esperaCpu) < lenSelectedList and state is True:
                    # time.sleep(1)
                    process = esperaDisco.pop()

                    tela()

                    print("\n\033[0;31mFila de Descritores Livres:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                    print(esperaCpu)

                    print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                    print(esperaDisco)

                    print(f"\n\033[0;32mUsando o Disco:\033[m")
                    print(process.processName)

                    print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando a Impressora:\033[m")
                    print(" ")

                    time.sleep(process.processTimeDisc)

                    esperaCpu.push(process)
                else:
                    state = False

                    # time.sleep(1)
                    if len(esperaCpu) != 0:
                        process = esperaCpu.pop()

                    tela()

                    print("\n\033[0;31mFila de Descritores Livres:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                    print(esperaCpu)

                    print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                    print(process.processName)

                    print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando o Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                    print(esperaPrinter)

                    print(f"\n\033[0;32mUsando a Impressora:\033[m")
                    print(" ")

                    time.sleep(process.processTimeCpu)

                    esperaPrinter.push(process)

                    if len(esperaPrinter) == lenSelectedList:
                        tela()

                        print("\n\033[0;31mFila de Descritores Livres:\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando o Disco:\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                        print(esperaPrinter)

                        print(f"\n\033[0;32mUsando a Impressora:\033[m")
                        print(" ")

                        break

            time.sleep(1)

            while True:
                if len(selected_desc) < lenSelectedList:

                    if len(esperaPrinter) != 0:
                        process = esperaPrinter.pop()

                    tela()

                    print("\n\033[0;31mFila de Descritores Livres:\033[m")
                    print(selected_desc)

                    print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;32mUsando o Disco:\033[m")
                    print(" ")

                    print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                    print(esperaPrinter)

                    print(f"\n\033[0;32mUsando a Impressora:\033[m")
                    print(process.processName)

                    time.sleep(process.processTimePrinter)

                    selected_desc.push(process)

                    if len(selected_desc) == lenSelectedList:
                        tela()

                        print("\n\033[0;31mFila de Descritores Livres:\033[m")
                        print(selected_desc)

                        print(f"\n\033[0;33mFila de Espera da C.P.U.:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando C.P.U. (Executando Processo):\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera do Disco:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando o Disco:\033[m")
                        print(" ")

                        print(f"\n\033[0;33mFila de Espera da Impressora:\033[m")
                        print(" ")

                        print(f"\n\033[0;32mUsando a Impressora:\033[m")
                        print(" ")

                        break

    i = input("\n\nPressione qualquer tecla para fechar o programa: ")


def listProcess():
    tela()
    print("===>>>" * 5 + " Lista de Todos os Processos " + "<<<===" * 5, "\n")

    print(f"{'_' * 27:<27}|{'_' * 24:^24}|{'_' * 24:^24}|{'_' * 19:>19}")
    print(f"{'Nome do Processo':<27}|{'Tempo na C.P.U.':^24}|{'Tempo no Disco':^24}|{'Tempo na Impressora':^19}")
    print(f"{'_'*27:<27}|{'_'*24:^24}|{'_'*24:^24}|{'_'*19:>19}")

    for i in range(0, 10):
        print(f"{descLivre[i].processName:<27}|{descLivre[i].processTimeCpu:^24}|{descLivre[i].processTimeDisc:^24}|{descLivre[i].processTimePrinter:^19}")
        print(f"{'_' * 27:<27}|{'_' * 24:^24}|{'_' * 24:^24}|{'_' * 19:>19}")

    for i in range(10, len(descLivre)):
        print(f"{descLivre[i].processName:<27}|{descLivre[i].processTimeCpu:^24}|{descLivre[i].processTimeDisc:^24}|{descLivre[i].processTimePrinter:^19}")
        print(f"{'_' * 27:<27}|{'_' * 24:^24}|{'_' * 24:^24}|{'_' * 19:>19}")

    i = input("\n\nPressione qualquer tecla para fechar o programa: ")
