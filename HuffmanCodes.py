from collections import deque
from Merge_Sort import *
import sys


sys.setrecursionlimit(2500)
global merge_count


def huffman(G, n):
    global merge_count
    merge_count = {}
    G = sort(G)
    q1 = deque()
    q2 = deque()
    for i in range(n):
        merge_count[str(i)] = 0
        q1.append([G[i], str(i)])
    huffman_recursion(q1, q2)
    return max(merge_count.values()), min(merge_count.values())


def helper(t1, t2, q2):
    global merge_count
    comb = t1[0] + t2[0]
    meta = t2[1] + ',' + t1[1]
    for j in meta.split(','):
        merge_count[j] += 1
    q2.append([comb, meta])
    return q2


def huffman_recursion(que1, que2):
    global merge_count
    if (len(que1) + len(que2)) == 2:
        for k in merge_count.keys():
            merge_count[k] += 1
        return
    else:
        if len(que2) == 0:
            temp1 = que1.popleft()
            temp2 = que1.popleft()
            que2 = helper(temp1, temp2, que2)
            return huffman_recursion(que1, que2)
        elif len(que1) == 0:
            temp1 = que2.popleft()
            temp2 = que2.popleft()
            que2 = helper(temp1, temp2, que2)
            return huffman_recursion(que1, que2)
        else:
            if que1[0] < que2[0]:
                temp1 = que1.popleft()
                if len(que1) == 0:
                    temp2 = que2.popleft()
                    que2 = helper(temp1, temp2, que2)
                    return huffman_recursion(que1, que2)
                else:
                    if que1[0] < que2[0]:
                        temp2 = que1.popleft()
                        que2 = helper(temp1, temp2, que2)
                        return huffman_recursion(que1, que2)
                    else:
                        temp2 = que2.popleft()
                        que2 = helper(temp1, temp2, que2)
                        return huffman_recursion(que1, que2)
            else:
                temp1 = que2.popleft()
                if len(que2) == 0:
                    temp2 = que1.popleft()
                    que2 = helper(temp1, temp2, que2)
                    return huffman_recursion(que1, que2)
                else:
                    if que1[0] < que2[0]:
                        temp2 = que1.popleft()
                        que2 = helper(temp1, temp2, que2)
                        return huffman_recursion(que1, que2)
                    else:
                        temp2 = que2.popleft()
                        que2 = helper(temp1, temp2, que2)
                        return huffman_recursion(que1, que2)


def run_algo():
    file_name = input("Enter the file name to be processed:")
    f = open(file_name, 'r')
    C = f.read().split('\n')
    C.remove('')
    n = int(C[0])
    del C[0]
    for i in range(n):
        C[i] = int(C[i])
    f.close()
    print(huffman(C, n))


if __name__ == '__main__':
    run_algo()
