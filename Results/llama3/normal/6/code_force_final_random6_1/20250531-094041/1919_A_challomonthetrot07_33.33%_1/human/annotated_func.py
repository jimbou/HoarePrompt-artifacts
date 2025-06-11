#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
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
        
    #State: `T` is 0, `i` is `T`, `a` and `b` are undefined, stdin is empty. No more output is printed.

#Overall this is what the function does:Determines the winner of a series of games based on the values of two integers, a and b, and prints the winner's name. The function reads input from stdin, where the first line contains the number of games (T), and each subsequent line contains the values of a and b for each game. The function prints 'Alice' or 'Bob' to indicate the winner of each game, and after processing all games, stdin is empty and no more output is printed.

