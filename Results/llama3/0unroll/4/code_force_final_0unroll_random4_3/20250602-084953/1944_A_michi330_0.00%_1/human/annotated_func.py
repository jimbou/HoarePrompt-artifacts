#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop will print t lines, each containing either 1 or n-1, where n is the first integer in the corresponding line of stdin. The value printed will be 1 if k is greater than or equal to n-1, and n-1 otherwise.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t lines, each containing two integers n and k. It then prints t lines, each containing either 1 or n-1, depending on whether k is greater than or equal to n-1. If k is greater than or equal to n-1, it prints 1; otherwise, it prints n-1. The function does not modify the input values and only prints the calculated values to standard output.

