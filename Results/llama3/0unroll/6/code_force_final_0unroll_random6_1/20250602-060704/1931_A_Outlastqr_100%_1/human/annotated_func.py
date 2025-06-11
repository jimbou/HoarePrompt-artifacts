#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t integers n (3 <= n <= 78).
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
        
    #State: Output State: The variable `alphabet` remains unchanged as a string of all lowercase English letters. The variable `stdin` is empty as all the inputs have been read. The loop has executed `t` times, and for each iteration, it has printed a string of three characters. The strings are based on the input `n` and are constructed using the `alphabet` string. The output state includes the printed strings, which are determined by the input values of `n`.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers n. For each n, it constructs and prints a three-character string based on the value of n, using a combination of lowercase English letters from the alphabet. The function executes t times, printing a total of t strings, and leaves the standard input empty after reading all inputs.

