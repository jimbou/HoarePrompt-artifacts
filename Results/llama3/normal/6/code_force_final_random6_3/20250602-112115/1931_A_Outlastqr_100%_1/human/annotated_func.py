#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing an integer n (3 <= n <= 78).
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
        
    #State: alphabet is a string of all lowercase English letters, stdin is empty, i is equal to the value of t, n is an integer greater than 0 and less than or equal to 78. If n is greater than 52, word is a string consisting of the (n-53)th letter of the alphabet and 'zz'. If n is less than or equal to 52, word is either 'a' + an empty string + 'z' if n is less than or equal to 28, or 'a' + a character from the end of alphabet + 'z' if n is greater than 28. If n is less than or equal to 27, word is 'aay' if n is 27, otherwise word is a string that starts with 'aa' followed by the (n-2)th letter of the alphabet, and the value of word is being printed.

#Overall this is what the function does:This function generates and prints a series of strings based on input integers. It accepts a number of test cases (t) and then t integers (n), each between 3 and 78. For each n, it constructs a string (word) according to specific rules based on the value of n relative to 27 and 52, and then prints this word. The function consumes all input from stdin and leaves it empty, producing no return value but printing the constructed words for each input integer.

