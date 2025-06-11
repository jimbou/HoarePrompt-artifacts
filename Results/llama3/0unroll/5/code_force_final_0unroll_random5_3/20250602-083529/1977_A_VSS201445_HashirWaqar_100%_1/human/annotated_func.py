#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The output state contains multiple lines of output. The number of lines is equal to the value of t in the initial state. Each line contains either 'YES' or 'NO'. 'YES' is printed if n is greater than or equal to m and the difference between n and m is even. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and m. It then prints 'YES' or 'NO' for each pair of n and m, depending on whether n is greater than or equal to m and their difference is even. The function outputs t lines, each containing either 'YES' or 'NO', indicating whether the conditions are met for each input pair.

