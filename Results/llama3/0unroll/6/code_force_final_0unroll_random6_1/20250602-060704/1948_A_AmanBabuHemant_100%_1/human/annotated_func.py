#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The output state will contain t lines, where each line is either 'YES' or 'NO'. If the input integer n is even, the output will be 'YES' followed by a string of 'AAB' repeated n/2 times, as long as the length of the string is less than 200 characters. If n is odd or the length of the string is 200 characters or more, the output will be 'NO'.

#Overall this is what the function does:This function reads a series of integers from standard input, determines whether each integer is even and can be represented as a string of 'AAB' repeated a certain number of times without exceeding 200 characters, and prints 'YES' followed by the string if possible, or 'NO' otherwise.

