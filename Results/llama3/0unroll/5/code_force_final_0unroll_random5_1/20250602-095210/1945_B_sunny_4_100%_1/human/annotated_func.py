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
        
    #State: Output State: The loop has executed t times, and for each iteration, the values of a, b, and m have been read from stdin, and the value of ans has been calculated and printed to stdout. The final state of the variables is: t is still an integer equal to the first integer read from stdin, stdin is empty, and the values of a, b, m, and ans are the values from the last iteration of the loop.

#Overall this is what the function does:Reads a series of test cases from standard input, where each case consists of three integers a, b, and m, and for each case, calculates and prints the sum of the integer divisions of m by a and m by b, plus 2, to standard output.

