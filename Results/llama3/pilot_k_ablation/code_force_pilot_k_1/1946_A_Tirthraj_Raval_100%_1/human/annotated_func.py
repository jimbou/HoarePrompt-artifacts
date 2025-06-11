#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: t is an integer equal to 0, _ is t, n is an integer, a is a sorted list of integers, p is an integer, res is an integer, stdin contains no test cases, and the value of res has been printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It sorts the list of integers and finds the count of the median value (the middle value in the sorted list). The function then prints the count of the median value for each test case. After processing all test cases, the function leaves the standard input empty.

