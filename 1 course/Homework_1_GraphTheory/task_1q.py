import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Input
V = 42
E = 87
fin_country = open("europe.txt")
fin_edges = open("distances.txt")
country = []  # список стран
edges = []  # список рёбер
edges_name = []
matrix = [[0] * V for i in range(V)]  # матрица смежности
for i in range(V):
    pars_one = fin_country.readline().split('.')
    if i != V - 1:
        num, name = pars_one[0], pars_one[1][:-1]
    else:
        num, name = pars_one[0], pars_one[1]
    country.append(name)

for i in range(E):
    pars_two = fin_edges.readline().split()
    a, b, c = int(pars_two[0]), int(pars_two[1]), int(float(pars_two[2]) // 1)
    matrix[a][b] = 1
    matrix[b][a] = 1
    edges.append([country[a], country[b], c])
    edges_name.append([a, b, c])


# найдём остовное дерево, с помощью алгоритма Прима
def solve(n, m, edges):
    def find(v):
        nonlocal parent
        while (v != parent[v]):
            v = parent[v]
        return v

    def jopa(v1, v2):
        return find(v1) == find(v2)

    def union():
        nonlocal parent, rank, a, b, c, answer

        v1 = find(a)

        v2 = find(b)
        if rank[v1] > rank[v2]:
            v1, v2 = v2, v1
        rank[v2] += rank[v1]
        parent[v1] = v2

    parent = [i for i in range(n)]
    rank = [1] * n

    answer = 0
    answer_edges = []
    for i in range(m):
        a, b, c = edges[i]
        if not jopa(a, b):
            union()
            answer += c
            answer_edges.append([a, b])

    # Получим код Прюфера
    G_new = nx.Graph()
    G_new.add_edges_from(answer_edges)
    prufer_code = nx.to_prufer_sequence(G_new)

    # Переведём num вершин в name и посмотрим на них
    for i in prufer_code:
        print(country[i], end =', ')


solve(V, E, edges_name)

