#State of the program right berfore the function call: stdin contains one input: an integer n (1 <= n <= 50).
    n = int(input())
    if (n <= 1) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            
            i += 1
            
        #State: 'YES' has been printed, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `n` is 0, `i` is equal to the initial value of `n`, if the initial value of `n` is even, `res` is a string containing the first `n/2` characters of the alphabet (A-Z) each repeated twice, if the initial value of `n` is odd, `res` is a string containing the first `(n-1)/2` characters of the alphabet (A-Z) each repeated twice, followed by the first character of the alphabet (A)
        print(res)
        #This is printed: (an empty string)
    #State: `n` is an integer between 1 and 50 (inclusive), stdin is empty. If `n` is less than or equal to 1, 'NO' is printed. Otherwise, 'YES' is printed, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `n` is 0, `i` is equal to the initial value of `n`, and if the initial value of `n` is even, `res` is a string containing the first `n/2` characters of the alphabet (A-Z) each repeated twice. If the initial value of `n` is odd, `res` is a string containing the first `(n-1)/2` characters of the alphabet (A-Z) each repeated twice, followed by the first character of the alphabet (A), and an empty string is printed.

#Overall this is what the function does:This function reads an integer input from the user, checks if it is less than or equal to 1, and prints 'NO' if true. Otherwise, it prints 'YES' and generates a string of repeated alphabet characters based on the input value. If the input is even, it repeats the first half of the alphabet (A-Z) twice. If the input is odd, it repeats the first half of the alphabet (A-Z) twice and appends the first character 'A'. The function then prints the generated string.

#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 1 and 50, stdin contains 0 integers, _ is t-1, and the function func_1() has been executed t times and returned None.

#Overall this is what the function does:Reads an integer `t` from standard input, then reads `t` integers from standard input, and executes the function `func_1()` `t` times, discarding its return value.

