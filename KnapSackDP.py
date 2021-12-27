if __name__ = '__main__':

    def knapSack(maxW, wt, val, n):
        K = [[0 for _ in range(maxW + 1)] for _ in range(n + 1)]

        # Build table K[][] in bottom up manner
        for i in range(n + 1):
            for w in range(maxW + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                    # print (K[i][w])
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1]
                                  + K[i-1][w-wt[i-1]],
                                  K[i-1][w])
                    # print (K[i][w])
                else:
                    K[i][w] = K[i-1][w]
                    # print (K[i][w])

        return K[n][maxW]

    # Driver code
    val = [1024, 2048, 3192, 4096]
    wt = [1024, 2048, 3192, 4096]
    W = 37000
    n = len(val)
    print(knapSack(W, wt, val, n))
