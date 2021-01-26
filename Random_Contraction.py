from random import sample, choice
import copy


def random_contraction(Z):
    w = 0
    while len(Z) > 2:
        superN = 'Super ' + str(w)
        w += 1
        u, v = sample(Z, 2)
        while v[0] not in u or v == u:
            v = choice(Z)
        Z.remove(u)
        Z.remove(v)
        t = [superN] + u[1:] + v[1:]
        if u[0] in t[1:]:
            t.remove(u[0])
        if v[0] in t[1:]:
            t.remove(v[0])
        Z.append(t)
        for i in range(len(Z)):
            if u[0] in Z[i][1:] or v[0] in Z[i][1:]:
                for j in range(1, len(Z[i])):
                    if Z[i][j] == u[0] or Z[i][j] == v[0]:
                        Z[i][j] = t[0]
                        if Z[i][j] == Z[i][0]:
                            Z[i][j] = 'delete'
                for k in range(Z[i].count('delete')):
                    Z[i].remove('delete')

    return Z[0], Z[1]


def cut_count(c, d):
    if len(c[1:]) < len(d[1:]):
        return len(c[1:])
    else:
        return len(d[1:])


def random_contraction_loop(A):
    K = copy.deepcopy(A)
    n = len(K)
    e, f = random_contraction(K)
    best_pair = [e[0], f[0]]
    best_min_cuts = cut_count(e, f)
    for y in range(int((n ** 2))):
        G = copy.deepcopy(A)
        e, f = random_contraction(G)
        min_cuts = cut_count(e, f)
        if min_cuts < best_min_cuts:
            best_min_cuts = min_cuts
            best_pair = [e, f]
    return best_pair, best_min_cuts


def run_algo():
    print("Program expects an adjacency list representing an undirected graph.")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    f.close()
    C.remove('')

    for i in range(len(C)):
        C[i] = C[i].split('\t')
        if '' in C[i]:
            C[i].remove('')

    pair, cuts = random_contraction_loop(C)
    print('Best A = ', pair[0])
    print('Best B = ', pair[1])
    print('with ', cuts, '# of cuts')


if __name__ == '__main__':
    run_algo()

