#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The output will be a series of integers, each representing the result of the condition n - k <= 1 for each test case. If the condition is true, the output will be n, otherwise it will be 1. The number of integers in the output will be equal to the value of t in the initial state.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then evaluates the condition n - k <= 1 for each test case and prints the result. If the condition is true, it prints the value of n; otherwise, it prints 1. The function repeats this process for each test case, with the number of test cases specified by an initial integer t read from standard input.

