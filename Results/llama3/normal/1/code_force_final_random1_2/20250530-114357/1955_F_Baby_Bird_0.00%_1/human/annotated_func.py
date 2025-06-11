#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The loop head variable `_` is equal to `int(input()) - 1`, `p` is a list of four even integers, stdin contains an integer t (1 <= t <= 10^4) followed by 0 lines, each containing four integers p_i (0 <= p_i <= 200), and the sum of the first three elements of `p` modulo 2, plus the sum of all elements in `p` divided by 2 is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four integers. It then calculates and prints the sum of the first three integers modulo 2, plus the sum of all four integers divided by 2, for each test case. The function repeats this process for a number of test cases specified by the first integer read from standard input.

