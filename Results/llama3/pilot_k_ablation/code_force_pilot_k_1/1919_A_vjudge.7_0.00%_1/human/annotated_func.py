#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two space-separated integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: `_rep` is equal to `t`, `t` is 0, stdin is empty, the number of 'Alice' printed is equal to the number of times `n` is less than `k` in the input, the number of 'Bob' printed is equal to the number of times `n` is greater than or equal to `k` in the input.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each of the following t lines contains two space-separated integers a and b. It then compares each pair of integers and prints 'Alice' if a is less than b, 'Bob' if a is greater than or equal to b. The function continues this process until all t lines have been processed, leaving stdin empty.

