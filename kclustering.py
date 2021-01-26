import heapq
from networkx.utils import union_find


def preprocessing(D):
    for i in range(len(D)):
        D[i].append(D[i][2])
        D[i][2] = int(D[i][1])-1
        D[i][1] = int(D[i][0])-1
        D[i][0] = int(D[i][3])
        del D[i][3]
    return D


def kclustering(c_list, vert_count):

    u = union_find.UnionFind(range(0, vert_count))
    heapq.heapify(c_list)
    k = [i for i in u.to_sets()]
    while len(k) > 4:
        temp = heapq.heappop(c_list)
        j = u.__getitem__(temp[1])
        l = u.__getitem__(temp[2])
        if j != u:
            u.union(j, l)
        k = [i for i in u.to_sets()]
    ans = heapq.heappop(c_list)
    while u.__getitem__(ans[1]) == u.__getitem__(ans[2]):
        ans = heapq.heappop(c_list)

    return ans[0]


def run_algo():
    print("Program expects a list of edges of an undirected graph: 'tail', 'head', 'cost'.")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    for i in range(1, len(C)):
        C[i] = C[i].split(' ')
    f.close()
    n = int(C[0])
    C_processed = preprocessing(C[1:])
    print(kclustering(C_processed, n))


if __name__ == '__main__':
    run_algo()
