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
        
    #State: t is 0, r is a list containing t elements, stdin contains no input, n is an integer, a is an integer, x is an integer, bx is either -1 or the maximum of its previous value and x, ax is either the minimum of x and 1000000007 or 1000000007, cx is either an empty set, a set containing one element which is x, or a set containing multiple elements which are x and other elements, tmp is the total number of elements in cx that are within the range of bx and ax (inclusive).
    print(*r, sep='\n')
    #This is printed: the elements of the list r (where r is a list containing t elements and t is 0)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then processes each test case by finding the maximum value of x when a is 1, the minimum value of x when a is 2, and storing all x values when a is 3. If the maximum value of x when a is 1 is greater than the minimum value of x when a is 2, it appends 0 to the result list. Otherwise, it counts the number of x values within the range of the maximum and minimum x values (inclusive) and subtracts this count from the difference between the maximum and minimum x values plus 1, appending the result to the list. Finally, it prints the elements of the result list, each on a new line.

