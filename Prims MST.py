

def prims_MST(G):
    X = set('1')
    T = []
    V = set()
    cost = 0
    for i in G.keys():
        V.add(i)
    while X != V:
        best = 100000000000
        v = ''
        e = [0, 0, 0]
        for i in X:
            for j in G[i]:
                if j[0] not in X:
                    if int(j[1]) < best:
                        best = int(j[1])
                        v = j[0]
                        e = [i, j[0], j[1]]
        X.add(v)
        cost += int(e[2])
        T.append(e)
    return cost


def run_algo():
    print("Program expects a list of edges of an undirected graph: 'tail head cost'.")
    print("Program will output cost of the MST of the graph.")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    f.close()
    D = {}
    for y in range(1, len(C)):
        temp = C[y].split(' ')
        if temp[0] in D.keys():
            D[temp[0]].append(temp[1:])
        else:
            D[temp[0]] = [temp[1:]]
        if temp[1] in D.keys():
            D[temp[1]].append([temp[0], temp[2]])
        else:
            D[temp[1]] = [[temp[0], temp[2]]]
    print(prims_MST(D))


if __name__ == '__main__':
    run_algo()
