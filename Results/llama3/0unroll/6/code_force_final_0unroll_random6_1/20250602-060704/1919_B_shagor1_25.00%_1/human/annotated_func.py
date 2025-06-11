#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: neg is the number of '-' characters in the string s, n is an integer between 1 and 5000, s is a string of length n consisting of characters "+" and "-", stdin contains multiple test cases minus one.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n is not equal to neg, otherwise n (where n is the length of the string s and neg is the number of '-' characters in s)

#Overall this is what the function does:This function reads a test case from standard input, consisting of an integer n and a string s of length n containing "+" and "-" characters. It then calculates the difference between the length of the string and twice the number of "-" characters, but if the number of "-" characters equals the length of the string, it simply returns the length of the string. The result is printed to standard output.

