#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
    #State: Output State: r is a list containing the number of integers in the range [bx, ax] that are not in cx for each test case, t is an integer, stdin is empty.
    print(*r, sep='\n')
    #This is printed: The count of integers in each range [bx, ax] that are not in cx, separated by newline characters

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of two integers a and x. It then processes each test case by finding the maximum value of x when a is 1, the minimum value of x when a is 2, and storing all x values when a is 3. If the maximum value of x when a is 1 is greater than the minimum value of x when a is 2, it appends 0 to the result list. Otherwise, it counts the number of integers in the range [bx, ax] that are not in the set of x values when a is 3 and appends this count to the result list. Finally, it prints the result list, with each count separated by a newline character.

