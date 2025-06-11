#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
    t = int(input())
    r = []
    for _ in range(t):
        n = int(input())
        
        cx = set()
        
        ax = int(1000000000.0 + 7)
        
        bx = -1
        
        for _ in range(n):
            a, x = map(int, input().split())
            if a == 1:
                bx = max(x, bx)
            elif a == 2:
                ax = min(x, ax)
            else:
                cx.add(x)
        
        if bx >= ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: Output State: t is an integer, r is a list containing the number of integers in the range [bx, ax] that are not in cx for each test case, stdin is empty.
    print(*r, sep='\n')
    #This is printed: The number of integers in the range [bx, ax] that are not in cx for each test case, printed on separate lines

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then processes each test case to find the number of integers in the range [bx, ax] that are not in the set cx, where bx is the maximum x value for a=1, ax is the minimum x value for a=2, and cx is the set of x values for a=3. The function prints the result for each test case on a separate line.

