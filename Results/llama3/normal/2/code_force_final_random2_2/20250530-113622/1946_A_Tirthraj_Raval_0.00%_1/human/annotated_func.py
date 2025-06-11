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
        
    #State: t is 0, stdin contains no test cases, n is an integer equal to the number of elements in the list a, a is a sorted list of integers, p is an integer equal to (n + 1) // 2 - 1, res is an integer equal to the count of the middle element in the sorted list a, and the count of the middle element in the sorted list a which is equal to res is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It sorts the integers in ascending order, finds the middle element, counts its occurrences, and prints the count. The function processes all test cases and leaves the input stream empty.

