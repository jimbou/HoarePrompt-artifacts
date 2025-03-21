#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. Each of the following n lines contains two integers a and x where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. a = 1 indicates k must be greater than or equal to x, a = 2 indicates k must be less than or equal to x, and a = 3 indicates k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
def func():
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
        
        num = min(less) - max(big) + 1
        
        if num < 1:
            print(0)
            continue
        
        for i in no:
            if i <= min(less) and i >= max(big):
                num -= 1
        
        print(num)
        
    #State: The program has processed all `t` test cases and printed the number of valid integers `k` for each test case based on the given constraints.
#Overall this is what the function does:The function processes multiple test cases, each consisting of several constraints on an integer `k`. For each test case, it calculates and prints the number of valid integers `k` that satisfy all the given constraints. Constraints can specify that `k` must be greater than or equal to, less than or equal to, or not equal to certain values.

