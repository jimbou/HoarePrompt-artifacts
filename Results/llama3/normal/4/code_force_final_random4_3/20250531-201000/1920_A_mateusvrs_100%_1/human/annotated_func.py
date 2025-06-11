#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
        if bx > ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: t is 0, r is a list containing t elements, n is an integer between 2 and 100, stdin contains no test cases, _ is n-1. ax is the minimum of all x values where a is 2, bx is the maximum of all x values where a is 1, cx is a set containing all x values where a is not 1 or 2. If bx > ax, then r contains 0. Otherwise, r contains ax - bx + 1 - tmp, where tmp is the number of elements in cx that are within the range of bx and ax (inclusive), and cx is an empty set.
    print(*r, sep='\n')
    #This is printed: (nothing, because r is an empty list)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then processes each test case by finding the maximum x value where a is 1, the minimum x value where a is 2, and the set of x values where a is neither 1 nor 2. If the maximum x value where a is 1 is greater than the minimum x value where a is 2, it appends 0 to the result list. Otherwise, it appends the difference between the minimum x value where a is 2 and the maximum x value where a is 1, plus 1, minus the number of x values in the set that are within the range of the maximum x value where a is 1 and the minimum x value where a is 2 (inclusive). Finally, it prints the result list, with each element on a new line.

