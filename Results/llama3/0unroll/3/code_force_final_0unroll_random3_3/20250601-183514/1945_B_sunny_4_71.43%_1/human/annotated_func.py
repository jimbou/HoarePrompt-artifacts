#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The output will be the sum of the ceiling of m/a and m/b for each test case, printed on a new line for each test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. For each test case, it calculates the sum of the ceiling of m/a and m/b, and prints this sum on a new line. The function processes all test cases and produces the corresponding output.

