#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18).
    """t=int(input())
    for _ in range(t):
        a,b,m=map(int,input().split())
        A=int(m/a)+1
        B=int(m/b)+1
        print(A+B)"""
    t = int(input())
    for qi in range(t):
        a, b, m = [int(x) for x in input().split()]
        
        ans = m // a + m // b + 2
        
        print(ans)
        
    #State: qi is t-1, t is an integer between 1 and 10^4, a is an integer between 1 and 10^18, b is an integer between 1 and 10^18, m is an integer between 1 and 10^18, ans is an integer equal to m // a + m // b + 2, stdin is empty, and ans which is m // a + m // b + 2 is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. For each test case, it calculates the sum of the integer divisions of m by a and m by b, adds 2 to the result, and prints the final value. The function processes all test cases and then terminates, leaving the standard input empty.

