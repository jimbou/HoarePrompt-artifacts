#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000), and the remaining t inputs are strings of lowercase English letters of length at most 10.
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 2:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: The output state will be a series of 'YES' or 'NO' strings, followed by either the sorted or reverse-sorted version of the input strings, depending on whether the input strings are already sorted or not. The number of output lines will be 2n, where n is the initial value of the variable 'n'. The value of 'n' will be 0 after the loop finishes executing. The stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads a series of input strings from stdin, checks if each string contains exactly two unique characters, and prints 'YES' or 'NO' accordingly. If the string is not a two-character string, it prints the sorted or reverse-sorted version of the string, depending on whether the original string was already sorted or not. The function processes multiple input strings, as specified by the initial integer input, and empties the stdin after execution.

