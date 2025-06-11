#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing an integer n (3 <= n <= 78).
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 27:
            word += 'a' + alphabet[n - 28] + 'z'
        elif n == 27:
            word = 'aay'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: Output State: The output state after the loop executes all the iterations is that the variable `alphabet` remains unchanged, and the variable `stdin` is empty. The loop has consumed all the input from `stdin` and has printed `t` lines to the standard output, where each line is a string of three characters. The strings are constructed based on the input integers `n` according to the logic in the loop body.

#Overall this is what the function does:The function reads a series of integers from standard input, constructs a string of three characters for each integer based on a specific logic, and prints these strings to the standard output. The function consumes all input from standard input and produces a total of t lines of output, where t is the first integer read from standard input. The output strings are constructed by combining characters from the lowercase English alphabet, with the specific characters used depending on the value of each input integer.

