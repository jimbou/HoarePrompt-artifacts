#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t, then t pairs of integers n and k, where n and k are positive integers and k <= n.
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
        
    #State: t is 0, _ is any value, n is 0, k is an integer, m is a power of 2, x is an integer equal to the original value of n plus 1 divided by 2, s is an integer equal to the sum of all x values from previous iterations, and the value of the expression (2 * (k - s) - 1) * m is being printed, where k is an integer, s is the sum of all x values from previous iterations, and m is a power of 2.

#Overall this is what the function does:This function reads input from the standard input (stdin) and processes it in batches. It expects the first input to be an integer t, representing the number of batches. For each batch, it reads a pair of integers n and k, where n and k are positive integers and k is less than or equal to n. The function then calculates and prints a value based on the given n and k. The calculation involves finding the sum of a series of numbers derived from n and k, and then using this sum to compute the final output. The function repeats this process for each batch until all t batches have been processed.

