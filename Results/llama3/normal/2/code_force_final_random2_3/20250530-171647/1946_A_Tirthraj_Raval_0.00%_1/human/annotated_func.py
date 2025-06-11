#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: t is equal to 0, n is an integer equal to the input value, a is a sorted list of integers equal to the input list, p is an integer equal to the index of the middle element in the sorted list a, res is the count of the middle element in the sorted list a, stdin contains multiple test cases minus t, and the count of the middle element in the sorted list a is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by a list of n integers. It sorts the list of integers, finds the middle element, counts its occurrences, and prints the count. The function processes all test cases and prints the count of the middle element for each case.

