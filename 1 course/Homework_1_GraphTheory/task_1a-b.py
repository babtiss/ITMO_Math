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
print(country)
# создадим граф
for i in range(E):
    a, b = edges[i]
    G.add_edge(country[a], country[b])

# нарисуем граф
plt.figure(figsize=(18, 12))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=400)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(G, pos, arrows=False)
plt.show()

# --- task 1.b ---
# Посчитаем степени вершин
degree = [0] * V
for i in range(V):
    degree[i] = sum(matrix[i])

# Посчитаем кратчайшее растояние по алгоритму Флойда–Уоршелла
distance = [[0] * V for i in range(V)]
inf = 10 ** 5
for i in range(V):
    for j in range(V):
        if matrix[i][j]:
            distance[i][j] = 1
        else:
            distance[i][j] = inf

for k in range(V):
    for i in range(V):
        for j in range(V):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# Нахождение эксцентриситета для каждой вершины графа
ext = [0] * V
for i in range(V):
    for j in range(V):
        ext[i] = max(ext[i], distance[i][j])

# Расчёт радиуса/диаметра/центра
rad = min(ext)
diam = max(ext)
center = []
for i in range(V):
    if ext[i] == rad:
        center.append(country[i])

# Выводим то что нашли
print('max_degree:', max(degree))
print('min_degree:', min(degree))
print('all ex:', *ext)
print('radius', rad)
print('diameter', diam)
print('center', center)
