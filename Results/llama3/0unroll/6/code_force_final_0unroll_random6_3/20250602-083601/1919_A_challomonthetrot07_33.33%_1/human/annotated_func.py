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
        
    #State: The output state will be a series of T lines, each containing either 'Alice' or 'Bob', depending on the values of a and b in each iteration. The exact output will depend on the specific values of a and b in the input.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for a series of T pairs of integers (a, b) based on specific rules and prints the result for each pair.

