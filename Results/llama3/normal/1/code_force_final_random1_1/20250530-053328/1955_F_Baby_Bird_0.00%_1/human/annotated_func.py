#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: `p` is a list of four even integers between 0 and 200, `stdin` is empty, `int(input())` is 0, and `_` is equal to the initial value of `t`, and this is printed: 0 + sum of the list p divided by 2

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It then processes each test case by rounding down the integers to the nearest even number, checks if the first three numbers are odd (in which case it prints 1 plus half the sum of the four numbers), and otherwise prints half the sum of the four numbers. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

