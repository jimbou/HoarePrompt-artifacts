#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of pairs of integers (n and k), where 1 <= k <= n <= 10^3.
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: t is the number of test cases that must be greater than or equal to 0, _ is t, n is an integer, k is an integer, res is a list of integers, and the list of integers in res is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers: n and k. It then generates a list of integers based on the values of n and k, and prints the list. If k is equal to n, the list contains all ones. If k is equal to 1, the list contains the numbers from 0 to n-1. For all other cases, the list contains a single -1. The function repeats this process for the specified number of test cases.

