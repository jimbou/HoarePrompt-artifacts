#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: stdin is empty, _ is equal to the initial value of t, for each pair of n and m, if n is less than m, 'NO' is printed, if n is larger than or equal to m, 'YES' is printed if both n and m are either odd or even.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair consists of two numbers n and m. It then checks each pair and prints 'YES' if n is greater than or equal to m and both n and m are either both odd or both even, otherwise it prints 'NO'. The function continues this process until all pairs have been read from standard input, at which point the input is empty.

