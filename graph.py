from random import sample, randint

class Graph:

    def __init__(self):
        self.graph = self.new_graph()
        self.suggestion = self.reverse_graph()

    def randomNames(self, name, names):
        """ Retorna uma lista de 2 a 100 pessoas em names, excluindo name """
        k = randint(11, 500)
        followed_peoples = sample(names, k = k)
        if name in followed_peoples:
            followed_peoples.remove(name)
        return followed_peoples

    def new_graph(self):
        """ Gera um grafo de 10000 vertices """
        graph = {}
        file_pointer = open('names.txt')
        names = file_pointer.read().split('\n')
        while True:
            if not names[-1]:
                names.pop()
            else:
                break
        for name in names:
            graph[name] = self.randomNames(name, names)
        file_pointer.close()
        return graph

    def reverse_graph(self):
        """ Retorna um dicionario com o valor de cada grau no grafo reverso """
        graphRcount = {}
        for value in self.graph.values():
            for name in value:
                if graphRcount.get(name):
                    graphRcount[name] = graphRcount[name] + 1
                else:
                    graphRcount[name] = 1
        return graphRcount

    def first_suggestion(self, follow):
        """ atribui um dicionario com nome da pessoa seguida pelo follow como chave e 1 como valor para self.suggestion"""
        self.suggestion = {x: 1 for x in self.graph[follow]}

    def suggestion_update(self, name, follow):
        """ atualiza a lista de sugestão dado que name começou a seguir follow """
        self.suggestion.pop(follow, None)

        for i in self.graph[follow]:
            #se o vizinho do follow já é meu vizinho
            if i in self.graph[name]:
                continue
            #senão se o vizinho do follow já esta nas minhas sugestões
            elif i in self.suggestion:
                self.suggestion[i] = self.suggestion[i] + 1
            #senão 
            else:
                self.suggestion[i] = 1

    def insert_edge(self, name, follow):
        """ Insere uma nova aresta no grafo atualizando as sugestões """
        #caso name já esteja conectado com o grafo
        if self.graph.get(name):
            self.graph[name] = self.graph[name] + [follow]
            self.suggestion_update(name, follow)
        else:
            self.graph[name] = [follow]
            self.first_suggestion(follow)
            