#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) — the number of coins in Alice's and Bob's wallets, respectively.
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `i` is `t-1`, `a` and `b` are integers between 1 and 10^9 (inclusive) and are assigned the values of the last two integers from the input, stdin contains multiple lines of input, each containing two integers a and b (1 <= a, b <= 10^9), minus `t` lines of input that have been read. If the absolute difference between `a` and `b` is even, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:Determines the winner of a series of coin comparisons between Alice and Bob, where the winner is decided based on whether the absolute difference between the number of coins in their wallets is even or odd, and prints the winner's name for each comparison.

