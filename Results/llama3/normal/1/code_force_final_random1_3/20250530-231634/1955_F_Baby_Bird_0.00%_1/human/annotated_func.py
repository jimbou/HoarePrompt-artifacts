#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: `stdin` contains 0 lines, `p` is a list of four even integers where each integer is either 0 or an even number between 2 and 200, `_` is `t-1`, `t` must be greater than or equal to 1, and this is printed: False and the sum of all elements in the list `p` divided by 2.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It then processes each test case by rounding down the integers to the nearest even number, checks if the first three integers are odd (and if so, prints True), and finally prints the sum of all four integers divided by 2. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

