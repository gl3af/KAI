# 1 вариант
def fill_graph(n):
    graph = [[0] * n for i in range(n)]
    print("Введите n пар вершин (нумерация с 0):")
    for i in range(n):
        a, b = input().split()
        a = int(a)
        b = int(b)
        graph[a][b] = 1
        graph[b][a] = 1
    return graph


def has_alone_element(graph, n):
    for i in range(n):
        if sum(graph[i]) == 0:
            return True
    return False


def has_loops(graph, n):
    for i in range(n):
        if graph[i][i] == 1:
            return True
    return False


def print_graph(graph, n):
    print("  ", end=" ")
    for i in range(n):
        print(i, end=" ")
    print()
    print("  ", end=" ")
    for i in range(n):
        print("-", end=" ")
    print()
    for i in range(n):
        print(f"{i}|", end=" ")
        for j in range(n):
            print(graph[i][j], end=" ")
        print()


def neighbours(graph, n):
    print("Номера смежных вершин:")
    for i in range(n):
        print(f"{i} ->", end=" ")
        for j in range(n):
            if graph[i][j] == 1:
                print(j, end=" ")
        print()


def has_element_with_all_links(graph, n):
    for i in range(n):
        if sum(graph[i]) == n:
            return True
    return False


def graph_powers(graph, n):
    powers = list()
    for i in range(n):
        powers.append(sum(graph[i]))
    return powers


def elements_with_power_of_one(graph, n):
    print("Вершины графа со степенью 1: ", end=" ")
    for i in range(n):
        if sum(graph[i]) == 1:
            print(i, end=" ")


def main():
    n = int(input("Введите размер графа n <= 10: "))
    while n > 10:
        print("неверный ввод")
        n = int(input("Введите размер графа n <= 10: "))
    graph = fill_graph(n)
    print_graph(graph, n)
    if has_loops(graph, n):  # A
        print("Петли есть")
    else:
        print("Петлей нет")
    # Б
    if has_alone_element(graph, n):
        print("Есть несмежные с остальными вершины")
    else:
        print("Все вершины смежны с какой-либо другой вершиной")
    neighbours(graph, n)  # В
    has_element_with_all_links(graph, n)
    # Г
    if has_element_with_all_links(graph, n):
        print("Есть вершина связанная со всеми")
    else:
        print("Нет вершины связанной со всеми")

    # Д
    powers = graph_powers(graph, n)
    print("Степени вершин:", powers)
    # E
    print("Вершины со степенью 1:", end=" ")
    for i in range(len(powers)):
        if powers[i] == 1:
            print(i, end=" ")
    print()
    # Ж
    print("Степень графа:", max(powers))


if __name__ == '__main__':
    main()
