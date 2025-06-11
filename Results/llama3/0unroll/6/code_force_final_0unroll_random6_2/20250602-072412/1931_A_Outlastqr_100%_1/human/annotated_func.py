#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t lines, each containing an integer (3 <= n <= 78).
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
        
    #State: Output State: The `alphabet` string remains unchanged, and the stdin contains no more inputs. The stdout contains t lines, each containing a string of lowercase English letters. The strings are generated based on the input integers, following the rules specified in the loop body.

#Overall this is what the function does:This function generates and prints t strings of lowercase English letters based on t input integers, where each string is constructed according to specific rules defined in the loop body, and leaves the input stream empty and the output stream containing the generated strings.

