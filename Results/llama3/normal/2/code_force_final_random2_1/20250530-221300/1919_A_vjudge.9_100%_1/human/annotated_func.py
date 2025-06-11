#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is greater than or equal to 0, `i` is `t`, `a` is an integer between 1 and 10^9, `b` is an integer between 1 and 10^9, stdin is empty. If the absolute difference between `a` and `b` is even, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for a series of pairs of integers based on whether the absolute difference between the integers is even or odd, and prints the result for each pair.

