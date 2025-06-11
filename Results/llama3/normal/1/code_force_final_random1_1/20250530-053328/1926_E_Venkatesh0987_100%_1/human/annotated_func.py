#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 5 ⋅ 10^4). Each of the following t lines contains two integers n and k (1 ≤ k ≤ n ≤ 10^9).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: The loop has executed the specified number of times, and the output state is determined by the final values of the variables in the loop head and body.

#Overall this is what the function does:Calculates and prints the minimum number of operations required to reach a target value k from an initial value n, where the operation involves either doubling the current value or adding 1 to it, for a specified number of test cases.

