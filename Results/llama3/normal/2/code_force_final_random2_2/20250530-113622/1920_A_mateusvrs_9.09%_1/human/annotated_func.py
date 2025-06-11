#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case starts with an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
    #State: t is 0, n is 0, ax is the minimum of 1000000007 and all x values where a is 2, bx is the maximum of -1 and all x values where a is 1, cx is a set containing all x values where a is not 1 or 2, r is a list containing t integers where each integer is the difference between ax and bx plus 1 minus the number of integers in cx that are between bx and ax inclusive, stdin contains 0 test cases, a is an integer between 1 and 100 inclusive, x is an integer between -1000000000 and 1000000000 inclusive.
    print(*r, sep='\n')
    #This is printed: (nothing)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It accepts no parameters and returns no values. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n, representing the number of lines, followed by n lines, each containing two integers a and x. The function processes each test case by maintaining the minimum value of x when a is 2, the maximum value of x when a is 1, and a set of x values when a is 3. It then calculates the difference between the minimum and maximum x values plus 1, minus the number of x values in the set that fall within this range. The function stores these results in a list and prints them at the end. The final state of the program is that the input has been processed, and the results have been printed to stdout.

