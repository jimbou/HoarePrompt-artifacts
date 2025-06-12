#State of the program right berfore the function call: n is a positive integer less than or equal to 50.
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
            
        #State: 'n' is 0, 'res' is a string consisting of a sequence of letters from 'A' to 'Z' repeated twice, with the last letter possibly repeated only once if the initial value of 'n' is odd, 'i' is equal to the initial value of 'n'
        print(res)
        #This is printed: A sequence of letters from 'A' to 'Z' repeated twice
    #State: *`n` is a positive integer less than or equal to 50, stdin contains one input: an integer. If the current value of `n` is less than or equal to 1, 'NO' is being printed. Otherwise, 'res' is a string consisting of a sequence of letters from 'A' to 'Z' repeated twice, with the last letter possibly repeated only once if the initial value of 'n' is odd, 'i' is equal to the initial value of 'n', and the string 'res' is being printed.

#Overall this is what the function does:This function takes an integer input from the user, checks if it's less than or equal to 1, and prints 'NO' in that case. If the input is greater than 1, it generates a string of letters from 'A' to 'Z', repeating each letter twice, with the last letter possibly repeated only once if the input is odd, and prints this string. The function effectively validates the input and produces a specific output based on the input value, either a simple 'NO' or a constructed string of repeated letters.

#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t number of integers, each integer n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 1 and 50, stdin contains `t` number of integers, each integer `n` (1 <= n <= 50), `_` is `t-1`, and the function `func_1()` has been executed `t` times.

#Overall this is what the function does:Reads an integer t from standard input, then reads t number of integers, and executes the function func_1() t times.

