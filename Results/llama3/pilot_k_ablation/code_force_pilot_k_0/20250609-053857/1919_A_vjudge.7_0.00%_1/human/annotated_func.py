#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: The loop will print 'Bob' for each pair of integers where n is greater than or equal to k, and 'Alice' for each pair where n is less than k. The value of t remains unchanged.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, compares each pair, and prints 'Bob' if the first integer is greater than or equal to the second, and 'Alice' otherwise. The function does not modify the input values or return any values, only producing output based on the comparisons.

