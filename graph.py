from random import sample, randint

def randomNames(name, names):
    """ Retorna uma lista de 2 a 100 pessoas em names, excluindo name """
    k = randint(2, 100)
    # k = randint(2, 10)
    followed_peoples = sample(names, k = k)
    if name in followed_peoples:
        followed_peoples.remove(name)
    return followed_peoples


def new_graph():
    """ Gera um grafo de 10000 vertices """
    graph = {}
    file_pointer = open('names.txt')
    # file_pointer = open('names_test.txt')
    names = file_pointer.read().split('\n')
    while True:
        if not names[-1]:
            names.pop()
        else:
            break
    print(names)
    for name in names:
        graph[name] = randomNames(name, names)
    file_pointer.close()
    return graph


def reverse_graph(graph):
    """ Retorna 2 dicionarios, um sendo o grafo reverso e o outro sendo o grau de cada vertice no grafo reverso """
    graphR = {}
    graphRcount = {}
    for key, value in graph.items():
        for nome in value:
            if graphR.get(nome):
                graphR[nome] = graphR[nome] + [key]
                graphRcount[nome] = graphRcount[nome] + 1
            else:
                graphR[nome] = [key]
                graphRcount[nome] = 1
    return graphR, graphRcount


def most_popular(graphRcount):
    """ Retorna uma lista decrescente de acordo com o grau, cada indice é uma tupla contendo o vertice e seu grau """
    lista = list(graphRcount.items())
    lista.sort(reverse=True, key = lambda x: x[1])
    return lista
    