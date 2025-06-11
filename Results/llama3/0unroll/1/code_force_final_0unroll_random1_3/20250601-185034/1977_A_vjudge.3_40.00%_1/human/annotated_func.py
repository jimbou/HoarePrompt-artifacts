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
        
    #State: The output state will be a series of 'Yes' or 'No' printed to the console, one for each line of input. The output will be 'Yes' if the numbers n and m are equal, or if they are both even or both odd, or if m is one less than n. Otherwise, the output will be 'No'.

#Overall this is what the function does:Determines and prints whether two given integers are equal, both even or both odd, or if one is one less than the other, for multiple test cases.

