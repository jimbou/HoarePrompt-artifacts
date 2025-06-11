#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two integers n and k such that 1 <= n <= 100 and 0 <= k <= n*(n-1)/2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: _ is the number of test cases in stdin, stdin is empty, and the value of n if n - k > 1 otherwise 1 is printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then prints the value of n if n is greater than k by more than 1, otherwise it prints 1. This process is repeated for each test case, until all input has been processed and the standard input is empty.

