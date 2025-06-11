#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: t is greater than or equal to 0, _ is t-1, stdin contains no test cases, n is an integer equal to the last input integer, a is a sorted list of integers equal to the last input list of integers, p is an integer equal to (n+1)//2 - 1, res is an integer equal to the count of the (n+1)//2 th element in the sorted list a, and the count of the (n+1)//2 th element in the sorted list a is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order, finds the median (the middle value), and counts the occurrences of the median. The function then prints the count of the median for each test case.

