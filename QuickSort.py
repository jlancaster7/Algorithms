

def partition(B, l, r):
    med = (r-l-1) // 2 + l
    D = [B[l], B[med], B[r-1]]
    if int(D[0]) > int(D[1]):
        if int(D[1]) > int(D[2]):
            p = D[1]
            x = med
        else:
            if int(D[0]) > int(D[2]):
                p = D[2]
                x = r-1
            else:
                p = D[0]
                x = l
    else:
        if int(D[0]) > int(D[2]):
            p = D[0]
            x = l
        else:
            if int(D[1]) < int(D[2]):
                p = D[1]
                x = med
            else:
                p = D[2]
                x = r-1
    B[x] = B[l]
    B[l] = p

    i = l + 1
    for j in range(l + 1, r):
        if int(B[j]) < int(p):
            a = B[j]
            B[j] = B[i]
            B[i] = a
            i += 1
    a = B[l]
    B[l] = B[i-1]
    B[i-1] = a
    return B, l, i-1, i, r


def quicksort(A, l, r, count):
    count += max((r-l) - 1, 0)
    if (r - l) <= 1:
        return A, count
    else:
        A, l1, r1, l2, r2 = partition(A, l, r)
        A, count = quicksort(A, l1, r1, count)
        A, count = quicksort(A, l2, r2, count)

        return A, count


def run_algo():
    print("Program expects a list of numbers in unsorted order.")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    f.close()
    C.remove('')

    l = 0
    r = len(C)
    count = 0
    C, count = quicksort(C, l, r, count)
    print(C)


if __name__ == '__main__':
    run_algo()

