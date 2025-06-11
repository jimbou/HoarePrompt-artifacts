#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: The loop has finished executing, and the output state is the final state after all iterations. The loop has processed all the input lines, and the output is a series of lists or -1 values, depending on the values of `n` and `k` in each input line. The stdin contains no more lines, and the loop has terminated.

#Overall this is what the function does:This function reads input from stdin, processes each line containing two integers n and k, and prints a list of numbers or -1 based on the values of n and k. If k is 1, it prints a list of numbers from 0 to n-1. If k is greater than 1, it prints a list of k repeated k times if n equals k, otherwise it prints -1. The function continues processing input lines until all lines have been read from stdin, resulting in a series of lists or -1 values as output.

