#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case contains an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: t is an integer between 1 and 500 inclusive, i is t-1, n is an integer, last is an integer, other is an integer, ls is an empty list, and the sum of last and other is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it extracts the last integer and the largest of the remaining integers, and prints their sum. The function processes multiple test cases, as specified by an initial integer t, and does not return any value, only producing output for each test case.

