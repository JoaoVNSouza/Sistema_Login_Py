# Bibliotecas utilizadas.
import os
import time
from getpass import getpass
import stdiomask
from colorama import Fore, Back, Style


# Menu de opções.
def exibir_menu():
    '''
    Mostra um menu com as opções para o usuário escolher.
    [1] Novo usuário.
    [2] Login.
    [3] Sair.

    Parameters:

    Returns:
        opção escolhida.
    '''

    while True:
        os.system('cls')
        print(Fore.WHITE + '''    Bem-vindo ao sistema de login:
    [1] Novo usuário.
    [2] Login.
    [3] Sair.
            ''')

        try:
            opc = int(input('    >>>> '))
        except:
            print('\nOpcão inválida, digite outro valor [1 a 3]\n')
        else:
            if opc < 1 or opc > 3:
                print('\nOpcão inválida, digite outro valor [1 a 3]\n')
            else:
                return opc

        time.sleep(1)  # Aguarda 1 segundos.


def login_senha():
    '''
    Utilizado para pegar o nome de usuário e senha.

    Parameters:

    Returns:
    login e senha.
    '''
    login = input('Usuário: ')
    senha = stdiomask.getpass(prompt='Senha: ', mask='*')

    return login, senha


def user_existe(login):
    '''
        Verifica se o usuário já está cadastrado no sistema.

        Parameters:

        Returns:
        True -> Já existe.
        False -> Não existe.
    '''
    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            for user in file:
                lista = user.split(' |')
                if login == lista[0]:
                    return True
        return False
    except:
        print('\nArquivo não encontrado.')


def novo_user(login, senha):
    if login == senha:
        print(Fore.RED + '\nLogin e senha são iguais, Repita!')
    elif user_existe(login):
        print(Fore.RED + '\nUsuário já existe cadastrado')
    else:
        try:
            with open(absolute_path, 'a+', encoding='utf-8') as file:
                file.writelines(f'{login} | {senha}\n')
            print(Fore.GREEN + '\nCadastro realizado com sucesso.')
        except:
            print('\nArquivo não foi encontrado')


def login_user(login, senha):
    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            for user in file:
                lista = user.split(' | ')
                if lista[0] == login:
                    if (lista[1].split('\n'))[0] == senha:
                        print(Fore.GREEN + '\nUsuário autenticado, acesso liberado')
                        return True
        print(Fore.RED + '\nUsuário não autenticado, revise seu login e senha')
    except:
        print('\nArquivo não encontrado')


while True:
    opc = exibir_menu()
    os.system('cls')
    if opc == 1 or opc == 2:
        login, senha = login_senha()
        absolute_path = r'D:\Force\Área de Trabalho\Programming\Python\Projetos\Login\users.txt'

        if opc == 1:
            novo_user(login, senha)
        else:
            c = login_user(login, senha)
            if c == True:
                break
    else:
        exit()

    time.sleep(2)
