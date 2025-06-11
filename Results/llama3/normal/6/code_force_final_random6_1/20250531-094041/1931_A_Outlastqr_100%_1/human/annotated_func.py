#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing an integer n (3 <= n <= 78).
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
        
    #State: alphabet is a string of all lowercase English letters, stdin is empty, i is equal to t, n is an integer equal to the last input, and word is a string that was printed in the last iteration of the loop.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers. For each integer n, it constructs a three-letter string based on the value of n and prints it. The constructed string follows specific rules based on the value of n: if n is greater than 52, it prefixes the string with the (n-53)th letter of the alphabet and appends 'zz'; if n is greater than 27 but not greater than 52, it prefixes the string with 'a', appends the (n-28)th letter of the alphabet, and suffixes with 'z'; if n is exactly 27, it sets the string to 'aay'; otherwise, it prefixes the string with 'aa' and appends the (n-3)th letter of the alphabet. After processing all integers, the function leaves the standard input empty and the variables i, n, and word in specific states, but these states are not relevant to the function's primary purpose of printing the constructed strings.

