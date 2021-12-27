if __name__ == '__main__':

    def knapSack(maxW, wt, val, n):
        # initial conditions to break recursion
        if n == 0 or maxW == 0:
            return 0
        # If weight is higher than capacity then it is not included
        if (wt[n-1] > maxW):
            return knapSack(maxW, wt, val, n-1)
        # return either nth item being included or not
        else:
            return max(val[n-1] + knapSack(maxW-wt[n-1], wt, val, n-1),
                       knapSack(maxW, wt, val, n-1))
    # To test above function
    val = [1024, 2048, 3192, 4096]
    wt = [1024, 2048, 3192, 4096]
    maxW = 37000
    n = len(val)
    print(knapSack(maxW, wt, val, n))
