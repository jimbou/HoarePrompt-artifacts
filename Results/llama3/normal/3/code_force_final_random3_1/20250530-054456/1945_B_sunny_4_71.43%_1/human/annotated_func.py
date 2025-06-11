#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: t is equal to 0, _ is equal to t, stdin is empty, a is an integer equal to the last value of a, b is an integer equal to the last value of b, m is an integer equal to the last value of m, A is an integer equal to ((m/a)+1), B is an integer equal to ((m/b)+1), and the sum of A and B is printed which is equal to ((m/a)+1) + ((m/b)+1)

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. For each case, it calculates the smallest integer greater than or equal to m/a and m/b, adds these two values together, and prints the result. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

