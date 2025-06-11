#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers a and b (1 <= a, b <= 10^9).
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
        
    #State: `T` is at least `T`, `i` is `T-1`, `a` and `b` are integers between 1 and 10^9 inclusive, stdin contains multiple test cases minus `T+1` test cases. If `a` equals `b`, 'Bob' is printed. If `a` is not equal to `b`, then if `a` is 1, 'Alice' is printed. If `a` is not 1, then if `b` is 1, 'Bob' is printed. If `b` is not 1, then if `a` is odd, 'Bob' is printed. If `a` is even, then if `b` is odd, 'Alice' is printed. Otherwise, if `a` is greater than `b`, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:Determines the winner of a game based on the values of two integers, a and b, and prints the result. The function takes no parameters and returns no value. It reads input from stdin, processes multiple test cases, and prints 'Alice' or 'Bob' depending on the values of a and b. The function's output is based on the following rules: if a equals b, the winner is 'Bob'; if a is 1, the winner is 'Alice'; if b is 1, the winner is 'Bob'; if a is odd, the winner is 'Bob'; if a is even and b is odd, the winner is 'Alice'; if a is greater than b, the winner is 'Bob'; otherwise, the winner is 'Alice'.

