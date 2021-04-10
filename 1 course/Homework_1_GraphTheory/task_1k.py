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
G = nx.Graph()  # граф
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
    a, b = int(pars_two[0]), int(pars_two[1])
    matrix[a][b] = matrix[b][a] = 1
    edges.append([a, b])

# создадим граф
for i in range(E):
    a, b = edges[i]
    G.add_edge(country[a], country[b])

# Построим кратчайший замкнутый путь, с помощью функции либы networkx
a = list(nx.eulerian_circuit(nx.eulerize(G)))
for i in a:
    v1, v2 = i
    print('(', v1, '-->', v2, end=') ')
