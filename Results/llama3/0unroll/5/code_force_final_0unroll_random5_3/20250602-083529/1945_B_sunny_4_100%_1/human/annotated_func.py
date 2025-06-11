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
        
    #State: The standard output contains t lines, each containing an integer which is the value of the variable ans in the last iteration of the loop. The values of t, a, b, and m remain unchanged.

#Overall this is what the function does:Reads a series of input lines, each containing three integers a, b, and m, and prints the sum of the integer divisions of m by a and b, plus 2, for each input line.

