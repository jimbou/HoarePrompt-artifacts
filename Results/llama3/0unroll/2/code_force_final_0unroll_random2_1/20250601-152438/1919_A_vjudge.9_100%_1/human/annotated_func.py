#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output will be a series of 'Alice' or 'Bob' printed to the console, with the number of lines equal to the initial value of `t`. Each line will be either 'Alice' or 'Bob', depending on whether the absolute difference between `a` and `b` is odd or even, respectively. The values of `t`, `a`, and `b` will remain unchanged.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for a series of pairs of integers based on whether the absolute difference between the integers is odd or even, and prints the results to the console.

