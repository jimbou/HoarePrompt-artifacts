#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4), then t pairs of integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: The output state will be a list of t integers, each representing the result of the calculation (2 * (k - s) - 1) * m for the corresponding input pair (n, k). The value of t remains unchanged, as it is not modified within the loop.

#Overall this is what the function does:This function reads a series of input pairs (n, k) from stdin, where n and k are integers, and for each pair, it calculates and prints the result of the expression (2 * (k - s) - 1) * m, where s and m are intermediate values determined by a while loop. The function processes t such pairs, where t is also read from stdin, and outputs a list of t integers, each corresponding to the result of the calculation for the respective input pair.

