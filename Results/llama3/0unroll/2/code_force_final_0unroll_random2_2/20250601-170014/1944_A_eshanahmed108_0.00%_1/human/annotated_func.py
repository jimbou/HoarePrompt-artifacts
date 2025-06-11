#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: The output will be a series of integers, each representing the result of the calculation for the corresponding input pair (n, k). The result will be 1 if n - k is greater than 1, and n otherwise.

#Overall this is what the function does:The function reads a series of input pairs (n, k) from the standard input, where n and k are integers, and prints the result of a calculation for each pair. The result is 1 if n - k is greater than 1, and n otherwise. The function processes multiple input pairs, as specified by an initial integer t, and outputs the results in a series of integers.

