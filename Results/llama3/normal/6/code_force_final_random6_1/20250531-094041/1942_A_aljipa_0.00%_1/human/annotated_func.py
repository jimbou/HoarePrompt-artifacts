#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer equal to 0, stdin is empty, n is an integer, k is an integer, res is a list of length n with values of either 1, a range from 0 to n-1, or -1, and the elements of the list res which are either 1, a range from 0 to n-1, or -1 are being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers n and k. It then generates a list of length n based on the values of n and k. If k equals n, the list contains all 1s. If k equals 1, the list contains a range of numbers from 0 to n-1. Otherwise, the list contains a single -1. The function prints the generated list for each test case.

