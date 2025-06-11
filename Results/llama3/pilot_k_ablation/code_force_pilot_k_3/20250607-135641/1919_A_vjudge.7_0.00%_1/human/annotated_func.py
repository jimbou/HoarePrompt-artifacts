#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) — the number of coins in Alice's and Bob's wallets, respectively.
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `n` is an integer between 1 and 10^9 (inclusive), `k` is an integer between 1 and 10^9 (inclusive), `_rep` is `t-1`, stdin contains no lines of input. If `n` is greater than `k`, 'Bob' is printed `t-1` times. If `n` is less than `k`, 'Alice' is printed `t-1` times. If `n` is equal to `k`, 'Bob' is printed `t-1` times.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines the winner based on the number of coins in Alice's and Bob's wallets. It prints the winner's name ('Alice' or 'Bob') for each test case, with 'Bob' being the default winner in case of a tie. The function consumes all input from stdin and does not return any value.

