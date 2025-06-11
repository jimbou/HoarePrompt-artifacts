#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with a line containing a single integer n (2 <= n <= 100) — the number of constraints. The following n lines describe the constraints. Each line contains two integers a and x (a ∈ {1,2,3}, 1 <= x <= 10^9). a denotes the type of constraint. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x. The first line contains a single integer t (1 <= t <= 500) — the number of test cases.
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
        
    #State: Output State: The list r contains t integers, each representing the number of integers in the range [bx, ax] that are not in the set cx for each test case. The value of t remains unchanged, still a positive integer between 1 and 500.
    print(*r, sep='\n')
    #This is printed: t integers, each representing the number of integers in the range [bx, ax] that are not in the set cx for each test case, separated by newline characters

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a set of constraints defining a range of valid integers. It then calculates and prints the number of integers within this range that do not violate any of the given constraints, for each test case.

