#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The program will print 'Yes' or 'No' for each pair of integers, depending on whether at least one of the integers is even. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads multiple pairs of integers from standard input and prints 'Yes' if at least one integer in each pair is even, otherwise prints 'No'. The function does not modify the input values or return any values, only producing output based on the input pairs.

