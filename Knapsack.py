import time


def knapsack(G, W, n):

    A = [[], []]
    for i in range(W+1):
        A[0].append(0)
        A[1].append(0)

    for j in range(1, n+1):
        jmod = j % 2
        for x in range(W+1):
            if jmod == 1:
                k = 0
            else:
                k = 1
            if x < G[j-1][1]:
                Acase2 = 0
            else:
                Acase2 = A[k][x - G[j-1][1]] + G[j-1][0]
            A[jmod][x] = max(A[k][x], Acase2)

    return A[jmod][W]


def run_algo():
    print("In the first line of the file, program expects: 'knapsack_size num_of_items'.")
    print("Lines there after are expected as: 'value_1 weight_1'")
    print("Program will output the value of the optimal solution.")
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    C0 = C[0].split(' ')
    W = int(C0[0])
    n = int(C0[1])
    del C[0]
    for i in range(n):
        C[i] = C[i].split(' ')
        C[i][0] = int(C[i][0])
        C[i][1] = int(C[i][1])

    f.close()

    start = time.time()
    print(knapsack(C, W, n))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run_algo()



