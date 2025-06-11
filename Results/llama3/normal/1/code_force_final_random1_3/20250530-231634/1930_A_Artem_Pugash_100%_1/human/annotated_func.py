#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= 10^7).
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The loop has finished executing, `t` test cases have been processed, `n` is an integer between 1 and 50, `l` is a sorted list of 2n integers between 1 and 10^7, `score` is the sum of all even-indexed elements in `l`, `i` is 2n, `2 * n` must be greater than or equal to 0, stdin is empty, and the sum of all even-indexed elements in `l` which is `score` has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It sorts the integers in ascending order, calculates the sum of the even-indexed elements, and prints this sum for each test case. The function processes all test cases and then terminates, leaving the standard input empty.

