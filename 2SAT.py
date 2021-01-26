import time
import math
import random


def random_state(n):
    state = []
    for i in range(n):
        x = random.random()
        if x >= 0.5:
            state.append('1')
        else:
            state.append('0')
    return state


def satisfaction_check(A, B, potential_state, n):
    count = 0
    rules = A + B
    sat = []
    unsat = []
    for x in rules:
        if x[0][0] == '-' and potential_state[abs(int(x[0])) - 1] == '0':
            sat.append(x)
            count += 1
            continue
        elif x[0][0] != '-' and potential_state[abs(int(x[0])) - 1] == '1':
            sat.append(x)
            count += 1
            continue
        elif x[1][0] == '-' and potential_state[abs(int(x[1])) - 1] == '0':
            sat.append(x)
            count += 1
            continue
        elif x[1][0] != '-' and potential_state[abs(int(x[1])) - 1] == '1':
            sat.append(x)
            count += 1
            continue
        else:
            unsat.append(x)
    if count == len(rules):
        return sat, unsat, 1
    else:
        return sat, unsat, -1


def state_flip(unsatisfied, prev_state):
    rand_rule = random.randint(0, len(unsatisfied)-1)
    s_flip = unsatisfied[rand_rule]

    rand_var = random.random()
    if rand_var >= 0.5:
        prev_state[abs(int(s_flip[1])) - 1] = str((int(prev_state[abs(int(s_flip[1])) - 1]) + 1) % 2)
    else:
        prev_state[abs(int(s_flip[0])) - 1] = str((int(prev_state[abs(int(s_flip[0])) - 1]) + 1) % 2)
    return prev_state


def twosat(G, n):
    for i in range(int(math.log(n, 2))):
        state = random_state(n)
        A = G.copy()
        B = []
        for j in range(int(max(2*len(G), 5000))):
            A, B, test = satisfaction_check(A, B, state, n)
            if test == 1:
                return 'Satisfied'
            else:
                state = state_flip(B, state)
    return "Unsatisfiable"


def reduction(G, gn, n):
    count_array = [[0,0] for _ in range(gn+1)]
    for x in G:
        if x[0][0] == '-':
            count_array[abs(int(x[0]))][1] += 1
        else:
            count_array[abs(int(x[0]))][0] += 1
        if x[1][0] == '-':
            count_array[abs(int(x[1]))][1] += 1
        else:
            count_array[abs(int(x[1]))][0] += 1
    elim_list = [i for i in range(1,gn+1) if (count_array[i][0] == 0) or (count_array[i][1] == 0)]
    elim_list = set(elim_list)
    for i in range(n-1, -1, -1):
        if (abs(int(G[i][0])) in elim_list) or (abs(int(G[i][1])) in elim_list):
            del G[i]
    return G


def run_algo():
    print("Program expects two variables per clause and '-' denoting 'not'.")
    file_name = input("Enter file to be processed: ")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    n = int(C[0])
    del C[0]
    for i in range(n):
        C[i] = C[i].split(' ')
    start = time.time()
    check = len(C)+1
    while check > len(C):
        check = len(C)
        D = reduction(C, n, len(C))
        C = D
    print(twosat(C, n))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run_algo()

