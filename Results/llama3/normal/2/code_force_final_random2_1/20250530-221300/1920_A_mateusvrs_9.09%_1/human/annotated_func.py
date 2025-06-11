#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9). a denotes the type of constraint. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x.
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
        
    #State: `t` is 0, `r` is a list containing `t` elements, `_` is `n`, `n` is an integer, `ax` is an integer, `bx` is an integer, `cx` is a set, `a` is an integer, `x` is an integer, and stdin contains no input. If `bx` is greater than or equal to `ax`, then `r` contains `t` zeros. Otherwise, `r` contains `t` elements, each of which is `ax - bx + 1 - tmp`, where `tmp` is the number of elements in `cx` that are greater than or equal to `bx` and less than or equal to `ax` if all elements in `cx` are within this range, or the number of elements in `cx` that meet this condition otherwise.
    print(*r, sep='\n')
    #This is printed: (empty output)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of two integers a and x. It then processes these test cases to determine the number of possible values of k that satisfy certain constraints. The constraints are: if a=1, k must be greater than or equal to x; if a=2, k must be less than or equal to x; and if a=3, k must not be equal to x. The function returns a list of integers, where each integer represents the number of possible values of k for the corresponding test case. If there are no possible values of k for a test case, the function returns 0 for that test case.

