#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 5000) and then a string of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: n is an integer between 1 and 5000 inclusive, s is an empty string, neg is the number of '-' characters in the initial string s, stdin contains multiple test cases minus one.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: n (where n is an integer between 1 and 5000 inclusive)

#Overall this is what the function does:This function reads a test case from standard input, consisting of an integer n and a string s of length n containing '+' and '-' characters. It calculates the absolute difference between n and twice the number of '-' characters in s, and prints this value. If the number of '-' characters is equal to n, it simply prints n. The function processes one test case and does not modify the input variables.

