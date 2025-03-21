#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2⋅10^5. The first line of each test case contains three integers n, x, and y. The second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: The output state will be the sum of `x + sx - 2` for each iteration of the loop, where `sx` is calculated based on the operations within the loop.
    #
    #To understand this output state, let's break down the process:
    #
    #1. **Initialization**: The variable `t` is initialized to the first element of the tuple returned by `R()`, which is a positive integer between 1 and 10^4.
    #
    #2. **Loop Execution**:
    #   - In each iteration, `t` is decremented by 1.
    #   - New values `n`, `x`, and `y` are obtained from `R()`.
    #   - A list `l` is created from `R()` and sorted.
    #   - The list `l` is modified by appending `n + l[0]`.
    #   - A list `val` is created by calculating the differences between consecutive elements of `l` and storing them.
    #   - `val` is sorted based on specific criteria.
    #   - A value `sx` is computed by iterating over `val` and adding up values until `y` is less than half of the current value in `val`.
    #   - Finally, `cons` is calculated as `x + sx - 2` and printed.
    #
    #3. **Final Output**: After all iterations of the loop, the final output state will be the cumulative sum of `x + sx - 2` for each iteration.
    #
    #The exact numerical value of the output state cannot be determined without knowing the specific values returned by `R()` at each step, but it will always be a non-negative integer resulting from the described operations.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads three integers \( n \), \( x \), and \( y \), and a list of \( x \) distinct integers from 1 to \( n \). It calculates a value \( sx \) based on the differences between consecutive elements in the sorted list and a condition involving \( y \). Finally, it computes and prints \( cons \) as \( x + sx - 2 \) for each test case. The function does not return any value but outputs the result for each test case.

