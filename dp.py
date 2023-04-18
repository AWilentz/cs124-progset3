
def dp(A):    
    n = len(A)
    b = sum(A)
    # print(n, b)
    dp = [[[False, -1] for i in range(b+1)] for j in range(n+1)]
    dp[1][A[0]] = [True, 1]
    for i in range(1, n):
        for j in range(b+1):
            curr = dp[i][j]
            # print(A[i])
            if curr[0]:
                if j + A[i] <= b:
                    # print(i,j,A[i],1)
                    dp[i+1][j + A[i]] = [True, 1]
                dp[i+1][j] = [True, 0]
    
    residue = b+1
    for j in range(b+1):
        if dp[n][j][0] == True:
            if abs((b-j)-j) < residue:
                residue = min(residue, abs((b-j)-j))
                sum_group1 = j

    pred = n
    ptr = sum_group1
    assignment = []
    # # print(dp[n])
    # # print(ptr)
    while pred > 0:
        assgn_val = dp[pred][ptr][1]
        assignment.insert(0, (assgn_val if assgn_val else -1))
        ptr = ptr - A[pred-1] * assgn_val
        pred -= 1
    print(residue, sum_group1, assignment, sep='\t')

    # for i in range(n+1):
    #     print(dp[i])

print('residue', 'sum_1', 'assignment', sep='\t')
dp([10,8,7,6,5])
dp([10])
dp([10, 15, 5, 1])