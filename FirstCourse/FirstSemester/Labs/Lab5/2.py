import csv

inf = float('Inf')


def menu(graph):
    destinations_list = ["центральный вокзал", "тандем", "ривьера", "парк хаус", "мега",
                         "кремль", "набережная", "городская больница №7", "каи 1 здание",
                         "каи 2 здание", "каи 7 здание", "кфу", "парк горького", "аэропорт",
                         "площадь свободы", "ркб", "ак барс арена", "озеро кабан"]
    while True:
        choice = int(input("Введите действие\n1) Построить маршут из одной точки в другую\n2) Выход\n(ввести цифру)\n"))
        if choice == 2:
            break
        else:
            print("Доступные точки: ")
            for destination in destinations_list:
                print(destination)
            way = input("Введите пункт отправки и пункт названчения через пробел: ")
            dests = []
            indexes = []
            for dest in destinations_list:
                if dest in way:
                    dests.append(dest)
                    indexes.append(way.index(dest))
            start = dests[indexes.index(min(indexes))]
            stop = dests[indexes.index(max(indexes))]

            while not (start in destinations_list and stop in destinations_list):
                print("Неверный ввод, попробуйте еще раз")
                way = input("Введите пункт отправки и пункт названчения через пробел: ")
                dests = []
                indexes = []
                for dest in destinations_list:
                    if dest in way:
                        dests.append(dest)
                        indexes.append(way.index(dest))
                start = dests[indexes.index(min(indexes))]
                stop = dests[indexes.index(max(indexes))]
            start_pos = destinations_list.index(start.lower())
            stop_pos = destinations_list.index(stop.lower())
            d = dijkstra(graph, start_pos)
            path = get_path(graph, start_pos, stop_pos, d)
            print(f"Ваша дорога займёт {round(d[stop_pos], 2)} км")
            print("Ваш путь: ", end=" ")
            for dot in path:
                print(f"{destinations_list[dot]} ->", end=" ")
            print()


def dijkstra(graph, start):
    n = len(graph)
    queue = [(0, start)]

    d = [inf for i in range(n)]
    d[start] = 0
    while len(queue) != 0:
        (cost, u) = queue.pop(0)

        for v in range(n):
            if d[v] > d[u] + graph[u][v]:
                d[v] = d[u] + graph[u][v]
                queue.append((d[v], v))

    for i in range(len(d)):
        d[i] = round(d[i], 1)
    return d


def get_path(graph, start, stop, d):
    n = len(graph)

    path = [stop]
    while stop != start:
        for v in range(n):
            if d[v] == round(round(d[stop], 1) - round(graph[stop][v], 1), 1):
                path.append(v)
                stop = v

    return path[::-1]


def fill_graph(graph):
    with open('matrix.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        n = 0
        for row in reader:
            graph.append(row)
            n += 1
        for i in range(n):
            for j in range(n):
                graph[i][j] = float(graph[i][j])


def main():
    graph = []
    fill_graph(graph)
    menu(graph)


if __name__ == "__main__":
    main()
