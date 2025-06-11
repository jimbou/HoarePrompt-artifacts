#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
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
        
    #State: The output state will be a list of T strings, where each string is either 'Alice' or 'Bob', depending on the values of a and b in each iteration of the loop.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each of T pairs of integers (a, b) provided as input, based on specific rules, and prints the results as a list of T strings.

