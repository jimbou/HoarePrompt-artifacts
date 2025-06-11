#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 5000) and then a string of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: n is an integer between 1 and 5000 inclusive, s is an empty string, neg is equal to the number of '-' characters in the original string s, stdin contains 0 test cases.
    print(n - 2 * neg if n != neg else n)
    #This is printed: n (where n is an integer between 1 and 5000 inclusive)

#Overall this is what the function does:This function reads two inputs from the user: an integer n and a string s of length n consisting of '+' and '-' characters. It then calculates the difference between the number of '+' characters and '-' characters in the string, and prints the result. If the number of '+' characters equals the number of '-' characters, it simply prints the original number n.

