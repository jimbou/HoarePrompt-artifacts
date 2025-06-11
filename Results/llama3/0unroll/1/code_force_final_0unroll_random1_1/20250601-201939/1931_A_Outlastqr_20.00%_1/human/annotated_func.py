#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100), then t integers n (3 <= n <= 78).
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
        
    #State: The output state after the loop executes all the iterations is a string of lowercase English letters, with the first character being the (n-53)th letter of the alphabet, followed by 'zz' if n is greater than 52, or the (n-28)th letter of the alphabet followed by 'z' if n is greater than 26, or the (n-3)th letter of the alphabet followed by 'aa' if n is less than or equal to 26. The input state remains unchanged, with stdin containing two inputs: first an integer t (1 <= t <= 100), then t integers n (3 <= n <= 78).

#Overall this is what the function does:This function generates and prints a series of strings based on input integers. It takes an integer t (1 <= t <= 100) and t subsequent integers n (3 <= n <= 78) from standard input. For each n, it constructs a string of lowercase English letters: if n > 52, the string starts with the (n-53)th letter of the alphabet followed by 'zz'; if n > 26, the string starts with 'a' followed by the (n-28)th letter of the alphabet and ends with 'z'; if n <= 26, the string starts with 'aa' followed by the (n-3)th letter of the alphabet. The function prints each constructed string, leaving the input state unchanged.

