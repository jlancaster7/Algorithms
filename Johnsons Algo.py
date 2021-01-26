from Bellman_Ford import *
from Dijkstras_Shortest_Path import dijkstra


def Johnsons(G, n, m):
    Gprime = G.copy()
    for i in range(1, n+1):
        Gprime.append([n+1, i, 0])
    weights, flag = bellmanford(Gprime, n, n + 1)
    if flag == -1:
        return "Negative cycle found in Bellman-Ford"
    Gdprime = {}
    for i in range(len(G)):
        if str(G[i][0]) in Gdprime.keys():
            Gdprime[str(G[i][0])].append([str(G[i][1]), G[i][2] + weights[G[i][0]] - weights[G[i][1]]])
        else:
            Gdprime[str(G[i][0])] = [[str(G[i][1]), G[i][2] + weights[G[i][0]] - weights[G[i][1]]]]
    SSSP = []
    for i in range(1, n+1):
        if str(i) not in Gdprime:
            Gdprime[str(i)] = []
    for x in Gdprime.keys():
        z = dijkstra(Gdprime, str(x))
        del z[x]
        for y in z.keys():
            z[y] = z[y] - weights[int(x)] + weights[int(y)]
        for value in z.values():
            SSSP.append(value)

    return min(SSSP)


def run_algo():
    print("Program expects a list of edges describing a graph in format: 'Tail', 'Head', 'cost'")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    x = C[0].split(' ')
    n = int(x[0])
    m = int(x[1])
    del C[0]
    for i in range(len(C)):
        C[i] = C[i].split(' ')
        C[i][0] = int(C[i][0])
        C[i][1] = int(C[i][1])
        C[i][2] = int(C[i][2])
    print(Johnsons(C, n, m))


if __name__ == '__main__':
    run_algo()
