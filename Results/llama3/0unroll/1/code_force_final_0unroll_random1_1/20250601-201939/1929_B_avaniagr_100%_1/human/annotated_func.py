#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The output state contains t lines, each containing a single integer. The integer on each line is the result of the calculations performed on the corresponding input line. Specifically, for each input line with values n and k, the output line contains the smallest integer greater than or equal to k/2 if k is less than or equal to 4n-4, 2n-1 if k is equal to 4n-3, or 2n if k is equal to 4n-2.

#Overall this is what the function does:The function reads input from stdin, processes multiple lines of input, and prints the results to stdout. It accepts no parameters and returns no value. The input is expected to contain a series of lines, where the first line contains a single integer t, and each subsequent line contains two integers n and k. The function calculates and prints the smallest integer greater than or equal to k/2 if k is less than or equal to 4n-4, 2n-1 if k is equal to 4n-3, or 2n if k is equal to 4n-2, for each input line. The output contains t lines, each with a single integer result.

