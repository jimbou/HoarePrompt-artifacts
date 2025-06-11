#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of pairs of integers (n and k), where 1 <= k <= n <= 10^3.
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is an integer larger than or equal to 0, _ is t, n is an integer equal to the first integer in the input, k is an integer equal to the second integer in the input, res is a list of integers equal to [1] * n if k equals n, or range(n) if k equals 1, or [-1] otherwise, stdin is empty, and the elements of the list res are printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then generates a list of integers based on the values of n and k. If k equals n, the list contains n ones. If k equals 1, the list contains the numbers from 0 to n-1. Otherwise, the list contains a single -1. The function prints the generated list for each test case.

