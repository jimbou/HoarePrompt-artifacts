#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 1000). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is at least 1, i is t-1, stdin is empty, s is an empty string, a is an integer between 1 and 10^9 inclusive, b is an integer between 1 and 10^9 inclusive. If the sum of a and b is even, 'Bob' was printed. Otherwise, 'Alice' was printed.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each of t pairs of integers (a, b) based on whether their sum is even or odd, and prints the result for each pair.

