#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer between 1 and 1000, `i` is `t`, `a` and `b` are integers (1 ≤ `a`, `b` ≤ 10^9) and are the last two integers from the input, stdin is empty. If the absolute difference between `a` and `b` is even, 'Bob' is printed. If the absolute difference between `a` and `b` is odd, 'Alice' is printed, and either 'Alice' or 'Bob' is printed `t-1` times.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for a series of integer pairs based on the parity of their absolute difference and prints the result for each pair.

