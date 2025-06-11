#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The output state will contain t lines, each containing an integer that is the result of the calculation (k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2) for the corresponding input values of n and k.

#Overall this is what the function does:Calculates and prints the result of a mathematical expression for each pair of input integers n and k, where the result depends on the values of k and n, and prints the results in t lines, where t is the number of input pairs.

