#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t integers (3 <= n <= 78).
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
        
    #State: The loop will execute for a number of times equal to the first input integer. Each iteration will print a string of three characters. The first character will be the nth letter of the alphabet, where n is the current iteration number. The second character will be 'a' if the iteration number is less than or equal to 26, 'z' if the iteration number is greater than 26 and less than or equal to 52, and the (n-53)th letter of the alphabet if the iteration number is greater than 52. The third character will be 'z' if the iteration number is less than or equal to 26, the (n-28)th letter of the alphabet if the iteration number is greater than 26 and less than or equal to 52, and 'z' if the iteration number is greater than 52. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads a series of integers from standard input, generates and prints a string of three characters for each integer. The string is constructed based on the integer's value, using a specific pattern that involves the alphabet. The function continues this process until all input integers have been processed, leaving the standard input empty.

