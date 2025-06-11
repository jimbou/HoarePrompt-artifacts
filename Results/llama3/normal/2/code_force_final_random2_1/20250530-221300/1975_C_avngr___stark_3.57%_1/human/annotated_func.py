#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given before the test cases.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: _ is t, t is an integer between 1 and 500, n is an integer between 2 and 10^5, a is a list of n integers between 1 and 10^9, max is the maximum of the minimum of adjacent pairs of elements in a, stdin contains 0 test cases, i is n-1, and max (which is the maximum of the minimum of adjacent pairs of elements in a) is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds the maximum of the minimum of adjacent pairs of elements in the list and prints this value. The function repeats this process for all test cases, consuming all input from standard input.

