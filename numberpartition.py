import random
import math
import heapq

def residue(A, S):
    s1 = 0
    s2 = 0
    for i, s in enumerate(S):
        if s == 1:
            s1 += A[i]
        else:
            s2 += A[i]
    return abs(s1 - s2)

def kk(A):
    # A_copy = A.copy()
    # A = A[:]
    # # A = [(A[i], i, i) for i in range(len(A))]
    # # print(A)
    # while True:
    #     print(A)
    #     A.sort(reverse=True, key=lambda x: x[0])

    #     n1, sub1, idx1 = A[0]
    #     n2, sub2, idx2 = A[1]

    #     if n2 == 0:
    #         residue = n1
    #         break

    #     if sub1 / 2 != sub2 / 2:
    #         if sub2 > sub1:
    #             A[0] = (n1 - n2, sub1, idx1)
    #             A[1] = (0, int(sub1/2)*2 + (sub1+1)%2, idx2)
    #         else:
    #             A[0] = (n1 - n2, sub2, idx1)
    #             A[1] = (0, int(sub2/2)*2 + (sub2+1)%2, idx2)
               

    # print(A.sort(key=lambda x: x[2]))

    A = [-1 * a for a in A[:]]

    heapq.heapify(A)

    while True:
        n1  = heapq.heappop(A)

        try: 
            n2 = heapq.heappop(A)
        except:
            residue = n1
            break

        heapq.heappush(A, n1 - n2)

    return -residue

def rr(A, max_iter = 100):
    n = len(A)

    S = [random.choice([-1, 1]) for _ in range(n)]

    for _ in range(1, max_iter):
        S_ = [random.choice([-1, 1]) for _ in range(n)]
        if residue(A, S_) < residue(A, S):
            S = S_

    return S, residue(A, S)

def hill_climbing(A, max_iter = 1000):
    n = len(A)

    S = [random.choice([-1, 1]) for _ in range(n)]

    for _ in range(1, max_iter):
        i = random.randint(0, n-1)
        j = i
        while j == i:
            j = random.randint(0, n-1)
        S_ = S[:]
        S_[i] = -1 * S[i]
        S_[j] = -1 * S[j]
        if residue(A, S_) < residue(A, S):
            S = S_

    return S, residue(A, S)

def simulated_annealing(A, max_iter = 1000):
    def T(iter):
        return 10**10 * (.8)**(math.floor(iter / 300))

    n = len(A)

    S = [random.choice([-1, 1]) for _ in range(n)]

    S__ = S

    for iter in range(1, max_iter):
        i = random.randint(0, n-1)
        j = i
        while j == i:
            j = random.randint(0, n-1)
        S_ = S[:]
        S_[i] = -1 * S[i]
        S_[j] = -1 * S[j]
        if residue(A, S_) < residue(A, S):
            S = S_
        elif (random.random() < math.exp(-residue(A, S_) - residue(A, S)) / T(iter)):
            S = S_
        if residue(A, S) < residue(A, S__):
            S__ = S

    return S__, residue(A, S)

A = [10, 8, 7, 6, 5]

print(kk(A))

print(rr(A))

print(hill_climbing(A))

print(simulated_annealing(A))