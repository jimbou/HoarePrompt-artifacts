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
        
        if bx >= ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: t is 0, r is a list containing t elements, n is 0, _ is 0, a is an integer, x is an integer, ax is the minimum of the initial value of ax and all x values where a is 2, bx is the maximum of the initial value of bx and all x values where a is 1, cx is a set containing all x values where a is neither 1 nor 2, and stdin is empty. If bx is greater than or equal to ax, all elements in r are 0. Otherwise, all elements in r are ax - bx + 1 - tmp, and tmp is the count of elements in cx that are within the range of bx and ax.
    print(*r, sep='\n')
    #This is printed: (empty output)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then processes each test case by maintaining the maximum value of x when a is 1, the minimum value of x when a is 2, and a set of x values when a is 3. If the maximum value of x when a is 1 is greater than or equal to the minimum value of x when a is 2, it appends 0 to the result list. Otherwise, it appends the difference between the minimum value of x when a is 2 and the maximum value of x when a is 1, plus 1, minus the count of x values in the set that fall within this range. Finally, it prints the result list, one element per line.

