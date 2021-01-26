

def max_WIS(C, n):
    A = {'0': 0, '1': C[1]}
    for i in range(2, n+1):
        A[str(i)] = max(A[str(i - 1)], A[str(i - 2)] + C[i])

    S = set()
    j = n
    while j > 1:
        if A[str(j - 1)] >= A[str(j - 2)] + C[j]:
            j -= 1
        else:
            S.add(j)
            j -= 2
    if A['0'] < C[1] and 2 not in S:
        S.add(1)

    return S


def run_algo():
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    n = int(C[0])
    for i in range(n+1):
        C[i] = int(C[i])
    f.close()
    MWIS = max_WIS(C, n)
    print(MWIS)


if __name__ == '__main__':
    run_algo()
