import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import random

list_to_draw = []
b = random()*10

for i in range(int(b)):
    for j in range(int(b)):
        a = random()
        if a > 0.7:
            list_to_draw.append((i, j))

D = nx.DiGraph()
D.add_edges_from(list_to_draw)

n = len(D.nodes())

Matrix = [[0 for x in range(n)] for y in range(n)]
for (u, v, w) in D.edges(data=True):
    w['w'] = round(np.random.random(), 2)
    Matrix[v][u] = w['w']
    print('{0}--->{1}: {2}.'.format(u, v, w['w']))

labeldict = {}
for (i, p) in D.nodes(data=True):
    p[i] = [np.random.random_integers(50), np.random.random_integers(50)]
    labeldict.update(p)
print(labeldict)


V = []
P = []
for i, j in labeldict.values():
    V.append(i)
    P.append(j)


print('P:', P)
print('Matrix : ', Matrix)
print('V :', V)


t = 300
W = [[0 for c in range(t)] for z in range(n)]
for i in range(t):
    for o in range(n):
        U = V[o]
        V[o] = V[o] + np.dot(P, Matrix[o])
        P[o] = V[o] - U
        W[o][i] = V[o]
    print(V)
    print(P)

plt.subplot(212)
pos = nx.spring_layout(D)

nx.draw(D, pos=pos, labels=labeldict, with_labels=True, node_size=1600, node_color='green', alpha=0.7, )

plt.figure(1)
plt.subplot(211)

for i in range(n):
    plt.plot(list(range(t)), W[i])

plt.show()
