#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: neg is the number of '-' characters in the string s, n is an integer between 1 and 5000 inclusive, s is a string of length n consisting of characters "+" and "-", stdin contains multiple test cases minus one.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: the absolute difference between the length of the string s and twice the number of '-' characters in the string s, or the length of the string s if the length is equal to the number of '-' characters

#Overall this is what the function does:This function reads a test case from standard input, where each test case consists of an integer n and a string s of length n containing "+" and "-" characters. It then calculates and prints the absolute difference between the length of the string s and twice the number of '-' characters in the string s. If the length of the string s is equal to the number of '-' characters, it prints the length of the string s instead.

