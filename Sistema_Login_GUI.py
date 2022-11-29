# Bibliotecas utilizadas.
import os
import time
from tkinter import *
from tkinter import messagebox

# Constantes.
absolute_path = r'D:\Force\Área de Trabalho\Programming\Python\Projetos\Login\users.txt'


def dimensionamento(janela):
    width_tela = janela.winfo_screenwidth()
    heigth_tela = janela.winfo_screenheight()

    tamx = 350
    tamy = 200
    positionx = int(width_tela/2 - tamx/2)
    positiony = int(heigth_tela/2 - tamy/2)

    janela.geometry('{}x{}+{}+{}'.format(tamx, tamy, positionx, positiony))
    janela.resizable(False, False)


def user_existe(login):
    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            for user in file:
                lista = user.split(' |')
                if login == lista[0]:
                    return True
        return False
    except:
        print('\nArquivo não encontrado.')


def cadastrar_user(login, senha):
    try:
        with open(absolute_path, 'a+', encoding='utf-8') as file:
            file.writelines(f'{login} | {senha}\n')
    except:
        print('\nNão foi possível encontrar o banco de dados.')


def new_user(login, senha):
    if login == senha:
        messagebox.showinfo('AVISO', 'Login é igual a senha, repita!')
    elif user_existe(login):
        messagebox.showinfo('AVISO', 'Usuário já cadastrado, repita!')
    else:
        cadastrar_user(login, senha)
        messagebox.showinfo('AVISO', 'Cadastro realizado com sucesso!')

    # Limpar os campos preenchidos.
    etr_senha_var.set('')
    etr_login_var.set('')


def login(login, senha):
    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            for user in file:
                lista = user.split(' | ')
                if lista[0] == login:
                    if lista[1] == f'{senha}\n':
                        messagebox.showinfo(
                            'AVISO', 'Login realizado com sucesso')
                        return 0
        messagebox.showinfo('AVISO', 'Usuário e senha não encontrado.')
    except:
        print('\nNão possível encontrar o banco de dados.')
    finally:
        # Limpar os campos preenchidos.
        etr_senha_var.set('')
        etr_login_var.set('')


janela = Tk()
dimensionamento(janela)
janela.title('Sistema de login')

# Personalização.
janela['bg'] = '#0095E4'             # Cor de fundo.
# Icone.
# janela.iconbitmap('login_icon.ico')

txt_teste = Label(janela, text='', bg='#0095E4')
txt_teste.grid(row=0, column=0, padx=25)

txt_login = Label(janela, text='Login: ', font=('Arial', 14), bg='#0095E4')
txt_login.grid(row=1, column=1, padx=5, pady=5)

# create a StringVar class
etr_login_var = StringVar()
etr_login = Entry(janela, textvariable=etr_login_var, width=17)
etr_login.grid(row=1, column=2, padx=5, pady=5)

txt_senha = Label(janela, text='Senha: ', font=('Arial', 14), bg='#0095E4')
txt_senha.grid(row=2, column=1, padx=5, pady=5)

# create a StringVar class
etr_senha_var = StringVar()
etr_senha = Entry(janela, textvariable=etr_senha_var, width=17, show='*')
etr_senha.grid(row=2, column=2, padx=5, pady=5)

btn_NewUser = Button(janela, text='Novo usuário',
                     command=lambda: new_user(etr_login.get(), etr_senha.get()))
btn_NewUser.grid(row=3, column=1, pady=20)

btn_Login = Button(janela, text='Login', command=lambda: login(
    etr_login.get(), etr_senha.get()))
btn_Login.grid(row=3, column=2)

btn_Sair = Button(janela, text='Sair', command=lambda: janela.destroy())
btn_Sair.grid(row=3, column=3)


janela.mainloop()
