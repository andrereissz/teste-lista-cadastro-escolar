import os
from colorama import Fore, Back, Style


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def header():
    clearConsole()
    print(f"{' ESCOLA TESTE ':=^60}\n")


alunos = []
alunosid = []
reset = Fore.RESET+Back.RESET+Style.NORMAL
selecionado = Fore.BLACK+Back.YELLOW+Style.BRIGHT
while True:
    header()
    opc = str(input(f"{'[ 1 ] Cadastrar aluno':^60}\n{'[ 2 ] Ver lista de alunos':^60}\n{'[ 3 ] Desmatricular aluno':^60}\n{'[ 4 ] Sair':^60}\n\nDigite sua opção: "))
    if opc not in '1234':
        header()
        input('Opção inválida tente novamente...')
        continue
    else:
        if opc == '1':
            while True:
                header()
                print(f"{'[ 1 ] Cadastrar aluno':^60}\n")
                id = int(input('Digite o id do aluno: '))
                if id in alunosid:
                    input('ID já cadastrado tente novamente...')
                    continue
                else:
                    alunosid.append(id)
                    alunos.append(input('Digite o nome do aluno: ').capitalize().strip())
                    break
        elif opc == '2':
            header()
            if len(alunosid) == 0:
                print(f"{'[ 2 ] Ver lista de alunos':^60}\n")
                input(f"{Fore.RED+Back.BLACK} {'Não há alunos cadastrados...':^60} {reset}")
            else:
                print(f"{'[ 2 ] Ver lista de alunos':^60}\n")
                for n in range(len(alunosid)):
                    print(f'{alunosid[n]} - {alunos[n]}')
                input('\nAperte enter para retornar...')
        elif opc == '3':
            header()
            print(f"{'[ 3 ] Desmatricular aluno':^60}\n")
            val = int(input('Digite o ID para descadastrar: '))
            if val not in alunosid:
                input('ID não encontrado...')
            else:
                for n in range(len(alunosid)): # n para encontrar o index dos alunos nas respectivas listas
                    if val == alunosid[n]:
                        while True:
                            header()
                            print(f"{'[ 3 ] Desmatricular aluno':^60}\n")
                            print(f'{selecionado} {alunosid[n]} - {alunos[n]} {reset}\n')
                            opc2 = str(input(f"Deseja deletar a matrícula?\n\n{'[ 1 ] Confirmar':^60}\n{'[ 2 ] Cancelar ':^60}\n\nDigite sua opção: "))
                            if opc2 not in '12':
                                input('Opção inválida tente novamente...')
                                continue
                            else:
                                if opc2 == '1':
                                    header()
                                    print(f"{'[ 3 ] Desmatricular aluno':^60}\n")
                                    input(f"{alunosid[n]} - {alunos[n]} será deletado\n\nAperte enter para retornar...")
                                    alunos.remove(alunos[n])
                                    alunosid.remove(alunosid[n])
                                    break
                                else:
                                    header()
                                    print(f"{'[ 3 ] Desmatricular aluno':^60}\n")
                                    input(f"{alunosid[n]} - {alunos[n]} será mantido\n\nAperte enter para retornar...")
                                    break
                        break
        else:
            header()
            print(f"{'[ 4 ] Sair':^60}\n")
            while True:
                opc3 = str(input(f"{'Você tem certeza??':^60}\n\n{'[ 1 ] Sair':^60}\n{'[ 2 ] Retornar':^60}\n\nDigite sua opção: "))
                if opc3 not in '12':
                    input('Opção invalida tente novamente...')
                    continue
                else:
                    break
            if opc3 == '1': 
                break
            else:
                continue
clearConsole()
