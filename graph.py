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
    

def first_suggestion(follow):
    """ retorna um dicionario com nome de pessoa seguida pelo follow como chave e 1 como valor """
    dicio = {x: 1 for x in graph[follow]}
    return dicio


def suggestion_update(name, follow):
    global suggestions
    
    suggestions.pop(follow, None)

    for i in graph[follow]:
        if i in graph[name]:
            continue
        elif i in suggestions:
            suggestions[i] = suggestions[i] + 1
        else:
            suggestions[i] = 1


def insert_edge(name, follow):
    """ Insere uma nova aresta no grafo, atualizando tambem o graphR e o graphRcount """
    global suggestions
    if graph.get(name):
        graph[name] = graph[name] + [follow]
        suggestion_update(name, follow)
    else:
        graph[name] = [follow]
        suggestions = first_suggestion(follow)

    if graphR.get(follow):
        graphR[follow] = graphR[follow] + [name]
        graphRcount[follow] = graphRcount[follow] + 1
    else:
        graphR[follow] = [name]
        graphRcount[follow] = 1

    return suggestions


graph = new_graph()
graphR, graphRcount = reverse_graph(graph)
suggestions = graphRcount.copy()
