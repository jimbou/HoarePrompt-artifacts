#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1 and less than or equal to 50).
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
            
        #State: n is 0, letter is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', i is between 1 and 25 (inclusive), 'YES' has been printed. If the initial value of n is between 2 and 48 (inclusive), res is a string containing the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, followed by the character at index i % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times. If the initial value of n is between 1 and 49 (inclusive), res is a string containing the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, followed by the character at index i % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, and then the character at index i % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times. If the initial value of n is 50, res is the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' followed by the character at index i % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times.
        print(res)
        #This is printed: Error: res is not defined
    #State: *`n` is an integer between 1 and 50 (inclusive), stdin contains no input. If `n` is less than or equal to 1, 'NO' is printed. If `n` is between 2 and 48 (inclusive), 'YES' is printed, and a string `res` is printed, where `res` contains the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, followed by the character at index `i` % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times. If `n` is between 1 and 49 (inclusive), 'YES' is printed, and a string `res` is printed, where `res` contains the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, followed by the character at index `i` % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times, and then the character at index `i` % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times. If `n` is 50, 'YES' is printed, and a string `res` is printed, where `res` contains the first character of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' followed by the character at index `i` % 26 of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' repeated 2 times.

#Overall this is what the function does:This function reads an integer input from stdin between 1 and 50 (inclusive) and prints 'NO' if the input is less than or equal to 1. If the input is greater than 1, it prints 'YES' and generates a string 'res' based on the input value. The string 'res' is constructed by repeating characters from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' in a specific pattern, with the pattern depending on the input value. The function then prints the generated string 'res'.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `_` is `t-1`, and the function `func_1()` has been called `t` times with no input from stdin and has returned None.

#Overall this is what the function does:Reads a positive integer from standard input, then calls another function (`func_1`) that number of times, passing no arguments and ignoring its return value, which is expected to be `None`.

