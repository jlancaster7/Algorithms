def merge(b, c):
    i = 0
    j = 0
    Z = []
    c_end = False
    b_end = False
    for k in range(len(b) + len(c)):
        if (float(b[i]) < float(c[j]) or c_end) and not b_end:
            Z.append(b[i])
            if i == len(b)-1:
                b_end = True
            else:
                i += 1
        else:
            Z.append(c[j])
            if j == len(c)-1:
                c_end = True
            else:
                j += 1
    return Z


def sort(A):
    if len(A) == 2:
        if float(A[0]) < float(A[1]):
            return A
        else:
            return [A[1], A[0]]
    elif len(A) == 1:
        return A
    else:
        n2 = len(A) // 2
        x = sort(A[:n2])
        y = sort(A[n2:])
        return merge(x, y)


def run_algo():
    A = input().split(' ')
    output = sort(A)
    print(output)

if __name__ == '__main__':
    run_algo()
