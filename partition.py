import random
import math
import heapq
import sys

def residue(A, S):
    s1 = 0
    s2 = 0
    for i, s in enumerate(S):
        if s == 1:
            s1 += A[i]
        else:
            s2 += A[i]
    return abs(s1 - s2)

def prepart_residue(A, S):
    n = len(A)

    A_ = []

    for i in range(1, n+1):
        indices = [j for j, s in enumerate(S) if s == i]
        A_.append(sum([A[index] for index in indices]))

    return kk(A_)

def kk(A):
    A = [-1 * a for a in A[:]]

    heapq.heapify(A)

    while len(A) > 1:
        n1  = heapq.heappop(A)
        n2 = heapq.heappop(A)

        heapq.heappush(A, n1 - n2)

    return -A[0]

def rr(A, max_iter = 5000):
    n = len(A)

    S = [random.choice([-1, 1]) for _ in range(n)]

    for _ in range(1, max_iter):
        S_ = [random.choice([-1, 1]) for _ in range(n)]
        if residue(A, S_) < residue(A, S):
            S = S_

    return residue(A, S)

def hill_climbing(A, max_iter = 5000):
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

    return residue(A, S)

def simulated_annealing(A, max_iter = 5000):
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

    return residue(A, S__)

def prepart_rr(A, max_iter = 5000):
    n = len(A)

    S = [random.randint(1, n) for _ in range(n)]

    for _ in range(1, max_iter):
        S_ = [random.randint(1, n) for _ in range(n)]
        if prepart_residue(A, S_) < prepart_residue(A, S):
            S = S_

    return prepart_residue(A, S)

def prepart_hill_climbing(A, max_iter = 5000):
    n = len(A)

    S = [random.randint(1, n) for _ in range(n)]

    for _ in range(1, max_iter):
        i = random.randint(0, n-1)
        j = random.randint(1, n)
        while j == S[i]:
            j = random.randint(1, n)
        S_ = S[:]
        S_[i] = j
        if prepart_residue(A, S_) < prepart_residue(A, S):
            S = S_

    return prepart_residue(A, S)

def prepart_simulated_annealing(A, max_iter = 5000):
    def T(iter):
        return 10**10 * (.8)**(math.floor(iter / 300))

    n = len(A)

    S = [random.randint(1, n) for _ in range(n)]

    S__ = S

    for iter in range(1, max_iter):
        i = random.randint(0, n-1)
        j = random.randint(1, n)
        while j == S[i]:
            j = random.randint(1, n)
        S_ = S[:]
        S_[i] = j
        if prepart_residue(A, S_) < prepart_residue(A, S):
            S = S_
        elif (random.random() < math.exp(-prepart_residue(A, S_) - prepart_residue(A, S)) / T(iter)):
            S = S_
        if prepart_residue(A, S) < prepart_residue(A, S__):
            S__ = S

    return prepart_residue(A, S__)

try:
    flag, alg, file = sys.argv[1:4]
    flag, alg = int(flag), int(alg)
except:
    raise TypeError('Incorrect number of arguments')

A = []

f = open(file, "r")

for i in range(100):
    A.append(int(f.readline()))

if alg == 0:
    print(kk(A))
elif alg == 1:
    print(rr(A))
elif alg == 2:
    print(hill_climbing(A))
elif alg == 3:
    print(simulated_annealing(A))
elif alg == 11:
    print(prepart_rr(A))
elif alg == 12:
    print(prepart_hill_climbing(A))
elif alg == 13:
    print(prepart_simulated_annealing(A))
else:
    raise ValueError('Invalid algorithm selection')

# rand_inputs = []

# print('Starting random tests:')

# for i in range(50):
#     rand_inputs.append([random.randint(1, 10**12) for _ in range(100)])


# results = []
# for A in rand_inputs:
#     print([kk(A), rr(A, max_iter = 25000), hill_climbing(A, max_iter = 25000), 
#            simulated_annealing(A, max_iter = 25000), prepart_rr(A, max_iter = 25000),  
#            prepart_hill_climbing(A, max_iter = 25000),  prepart_simulated_annealing(A, max_iter = 25000)])