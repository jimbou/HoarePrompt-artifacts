#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 1000) and then a string of "+" and "-" characters (length of string = integer).
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is an integer between 1 and 1000, `s` is a string of "+" and "-" characters with a length equal to `n`, `neg` is the number of "-" characters in `s`, `stdin` contains multiple test cases minus one.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: the absolute difference between the total number of characters `n` and twice the number of "-" characters `neg` in the string `s`, or `n` if `n` equals `neg`

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer and a string of "+" and "-" characters. It then calculates and prints the absolute difference between the total number of characters and twice the number of "-" characters in the string, unless the total number of characters equals the number of "-" characters, in which case it prints the total number of characters.

