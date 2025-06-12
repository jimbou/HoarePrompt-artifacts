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
            
        #State: `n` is 0, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is equal to the initial value of `n`, `res` is a string consisting of pairs of identical letters from the English alphabet, except possibly the last character if the initial value of `n` is odd, in which case the last character is a single letter from the English alphabet, and 'YES' has been printed.
        print(res)
        #This is printed: a string consisting of pairs of identical letters from the English alphabet
    #State: *`n` is an integer between 1 and 50 (inclusive), stdin is empty. If `n` is less than or equal to 1, 'NO' is printed. Otherwise, 'YES' is printed, `letter` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is equal to the initial value of `n`, `res` is a string consisting of pairs of identical letters from the English alphabet, except possibly the last character if the initial value of `n` is odd, in which case the last character is a single letter from the English alphabet, and an empty string is printed.

#Overall this is what the function does:This function reads an integer n from standard input and prints 'NO' if n is less than or equal to 1. If n is greater than 1, it prints 'YES' followed by a string consisting of pairs of identical letters from the English alphabet, except possibly the last character if n is odd, in which case the last character is a single letter from the English alphabet. The function then leaves the input stream empty and the variable n set to 0.

#State of the program right berfore the function call: t is a positive integer (1 <= t <= 50)
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is a positive integer (1 <= t <= 50), and the function `func_1()` has been executed `t` times.

#Overall this is what the function does:Executes the function `func_1()` a specified number of times, where the number of executions is determined by user input, which is a positive integer between 1 and 50 (inclusive).

