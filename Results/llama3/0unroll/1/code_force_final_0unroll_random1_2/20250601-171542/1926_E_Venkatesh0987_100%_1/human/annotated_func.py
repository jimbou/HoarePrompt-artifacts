#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: The output state will be a series of integers, each representing the result of the calculation for the corresponding input pair (n, k). The number of integers in the output state will be equal to the value of t, which is the number of input pairs. Each integer will be the result of the calculation 2 * k - 1 if k is less than or equal to (n + 1) // 2, or 2

#Overall this is what the function does:Calculates and prints the result of a mathematical operation for each input pair (n, k), where the result is either 2 * k - 1 if k is less than or equal to (n + 1) // 2, or a more complex calculation involving powers of 2 and the difference between k and a cumulative sum of rounded halves of n, for a specified number of input pairs t.

