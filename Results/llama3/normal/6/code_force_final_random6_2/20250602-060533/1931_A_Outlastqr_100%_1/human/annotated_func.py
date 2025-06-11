#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100), then t integers n (3 <= n <= 78).
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
        
    #State: alphabet is a string of all lowercase English letters, stdin contains no input, i is equal to the value of t, n is an integer greater than or equal to 3, and the value of word is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, generates a string based on each integer according to specific rules, and prints the generated strings. The function takes no arguments and returns no value, but it consumes all input from standard input and produces output strings. The rules for generating strings are based on the value of the input integers, which are used to select characters from the lowercase English alphabet. The function processes all input integers and prints the corresponding strings before terminating.

