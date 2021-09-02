from collections import deque


# поиск в ширину в графе
def wide_search(graph, name):
    search_queue = deque()  # создаем очередь
    search_queue += graph[name]  # добавляем в очередь всех детей узла name
    searched = []  # в этот список будем добавлять всех, кото проверили
    while search_queue:  # пока очередь не пустая
        person = search_queue.popleft()  # достаем первого из очереди и проверяем, подходит он нам или нет
        if not person in searched:
            if person[0] == 'p':
                print(f'Mango seller is {person}')
                return True
            else:
                search_queue += graph[person]  # если не подходит, то добавляем в очередь всех его детей
                searched.append(person)  # добавляем узел в проверенные
    return False


# алгоритм Дейкстры - поиск наименьшего пути в взвешенном графе
# находим нод с наименьшим весом
def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs: # бежим по словарю стоимостей
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # проверяем только среди нодов, которые еще не обработали
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# разматываем итоговый путь
def get_path_back(parents, end_point):
    if end_point not in parents: # нет в родителях
        if end_point in parents.values(): # но есть в детях, значит это самое начало
            return str(get_path_back(parents, '')) + str(end_point)
        else:
            return ''
    else:
        new_end_point = parents[end_point] # новый родитель
        return str(get_path_back(parents, new_end_point)) + ' ' + str(end_point) # предыдущего родителя помещаем назад т.к. мы идем в обратном направлении


def alg_dekstry(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed) # ищем необработанный нод с наименьшим весом
    while node is not None:
        cost = costs[node] # вес нода
        neighbors = graph[node] # соседи нода

        for n in neighbors.keys():
            new_cost = cost + neighbors[n] # считаем сколько стоит добраться от этого нода до его соседей

            if costs[n] > new_cost: # если мы нашли более дешевый путь, то обновим стоимость и родителя
                costs[n] = new_cost
                parents[n] = node

        processed.append(node) # помечаем, что обработали нод
        node = find_lowest_cost_node(costs, processed)

    # итоговый лучший путь
    nodes_path = get_path_back(parents, 'end').split(' ')

    path = 0
    for i in range(len(nodes_path) - 1):
        print(f'From "{nodes_path[i]}" to "{nodes_path[i + 1]}" cost is "{graph[nodes_path[i]][nodes_path[i + 1]]}"')
        path += graph[nodes_path[i]][nodes_path[i + 1]]
    print('Total path is', path)


if __name__ == '__main__':
    # --- Поиск в ширину ---
    graph = {}
    graph['you'] = ['alice', 'bob', 'clarie']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['clarie'] = ['tom', 'jonny']
    graph['anuj'] = []
    graph['tom'] = []
    graph['peggy'] = []
    graph['jonny'] = []

    # wide_search(graph, 'you')
    # --- Поиск в ширину ---

    # --- Алгоритм Дейкстры ---
    # сам граф
    # start ---6---> a ---1---> end
    #   |            ^           ^
    #   2            3           |
    #   |            |           5
    #   b------------------------|

    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = {}
    graph['a']['end'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['end'] = 5
    graph['end'] = {}

    # стоимости
    infinity = float("inf")
    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['end'] = infinity

    # родители
    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['end'] = None

    alg_dekstry(graph, costs, parents)
    # --- Алгоритм Дейкстры ---
