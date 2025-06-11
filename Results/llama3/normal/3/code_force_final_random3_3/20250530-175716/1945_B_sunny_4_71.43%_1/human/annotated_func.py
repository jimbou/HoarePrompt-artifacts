#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: t is an integer (1 <= t <= 10^4) and is equal to 0, stdin contains 0 lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18), a is an integer (1 <= a <= 10^18), b is an integer (1 <= b <= 10^18), m is an integer (1 <= m <= 10^18), A is an integer equal to int(m / a) + 1, B is an integer equal to int(m / b) + 1, and the sum of A and B which is equal to (int(m / a) + 1) + (int(m / b) + 1) is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. For each case, it calculates the sum of the smallest integers A and B such that A is greater than or equal to m/a and B is greater than or equal to m/b, and prints this sum. The function continues this process until all test cases have been read from standard input.

