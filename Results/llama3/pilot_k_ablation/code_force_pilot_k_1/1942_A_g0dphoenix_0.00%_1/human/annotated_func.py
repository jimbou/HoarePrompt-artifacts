#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        else:
            print(-1)
        
    #State: stdin is empty, and the output contains t lines, each containing either a string of '1 ' repeated n times (where n is equal to k) with the last space removed, or -1, depending on whether n is equal to k for each input pair (n, k).

#Overall this is what the function does:This function reads a series of input pairs (n, k) from stdin, where each pair is on a new line, and prints either a string of '1 ' repeated n times (with the last space removed) if n equals k, or -1 if n does not equal k, for each input pair. The function continues this process until all input pairs have been processed, resulting in an empty stdin and an output containing the corresponding results for each pair.

