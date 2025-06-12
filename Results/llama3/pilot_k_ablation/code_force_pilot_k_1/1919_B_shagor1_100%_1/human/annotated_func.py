#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 5000) and then a string of "+" and "-" characters of length equal to the integer.
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is an integer between 1 and 5000, `s` is a string of "+" and "-" characters of length `n`, `neg` is the number of '-' characters in `s`, `stdin` contains multiple test cases minus one.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: the absolute difference between n and twice the number of '-' characters in s, or n if n equals the number of '-' characters in s

#Overall this is what the function does:Reads a test case from standard input, consisting of an integer n and a string s of "+" and "-" characters of length n, then prints the absolute difference between n and twice the number of '-' characters in s, or n if n equals the number of '-' characters in s.

