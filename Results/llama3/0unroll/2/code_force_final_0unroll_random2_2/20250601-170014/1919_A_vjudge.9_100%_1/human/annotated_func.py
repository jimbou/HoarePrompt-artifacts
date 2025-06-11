#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The program will print 'Bob' or 'Alice' for each pair of integers (a, b) in the input, depending on whether the absolute difference between a and b is even or odd, respectively. The value of t remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases, and then reads t pairs of integers (a, b). For each pair, it determines whether the absolute difference between a and b is even or odd and prints 'Bob' or 'Alice', respectively, to standard output. The function does not modify the input values or return any values, only producing output based on the input pairs.

