#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100), then t lines each containing an integer n (3 <= n <= 78).
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 26:
            word += 'a' + alphabet[n - 28] + 'z'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: Output State: The output state after the loop executes all the iterations is a string of all lowercase English letters, stdin contains no inputs, and the loop has printed t lines each containing a string of three lowercase English letters.

#Overall this is what the function does:This function reads a series of integers from standard input, generates a three-letter string for each integer based on its value, and prints these strings to standard output. The function takes no arguments and returns no value, instead producing output directly. The input integers are expected to be in the range 3 to 78, and the output strings consist of lowercase English letters. The function processes a variable number of inputs, determined by the first integer read from standard input, which specifies the number of subsequent integers to process.

