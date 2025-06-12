#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer between 1 and 10^3 (inclusive), stdin is empty, n is an integer, k is an integer, res is a list of integers.

#Overall this is what the function does:This function reads a series of input pairs from standard input, where each pair consists of two integers, n and k. It then generates a list of integers based on the values of n and k. If k is equal to n, the list contains all 1s. If k is 1, the list contains the numbers from 1 to n. For any other values of k, the list contains a single -1. The function prints each generated list to the console, one list per input pair.

