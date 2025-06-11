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
            
        #State: n is 0, 'YES' has been printed, letter is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', i is the integer division of the initial value of n by 2 plus the remainder of the division of the initial value of n by 2, res is a string consisting of two repetitions of each letter of the alphabet from 'A' to the letter at index (i-1) of the alphabet if the initial value of n is between 2 and 48 (inclusive), or a string consisting of two repetitions of each letter of the alphabet from 'A' to the letter at index (i-2) of the alphabet plus the letter at index (i-1) of the alphabet if the initial value of n is 1, or a string consisting of two repetitions of each letter of the alphabet from 'A' to the letter at index (i-2) of the alphabet plus the letter at index (i-1) of the alphabet if the initial value of n is less than or equal to 0.
        print(res)
        #This is printed: ''
    #State: *`n` is an integer between 1 and 50 (inclusive), stdin contains no input. If `n` is less than or equal to 1, 'NO' is printed. Otherwise, 'YES' is printed, and a string `res` is printed, which consists of two repetitions of each letter of the alphabet from 'A' to the letter at index (i-2) of the alphabet plus the letter at index (i-1) of the alphabet, where `i` is the integer division of the initial value of `n` by 2 plus the remainder of the division of the initial value of `n` by 2.

#Overall this is what the function does:This function reads an integer n from standard input and prints 'NO' if n is less than or equal to 1. Otherwise, it prints 'YES' followed by a string consisting of two repetitions of each letter of the alphabet from 'A' to a certain letter determined by the value of n. The function then terminates, leaving the standard input empty.

#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of integers (the number of special characters in each test case). The number of test cases is a positive integer and the number of special characters in each test case is a positive integer.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is greater than or equal to 0, and `func_1()` has been executed `t` times.

#Overall this is what the function does:This function reads a positive integer from standard input, representing the number of test cases, and then executes another function (`func_1`) that number of times. The function does not return any value or modify any external state; its sole purpose is to execute `func_1` a specified number of times based on the input.

