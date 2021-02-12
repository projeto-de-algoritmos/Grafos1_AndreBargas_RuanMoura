#
# --- Exercicio 4 ---
#
# Para o exemplo de funcionamento do algoritimos iremos ter:
# - 7 elementos representados pelas var de 'a' a 'g'
# - Os elementos 'a', 'b' e 'g' serão de uma mesma especie, e o restando da outra especie
# - Os elementos 'g' e 'd' teram coleções incoerentes.

import ctypes

# Definindo Lista de Adjacencia Vazia para os Elementos Grafo

a = []
b = []
c = []
d = []
e = []
f = []
g = []

adj_list = [a, b, c, d, e, f, g]

def addSameCorelation(node_list, corelated_node):
    node_list.append(id(corelated_node))


# Adicionando elementos do grupo 1
addSameCorelation(a,b)
addSameCorelation(a,g)
addSameCorelation(b,a)
addSameCorelation(b,g)
addSameCorelation(g,a)
addSameCorelation(g,b)
addSameCorelation(g,c) # esta é uma relação não coerente


# Adicionando elementos do grupo 1
addSameCorelation(c,d)
addSameCorelation(c,e)
addSameCorelation(c,f)
addSameCorelation(d,c)
addSameCorelation(d,e)
addSameCorelation(d,f)
addSameCorelation(d,a) # esta é uma relação incoerente
addSameCorelation(f,c)
addSameCorelation(f,e)
addSameCorelation(f,d)
addSameCorelation(e,c)
addSameCorelation(e,d)
addSameCorelation(e,f)


# Resolvendo o numero de relações coerentes
consistent_rel = 0

for i in adj_list:
    for e in i:
        if id(i) in ctypes.cast(e, ctypes.py_object).value :
            consistent_rel += 1 


# Apresentando o resultado

print ("De um total de 20 relacoes, " + consistent_rel + " são coerentes.")
