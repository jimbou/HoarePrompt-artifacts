#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: n is an integer between 1 and 5000 inclusive, s is a string of length n consisting of "+" and "-" characters, stdin contains multiple test cases minus one, neg is equal to the number of '-' characters in s.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n - 2 * neg if n != neg else n (where n is an integer between 1 and 5000 inclusive, and neg is the number of '-' characters in the string s)

#Overall this is what the function does:This function reads a test case from standard input, consisting of an integer n and a string s of length n containing "+" and "-" characters. It then calculates and prints the result of the expression n - 2 * neg if n is not equal to the number of '-' characters in s, otherwise it prints n. The function does not modify the input variables and does not have any side effects other than printing the result.

