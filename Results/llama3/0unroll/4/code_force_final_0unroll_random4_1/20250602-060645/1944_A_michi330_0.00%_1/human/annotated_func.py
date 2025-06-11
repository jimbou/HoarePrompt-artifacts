#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The output will be a series of integers, either 1 or n-1, where n is the first integer in each line of the input. The number of integers in the output will be equal to the value of t. If k is greater than or equal to n-1, the output will be 1; otherwise, the output will be n-1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers, n and k. It then prints the result of each test case, which is either 1 or n-1, depending on whether k is greater than or equal to n-1. The function processes multiple test cases, with the number of cases specified by the first integer read from standard input.

