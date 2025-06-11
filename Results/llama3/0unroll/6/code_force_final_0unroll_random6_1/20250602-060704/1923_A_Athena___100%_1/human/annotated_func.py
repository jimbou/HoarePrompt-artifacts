#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where at least one a_i is 1.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: The number of zeros in the input list, excluding leading and trailing zeros, is printed for each test case. The input list is modified by removing leading and trailing zeros. The variable 't' remains unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a list of integers. It then removes leading and trailing zeros from each list, counts the number of remaining zeros, and prints this count for each test case. The original input lists are modified in the process. The function does not return any value, but instead prints the results directly to the console.

