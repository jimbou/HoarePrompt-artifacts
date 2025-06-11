#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the encoded words). The number of test cases is a positive integer and the encoded words are integers between 3 and 78 (inclusive).
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
        
    #State: n is an integer equal to the number of test cases, word is a string, alphabet is a string of all lowercase English letters, stdin is empty, and i is equal to the number of test cases.

#Overall this is what the function does:This function reads a positive integer (the number of test cases) and a list of integers (the encoded words) from standard input, decodes each integer into a three-letter string using a specific mapping, and prints the decoded strings. The function processes all test cases and leaves the standard input empty.

