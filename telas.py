import os
from Novelas import Novelas
from cores import *


def cadastrarNovela() -> Novelas:
    limparTela()
    print(bcolors.BARRAVERDE, "-------- Cadastro de Novela --------", bcolors.END)
    novela = Novelas()
    novela.setNome(input('Nome da Novela: '))
    novela.setAtores(int(input('Quantidade de Atores: ')))
    novela.setDiretor(input('Diretor da novela: '))
    novela.setGenero(input('Genero da novela: '))
    novela.setClassificacao(input('Classificacao: '))

    return novela

def editarNovela() -> Novelas:
    limparTela()
    print(bcolors.BARRABRANCO, "-------- Edição da Novela --------", bcolors.END)
    novela = Novelas()
    novela.setId(int(input('ID: ')))
    novela.setNome(input('Nome da Novela: '))
    novela.setAtores(int(input('Quantidade de Atores: ')))
    novela.setDiretor(input('Diretor da novela: '))
    novela.setGenero(input('Genero da novela: '))
    novela.setClassificacao(input('Classificacao: '))

    return novela


def excluirNovela():
    print(bcolors.BARRAVERMELHO, "-------- Exclusão de Novela --------", bcolors.END)
    limparTela()
    id = int(input('Id: '))
    return id


def selecionarNovela():
    limparTela()
    print(bcolors.BARRAMARINHO, "-------- Seleção de Novela por ID --------", bcolors.END)
    id = int(input('Id: '))
    return id


def exibirNovela(novela: Novelas):
    print(bcolors.BARRACINZA, "-------- Novelas --------", bcolors.END)
    print(f"Id: {novela.getId()}")
    print(f"Nome da novela: {novela.getNome()}")
    print(f"Quantidade de Atores: {novela.getAtores()}")
    print(f"Diretor da novela: {novela.getDiretor()}")
    print(f"Genero da novela: {novela.getGenero()}")
    print(f"Classificacao: {novela.getClassificacao()}")    

def exibirNovelas(novelas):
    limparTela()
    print(bcolors.BARRACINZA,"---------------- Novelas ----------------", bcolors.END)
    for novela in novelas:
        exibirNovela(novela)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()