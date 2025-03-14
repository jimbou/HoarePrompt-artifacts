#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 * 10^5), and y is an integer such that 0 ≤ y ≤ n - x. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 * 10^5.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, x, y = R()
        
        sx = 0
        
        l = list(R())
        
        l.sort()
        
        l.append(n + l[0])
        
        val = []
        
        for i in range(1, x + 1):
            c = l[i] - l[i - 1] - 1
            val.append(c)
        
        val.sort(key=lambda x: (1 - x & 1, x))
        
        for i in val:
            c = i // 2
            if y < c:
                sx += y * 2
                break
            sx += i
            y -= c
        
        cons = x + sx - 2
        
        print(cons)
        
    #State: After all iterations of the loop, the variable `t` will be `0`, indicating that all test cases have been processed. The variables `n`, `x`, `y`, `l`, `sx`, `val`, and `cons` will hold the values from the last test case processed. However, since the problem asks for the output state after all executions of the loop, we focus on the printed results for each test case.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `x`, and `y`, and a list of `x` distinct integers representing chosen vertices. For each test case, it calculates and prints a value `cons` based on the given inputs, which represents the number of connections or modifications required among the chosen vertices.

