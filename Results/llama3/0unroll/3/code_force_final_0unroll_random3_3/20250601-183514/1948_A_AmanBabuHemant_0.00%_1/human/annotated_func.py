#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 ≤ t ≤ 50) and then t lines each containing an integer n (1 ≤ n ≤ 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The output will contain t lines, where each line is either 'YES' or 'NO'. If the input number n is even, the output will be 'YES' followed by a string of '110' repeated n/2 times. If the input number n is odd, the output will be 'NO'. The output will not exceed 200 characters in length.

#Overall this is what the function does:This function reads a series of integers from standard input, determines whether each integer is even or odd, and prints 'YES' followed by a string of '110' repeated n/2 times if the integer is even and the resulting string is less than 200 characters in length, otherwise prints 'NO'.

