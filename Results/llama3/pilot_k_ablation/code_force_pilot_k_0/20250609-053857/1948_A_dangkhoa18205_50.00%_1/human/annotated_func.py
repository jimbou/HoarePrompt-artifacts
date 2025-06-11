#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    n = int(input())
    if (n <= 1) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            
            i += 1
            
        #State: n is 0, letter is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', i is 1, res is 'AA', and 'YES' is being printed.
        print(res)
        #This is printed: AA
    #State: *`n` is a positive integer, stdin contains no input. If `n` is less than or equal to 1, 'NO' is printed. Otherwise, 'YES' is printed, and 'AA' is printed.

#Overall this is what the function does:This function reads a positive integer from standard input, checks if it is greater than 1, and prints 'YES' if true, otherwise prints 'NO'. If 'YES' is printed, it generates a string of repeated letters from 'A' to 'Z' based on the input integer and prints the resulting string. The function consumes the input from standard input and leaves it empty.

#State of the program right berfore the function call: stdin contains one input: an integer t (1 ≤ t ≤ 50)
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` is 0, stdin contains no input.

#Overall this is what the function does:Reads an integer t from standard input, executes func_1() t times, and leaves standard input empty.

