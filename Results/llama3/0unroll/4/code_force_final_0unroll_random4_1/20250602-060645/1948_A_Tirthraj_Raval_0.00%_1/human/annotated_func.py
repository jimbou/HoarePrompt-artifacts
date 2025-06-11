#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing an integer n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: The output state will contain 't' lines, where each line is either 'NO' if the corresponding input integer 'n' is odd, or 'YES' followed by a string of 'n' characters, where the string consists of alternating 'A's and 'B's, starting with 'A'.

#Overall this is what the function does:This function reads a series of integers from standard input, determines whether each integer is even or odd, and prints 'NO' if the integer is odd or 'YES' followed by a string of alternating 'A's and 'B's of the same length as the integer if it is even.

