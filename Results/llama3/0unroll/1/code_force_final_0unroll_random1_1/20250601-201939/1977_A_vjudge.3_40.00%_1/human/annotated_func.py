#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: The output will be a series of 'Yes' or 'No' for each pair of integers (n, m) in the input, indicating whether m is less than or equal to n and either both are even or both are odd, or if m is one less than n. The value of t will remain unchanged.

#Overall this is what the function does:Determines and prints whether a given integer m is less than or equal to n and either both are even or both are odd, or if m is one less than n, for multiple pairs of integers (n, m) provided as input, without modifying the input count t.

