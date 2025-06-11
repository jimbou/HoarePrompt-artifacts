#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t integers n (3 <= n <= 78).
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
        
    #State: i is t-1, stdin is empty, alphabet is a string of all lowercase English letters, n is an integer greater than 1. If n > 52, word is a string that consists of the (n-53)th lowercase English letter and 'zz'. If n is between 27 and 52, word is a string that starts with 'a', followed by a lowercase English letter, and ends with 'z'. If n is between 2 and 26, word is 'aa' plus the (n-2)th letter of the alphabet. and the word is printed

#Overall this is what the function does:This function reads a series of integers from standard input, generates a string based on each integer according to specific rules, and prints the generated strings. The rules are: if the integer is greater than 52, the string consists of the (n-53)th lowercase English letter followed by 'zz'; if the integer is between 27 and 52, the string starts with 'a', followed by a lowercase English letter, and ends with 'z'; if the integer is between 2 and 26, the string is 'aa' plus the (n-2)th letter of the alphabet. The function processes all integers provided in the input and prints the corresponding strings.

