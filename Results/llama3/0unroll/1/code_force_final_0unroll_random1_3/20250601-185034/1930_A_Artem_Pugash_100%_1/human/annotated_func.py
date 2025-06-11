#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= 10^7).
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The output state will contain t lines, each containing the sum of the smallest n numbers in the corresponding test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. For each test case, it sorts the 2n integers, calculates the sum of the smallest n numbers, and prints this sum. The function repeats this process for all test cases, producing a total of t output lines, where t is the number of test cases specified at the beginning of the input.

