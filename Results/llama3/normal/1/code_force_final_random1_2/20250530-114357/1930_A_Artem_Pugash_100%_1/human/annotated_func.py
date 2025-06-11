#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 <= a_i <= 10^7).
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: `n` is 0, `i` is 0, `l` is an empty list, `score` is 0, `_` is `t`, `stdin` is empty, and the sum of every other element of `l` starting from the first one which is `score` is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It calculates the sum of every other integer in each test case, starting from the first one, and prints this sum. The function processes all test cases and then terminates, leaving the input stream empty.

