from telas import *
from persistencia import *
from cores import *


def menu():
    limparTela()
    print(bcolors.BARRACINZA, "-------- Cadastro de Novela --------", bcolors.END)
    print(bcolors.BARRAVERDE,"1 - Cadastrar Novela", bcolors.END)
    print(bcolors.BARRAROSA,"2 - Editar informações", bcolors.END)
    print(bcolors.BARRAAMARELO,"3 - Excluir Novela", bcolors.END)
    print(bcolors.BARRAMARINHO,"4 - Selecionar Novela", bcolors.END)
    print(bcolors.BARRABRANCO,"5 - Listar Novelas", bcolors.END)
    print(bcolors.BARRAVERMELHO,"6 - Sair", bcolors.END)
    print(bcolors.BARRACINZA,"----------------------------------", bcolors.END)
    opcao = int(input("Digite a opção desejada: "))
    
    return opcao

persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        novela = cadastrarNovela()
        persistencia.criar(novela)
        exibirMsg("A novela foi cadastrada com sucesso!")

    elif opcao == 2:
        novela = editarNovela()
        persistencia.editar(novela)
        exibirMsg("A novela foi editada com sucesso!")

    elif opcao == 3:
        limparTela()
        id = excluirNovela()
        persistencia.excluir(id)
        exibirMsg("A novela foi excluída com sucesso!")

    elif opcao == 4:
        id = selecionarNovela()
        novela = persistencia.selecionar(id)
        if novela == None:
            exibirMsg("Novela não encontrada!")
        else:
            exibirNovela(novela)
            travarTela()
            
    elif opcao == 5:
        novelas = persistencia.selecionar_todos()
        exibirNovelas(novelas)

    elif opcao == 6:
        break
