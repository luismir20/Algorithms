def knapsack(M, w, val, n):
    K = [[0 for x in range(M + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i - 1] <= j:
                K[i][j] = max(val[i - 1] + K[i - 1][j - w[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    return K[n][M]


val = Values = [60, 100, 120]
w = Weight = [10, 20, 30]
M = MaxWeightAllowed =  50
n = len(val)

# Solve the problem using the knapsack function
result = knapsack(M, w, val, n)
print("Maximum value that can be obtained:", result)


#Maximum value that can be obtained: 220

#The Knapsack Problem algorithm is useful in
#situations where we need to optimize the use of limited resources.