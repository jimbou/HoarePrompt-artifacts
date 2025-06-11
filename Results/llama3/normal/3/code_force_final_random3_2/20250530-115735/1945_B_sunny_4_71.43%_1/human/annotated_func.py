#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: t is an integer between 1 and 10^4 (inclusive), stdin is empty, a, b, and m are integers (1 <= a, b, m <= 10^18), A is an integer equal to int(m / a) + 1, B is an integer equal to int(m / b) + 1, and the sum of A and B is printed which is equal to int(m / a) + 1 + int(m / b) + 1

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. For each test case, it calculates the ceiling of the division of m by a and b, adds 1 to each result, and prints their sum. The function processes all test cases and leaves the standard input empty.

