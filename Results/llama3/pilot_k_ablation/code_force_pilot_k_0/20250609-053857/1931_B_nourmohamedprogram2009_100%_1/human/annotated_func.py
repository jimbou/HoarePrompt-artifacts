#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t blocks of two lines, where the first line of each block contains an integer n (1 <= n <= 2 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        total_water = sum(a)
        
        target = total_water // n
        
        current_balance = 0
        
        possible = True
        
        for i in range(n):
            current_balance += a[i] - target
            if current_balance < 0:
                possible = False
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output state will be a series of 'YES' or 'NO' printed to the console, where each 'YES' or 'NO' corresponds to whether it is possible to distribute the water in the current block of input such that each person gets an equal amount of water. The number of 'YES' or 'NO' printed will be equal to t-1, and the values of t, n, a, total_water, target, current_balance, and possible will be reset after each iteration of the loop.

#Overall this is what the function does:This function reads input from the standard input, processes it in blocks, and prints 'YES' or 'NO' to the console for each block. Each block consists of an integer n followed by n integers. The function checks if it's possible to distribute the sum of the n integers equally among n people. If it's possible, it prints 'YES'; otherwise, it prints 'NO'. The function repeats this process for a number of blocks specified by the first integer input.

