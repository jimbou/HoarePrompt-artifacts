#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. The integer is a positive integer and does not exceed 10^5. The integers in the list are positive integers and do not exceed 10^9.
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: t is 0, _ is t, n is an integer, a is a sorted list of integers, p is an integer, res is the count of the most frequent integer in the second half of a, stdin contains multiple test cases - t, and the count of the most frequent integer in the second half of a which is res is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n positive integers. It sorts the list of integers and finds the count of the most frequent integer in the second half of the sorted list. The function then prints this count for each test case.

