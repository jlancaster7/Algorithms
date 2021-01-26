import time


def euclid_dist(a, b):
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5


def TSP_H(G, n):
    current = '1'
    V = set(G.keys())
    V.remove(current)
    path = []
    while len(V) != 0:
        nextc = '0'
        closest = 100000
        count_ = 0
        for x in V:
            dist = euclid_dist(G[current], G[x])
            count_ += 1
            if dist < closest:
                closest = dist
                nextc = x
            if dist == closest:
                if int(x) < int(nextc):
                    nextc = x
        path.append([current, nextc, closest])
        current = nextc
        V.remove(current)
    total_dist = 0
    for x in path:
        total_dist += x[2]
    total_dist += euclid_dist(G[path[-1][1]], G['1'])
    return total_dist // 1


def run_algo():
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    n = int(C[0])
    D = {}
    del C[0]
    temp = ''
    for i in range(0, n):
        temp = C[i].split(' ')
        D[temp[0]] = [float(temp[1]), float(temp[2])]
    start = time.time()
    print(TSP_H(D, n))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run_algo()

