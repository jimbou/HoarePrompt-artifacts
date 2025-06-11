#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains one integer t (1 <= t <= 1000). Each of the following t blocks of two lines contains an integer n (2 <= n <= 50) and a list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1.
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
        
    #State: t is an integer between 1 and 1000 and greater than or equal to 0, stdin contains 0 lines, n is an integer between 2 and 50, a is a non-empty list of integers (0 <= a_i <= 1) where at least one a_i is 1, the first element is 1, and the last element is not 0, i is equal to the length of a, and res is equal to the number of zeros in a, and the number of zeros in a which is equal to res is being printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of zeros in each list of integers. It expects the input to start with an integer t, representing the number of test cases, followed by t blocks of two lines. Each block contains an integer n, representing the length of the list, and a list of n integers (0s and 1s) where at least one integer is 1. The function removes leading and trailing zeros from each list, counts the remaining zeros, and prints this count for each list. After processing all test cases, the function concludes, leaving stdin empty.

