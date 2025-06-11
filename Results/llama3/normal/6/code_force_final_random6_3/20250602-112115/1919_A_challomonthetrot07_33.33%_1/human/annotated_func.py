#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9) — the number of coins in Alice's and Bob's wallets, respectively.
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: `T` is an integer between 1 and 1000 (inclusive), stdin is empty, `i` is `T-1`, `a` and `b` are integers, `a` and `b` are assigned the values of the two integers from the input, If `a` is equal to `b`, 'Bob' is printed. If `a` is not equal to `b`, then if `a` is 1, 'Alice' is printed. If `a` is not 1, then if `b` is 1, 'Bob' is printed. If `b` is not 1, then if `a` is odd, 'Bob' is printed. If `a` is even, then if `b` is odd, 'Alice' is printed. Otherwise, if `a` is greater than `b`, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers representing the number of coins in Alice's and Bob's wallets. It then determines the winner of each case based on a set of predefined rules and prints the winner's name. The rules are as follows: if the number of coins is equal, Bob wins; if Alice has one coin, she wins; if Bob has one coin, he wins; if Alice has an odd number of coins, Bob wins; if Alice has an even number of coins and Bob has an odd number, Alice wins; if Alice has more coins than Bob, Bob wins; otherwise, Alice wins. The function processes all test cases and prints the winner for each case.

