#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9). a denotes the type of constraint. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x. The first line contains a single integer t (1 <= t <= 500) — the number of test cases.
    loop = int(input())
    for iterable in range(loop):
        less = []
        
        big = []
        
        no = []
        
        num = 0
        
        innerLoop = int(input())
        
        for iterable2 in range(innerLoop):
            x, a = map(int, input().split())
            if x == 1:
                big.append(a)
            elif x == 2:
                less.append(a)
            else:
                no.append(a)
        
        for i in range(max(big), min(less)):
            if i not in no:
                num = i
                break
        
        print(num)
        
    #State: `big` is a list that must have at least one integer, `less` is a list that must have at least one integer and all integers in `less` are greater than all integers in `big`, `num` is equal to the current value of `i`, `innerLoop` is an integer, `iterable` is incremented by `innerLoop` if `i` is not in `no`, `iterable2` is `innerLoop - 1`, `x` is an integer, `a` is an integer, `i` is either in the list `no` or not and is increased by 1 if not in `no` and must be less than `min(less)` for the loop to execute again. If `i` is not in `no`, `i` is increased by 1. Otherwise, `i` remains unchanged., and the current value of `i` which is equal to `num` is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of two integers a and x. It categorizes the constraints based on the value of a (1, 2, or 3) and finds the smallest integer k that satisfies all the constraints. The function prints the value of k for each test case.

