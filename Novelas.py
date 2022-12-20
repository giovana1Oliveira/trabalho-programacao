class Novelas():
    __id: int
    __nome: str
    __atores: int
    __diretor: str
    __genero: str
    __classificacao: str


    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id


    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
    def getAtores(self):
        return self.__atores

    def setAtores(self, atores):
        self.__atores = atores

    def getDiretor(self):
        return self.__diretor

    def setDiretor(self, diretor):
        self.__diretor = diretor

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getClassificacao(self):
        return self.__classificacao

    def setClassificacao(self, classificacao):
        self.__classificacao = classificacao

    def toDict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'atores': self.__atores,
            'diretor': self.__diretor,
            'genero': self.__genero,
            'classificacao': self.__classificacao
        }
