#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: n is an integer between 1 and 5000 inclusive, s is an empty string, stdin contains multiple test cases minus one, neg is equal to the number of '-' characters in the initial string s.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: n (where n is an integer between 1 and 5000 inclusive)

#Overall this is what the function does:The function reads two inputs from the standard input: an integer n and a string s of length n consisting of "+" and "-" characters. It then calculates the absolute difference between n and twice the number of "-" characters in the string, and prints this value. If the number of "-" characters is equal to n, it simply prints n. The function does not modify the input variables and does not return any value, only printing the calculated result.

