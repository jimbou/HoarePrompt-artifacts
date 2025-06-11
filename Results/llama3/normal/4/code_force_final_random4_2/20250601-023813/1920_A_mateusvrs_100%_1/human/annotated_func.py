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
        
    #State: t is 0, r is a list containing t elements, stdin is empty, _ is n, n is an integer greater than or equal to 0, a is an integer, x is an integer, ax is the minimum of 1000000007 and the minimum of all x values when a is 2, bx is the maximum of -1 and the maximum of all x values when a is 1, cx is a set containing all x values when a is not 1 and not 2. If bx > ax, then the current value of bx is greater than the current value of ax. Otherwise, i is the last element in the set cx, bx is less than or equal to ax, tmp is the number of elements in cx that are greater than or equal to bx and less than or equal to ax, and the last element in r is ax - bx + 1 - tmp.
    print(*r, sep='\n')
    #This is printed: the last element in the list r which is ax - bx + 1 - tmp (where ax is the minimum of 1000000007 and the minimum of all x values when a is 2, bx is the maximum of -1 and the maximum of all x values when a is 1, and tmp is the number of elements in cx that are greater than or equal to bx and less than or equal to ax)

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then processes each test case by finding the maximum x value when a is 1, the minimum x value when a is 2, and the set of x values when a is not 1 or 2. If the maximum x value when a is 1 is greater than the minimum x value when a is 2, it appends 0 to the result list. Otherwise, it calculates the number of x values in the set that are within the range of the minimum and maximum x values and appends the difference between the maximum and minimum x values plus 1 minus this count to the result list. Finally, it prints the result list.

