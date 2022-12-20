from json_storage import *
from Novelas import *


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Novelas) -> Novelas:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: Novelas) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
                self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def selecionar(self, id: int) -> Novelas | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                return dado
        return None

    def selecionar_todos(self) -> list:
        novelas = []
        for i in self.__storage.lerJson():
            novela = Novelas()
            novela.setId(i['id'])
            novela.setNome(i['nome'])
            novela.setAtores(i['atores'])
            novela.setDiretor(i['diretor'])
            novela.setGenero(i['genero'])
            novela.setClassificacao(i['classificacao'])
            novelas.append(novela)
        return novelas

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1
