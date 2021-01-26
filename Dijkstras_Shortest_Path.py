def dijkstra(G, start):
    X = set()
    X.add(start)
    V = set(G.keys())
    a = {start: 0}
    b = {start: '1'}
    while X != V:
        best = 100000000000
        v = ''
        for i in X:
            for j in G[i]:
                if j[0] not in X:
                    if (a[i] + j[1]) < best:
                        best = a[i] + j[1]
                        #path = b[i] + '->' + j[0]
                        v = j[0]
        if v == '':
            return a
        a[v] = best
        X.add(v)
        #b[v] = path

    return a


def run_algo():
    print("Program expects an adjacency list representation of an undirected graph.")
    print("Each row should list an edge and then tuples of edges (edge, length).")
    file_name = input("Enter the file name to be processed:")
    start = input("Enter the starting point:")
    end = input("Enter the destinations:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    f.close()
    D = {}
    C.remove('')
    for x in C:
        g = x.split('\t')
        g.remove('')
        h = [[y.split(',')[0], int(y.split(',')[1])] if len(y) > 1 else y for y in g[1:]]
        D[g[0]] = h
    distances = dijkstra(D, start)
    output = end.split(' ')
    for k in output:
        print(k, distances[k])
        #print(k, path[k])


if __name__ == '__main__':
    run_algo()