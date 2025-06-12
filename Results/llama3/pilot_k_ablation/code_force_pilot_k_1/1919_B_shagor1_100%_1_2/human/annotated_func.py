#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a string (s) of length n consisting of characters "+" and "-".
    n = int(input())
    s = input()
    neg = 0
    for i in s:
        if i == '-':
            neg += 1
        
    #State: `n` is an integer, `s` is a string of length `n` consisting of "+" and "-" characters, `neg` is the number of "-" characters in `s`, stdin contains multiple test cases minus one.
    print(abs(n - 2 * neg) if n != neg else n)
    #This is printed: The absolute difference between the length of string s and twice the number of "-" characters in s, or the length of string s if all characters are "-"

#Overall this is what the function does:The function reads an integer (n) and a string (s) of length n from standard input, counts the number of "-" characters in the string, and prints the absolute difference between the length of the string and twice the number of "-" characters, unless all characters are "-", in which case it prints the length of the string.

