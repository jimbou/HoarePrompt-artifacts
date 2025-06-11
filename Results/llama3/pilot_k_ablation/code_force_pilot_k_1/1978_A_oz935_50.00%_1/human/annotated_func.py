#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: t is an integer between 1 and 500 (inclusive), i is t-1, stdin is empty, n is an integer between 2 and 100 (inclusive), ls is an empty list, last is the last integer in the last test case, other is the second largest integer in the last test case (excluding the last integer), and the sum of last and other has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it identifies the last integer and the second largest integer (excluding the last one), and prints their sum. The function processes multiple test cases as specified by the initial input t, and consumes all input from standard input.

