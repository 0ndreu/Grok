from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def person_in_search(person, search):
    for i in search:
        if person == i:
            return False
    return  True

def who_is_seller(graph):
    search_que = deque()
    search_que += graph["you"]
    searched = []

    while search_que:
        person = search_que.popleft()
        if person_in_search(person, searched):
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_que += graph[person]
                searched.append(person)
    print('There is no seller!')
    return False

print(who_is_seller(graph))