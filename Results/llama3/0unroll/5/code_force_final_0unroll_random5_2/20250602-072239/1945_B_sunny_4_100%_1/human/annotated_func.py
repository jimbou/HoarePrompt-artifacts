#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
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
        
    #State: t is an integer (1 <= t <= 10^4), stdin is empty, and the values of a, b, m, ans, and qi are undefined.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It then calculates and prints the sum of the integer divisions of m by a and m by b, plus 2, for each test case. The function consumes all input from standard input and leaves no values defined after execution.

