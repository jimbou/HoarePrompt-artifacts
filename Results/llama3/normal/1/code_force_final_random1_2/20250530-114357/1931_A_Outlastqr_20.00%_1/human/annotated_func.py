#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t integers n (3 <= n <= 78).
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
        
    #State: alphabet is a string of all lowercase English letters, stdin is empty, i is t-1, n is an integer between 3 and 78 inclusive. If n is larger than 52, word is a string that is either empty or contains a lowercase letter between 'a' and 'z' (inclusive) followed by 'zz'. If n is larger than 26 but not larger than 52, word is a string that starts with 'a' followed by the (n-28)th letter of the alphabet and ends with 'z'. If n is between 3 and 26 inclusive, word is a string 'aa' followed by the (n-2)th letter of the alphabet, and word is printed

#Overall this is what the function does:This function generates and prints a series of strings based on input integers. It accepts a number of test cases (t) and then t integers (n), each between 3 and 78. For each n, it constructs a string according to specific rules: if n is greater than 52, the string is a lowercase letter followed by 'zz'; if n is between 27 and 52, the string starts with 'a', followed by a letter determined by n, and ends with 'z'; if n is between 3 and 26, the string starts with 'aa' followed by a letter determined by n. The function prints each constructed string. After execution, the standard input is empty, having processed all inputs.

