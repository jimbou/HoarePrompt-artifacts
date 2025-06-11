#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
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
        
    #State: t is an integer between 1 and 10^4, qi is t-1, a is an integer, b is an integer, m is an integer, ans is an integer equal to m // a + m // b + 2, stdin is empty, and the value of ans which is equal to m // a + m // b + 2 is being printed

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads three integers a, b, and m, and calculates the sum of the integer divisions of m by a and m by b, adding 2 to the result. The function then prints this calculated value for each test case. The function does not return any value, and its purpose is to output the calculated sums for the given input test cases.

