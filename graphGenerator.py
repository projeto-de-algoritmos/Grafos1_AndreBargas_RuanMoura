from random import choices, randint

def randomNames(name, names):
    k = randint(2, 100)
    followed_peoples = choices(names, k = k)
    if name in followed_peoples:
        followed_peoples.remove(name)
    return followed_peoples


graph = {}
file_pointer = open('names.txt')
names = file_pointer.read().split('\n')
for name in names:
    graph[name] = randomNames(name, names)

file_pointer.close()