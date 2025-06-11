#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (2 <= integer <= 10^5) and then a list of integers (1 <= integer <= 10^9) of length equal to the first integer.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: `t` is an integer between 2 and 10^5 (inclusive), `n` is an integer between 1 and 10^9 (inclusive), `a` is a list of integers of length `t-1`, `i` is `n`, `stdin` is empty, `_` is `t-1`, and the maximum of the minimum of adjacent elements in `a` that is greater than the initial value of `max` (0) is being printed, and this is printed: the maximum of the minimum of adjacent elements in `a` that is greater than the initial value of `max` (0)

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer 'n' followed by a list of 'n' integers. It then finds the maximum of the minimum of adjacent elements in each list that is greater than 0 and prints this value. The function processes all test cases and prints the result for each case.

