#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9). There exists at least one constraint of type 1 and at least one constraint of type 2. No two constraints are the exact same.
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
        
    #State: Output State: t is an integer, r is a list of integers.
    print(*r, sep='\n')
    #This is printed: the elements of the list r, one element per line

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It processes each test case by finding the maximum value of x for constraints of type 1, the minimum value of x for constraints of type 2, and a set of x values for constraints of type 3. If the maximum value of x for type 1 constraints is greater than or equal to the minimum value of x for type 2 constraints, it outputs 0. Otherwise, it calculates the number of integers in the range from the maximum value of x for type 1 constraints to the minimum value of x for type 2 constraints, excluding the x values for type 3 constraints, and outputs this count. The function repeats this process for all test cases and prints the results, one per line.

