#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: `n` is an integer, `l` is a sorted list of integers, `score` is equal to the sum of every other element of `l` starting from the first element, `stdin` is empty, `i` is equal to 2 * `n`, `_` is equal to `t`, and the score which is the sum of every other element of `l` starting from the first element is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It sorts the integers in ascending order, calculates the sum of every other integer starting from the first, and prints this sum. The function processes all test cases and then terminates, leaving the standard input empty.

