#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: neg is the number of '-' characters in s, n is an integer between 1 and 5000 inclusive, s is a string of length n consisting of characters "+" and "-", stdin contains multiple test cases minus one.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n is not equal to neg, otherwise n (where n is an integer between 1 and 5000 inclusive, and neg is the number of '-' characters in the string s of length n)

#Overall this is what the function does:This function reads two inputs from the standard input: an integer n and a string s of length n consisting of "+" and "-" characters. It then calculates the difference between the total number of characters and twice the number of "-" characters in the string. If the total number of characters is equal to the number of "-" characters, it returns the total number of characters. Otherwise, it returns the calculated difference. The function prints the result to the standard output.

