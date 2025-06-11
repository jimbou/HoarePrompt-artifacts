#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The output will be a series of integers, each representing the result of the calculation n if n - k <= 1 else 1 for each test case. The number of integers in the output will be equal to the value of t.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it calculates and prints the result of the expression n if n - k <= 1 else 1. The function processes multiple test cases, with the number of test cases specified by an initial integer t read from standard input.

