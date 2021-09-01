from collections import deque


# поиск в ширину в графе
def wide_search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person[0] == 'p':
                print(f'Mango seller is {person}')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {}
    graph['you'] = ['alice', 'bob', 'clarie']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['clarie'] = ['tom', 'jonny']
    graph['anuj'] = []
    graph['tom'] = []
    graph['peggy'] = []
    graph['jonny'] = []

    wide_search(graph, 'you')
