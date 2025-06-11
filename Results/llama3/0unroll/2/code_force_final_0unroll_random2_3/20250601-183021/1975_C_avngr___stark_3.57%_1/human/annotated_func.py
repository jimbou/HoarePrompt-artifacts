#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given on the first line.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: The output state will contain t number of lines, each containing the maximum value of the minimum of adjacent pairs in the input list. The value of t remains unchanged, stdin will be empty after the loop execution, and the values of n and a will be the last input values.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds the maximum value of the minimum of adjacent pairs in each list and prints this value for each test case. The function processes all test cases and leaves the standard input empty.

