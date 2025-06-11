#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is 0, `s` is an empty string, `i` is the last character of the original string `s`. If `i` equals '-', then `neg` is equal to the number of '-' characters in the original string `s`. Otherwise, `neg` is equal to the number of '-' characters in the original string `s` minus 1. `stdin` contains multiple test cases minus `n`
    print(n - 2 * neg if n != neg else n)
    #This is printed: 0

#Overall this is what the function does:Reads a test case from standard input, consisting of an integer n and a string s of length n containing "+" and "-" characters, then prints the difference between n and twice the number of "-" characters in s, unless the number of "-" characters equals n, in which case it prints n.

