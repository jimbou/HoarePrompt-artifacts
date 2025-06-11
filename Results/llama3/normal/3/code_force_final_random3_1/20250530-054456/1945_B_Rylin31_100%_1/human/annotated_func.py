#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: `t` is greater than or equal to 0, `i` is `t-1`, `a`, `b`, and `m` are integers where 1 <= a, b, m <= 10^18, stdin is empty, and the value of m // a + m // b + 2 is being printed, `a`, `b`, and `m` are assigned the values of the last set of three space-separated integers from the input, and this is printed: m // a + m // b + 2 (where a, b, and m are the last set of three space-separated integers from the input), and the value of m // a + m // b + 2 is printed for all sets of three space-separated integers from the input.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It then calculates and prints the value of m // a + m // b + 2 for each test case. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted. The function does not return any value, but instead prints the calculated values for each test case.

