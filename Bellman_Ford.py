# Used for Johnsons Algorithm

def helper(A, dict, i, v):
    min_val = A[i-1][dict[v][0][0]] + dict[v][0][2]
    for x in dict[v]:
        y = A[i-1][x[0]] + x[2]
        if y < min_val:
            min_val = y
    return min_val


def bellmanford(G, n, s):
    A = []
    for i in range(n+1):
        A.append([])
        for j in range(n+2):
            A[i].append(float('inf'))

    A[0][s] = 0
    G_dict = {}
    for x in G:
        if x[1] in G_dict.keys():
            G_dict[x[1]].append(x)
        else:
            G_dict[x[1]] = [x]

    for i in range(1, n+1):
        for v in range(1, n+1):
            A[i][v] = min(A[i-1][v], helper(A, G_dict, i, v))

    for i in range(n+1):
        if A[n][i] < A[n-1][i]:
            return A[n], -1
    return A[n], 1



