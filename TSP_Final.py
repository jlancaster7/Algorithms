import time


def euclid_dist(a, b):
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5


def bitmask(c, n):
    mask = ['0' for i in range(n)]
    for i in c:
        mask[i-1] = '1'
    return ''.join(mask)


def bitmasks(n, m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1, m-1):
                yield (1 << (n-1)) + x
            for x in bitmasks(n-1, m):
                yield x
        else:
            yield 0
    else:
        yield (1 << n) - 1


def TSP(G, n):
    A = {'1'+'0'*(n-1): [0]}
    for m in range(1, n):
        for q in bitmasks(n-1, m):
            get_bin = lambda x, e: format(x, 'b').zfill(e)
            d = get_bin(q, n-1)
            r = '1' + d
            A[r] = [float('inf') for _ in range(n)]
            for t in range(n):
                s = list(r)
                if s[t] == '1' and t != 0:
                    s[t] = '0'
                    s = ''.join(s)
                    temp = []
                    for h in range(n):
                        if s[h] == '1':
                            temp.append(A[s][h] + euclid_dist(G[h], G[t]))
                    A[r][t] = min(temp)
    best = 100000000
    final = bitmask(range(0, n), n)
    for g in range(1, n):
        final_dist = euclid_dist(G[g], G[0])
        if (A[final][g] + final_dist) < best:
            best = A[final][g] + final_dist
    return best // 1


def run_algo():
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    n = int(C[0])
    del C[0]
    for i in range(n):
        C[i] = C[i].split(' ')
        C[i][0] = float(C[i][0])
        C[i][1] = float(C[i][1])
    start = time.time()
    print(TSP(C, n))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run_algo()
