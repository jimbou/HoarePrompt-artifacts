#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters with a maximum length of 10.
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 1:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: The output state will be a series of strings, where each string is either 'NO', 'YES' followed by a string, or 'YES' followed by two strings. The number of strings will be equal to the value of `n`. For each string, if all characters are the same, the output will be 'NO'. If all characters are different, the output will be 'YES' followed by the string sorted in ascending order. If the string is already sorted in ascending order, the output will be 'YES' followed by the string sorted in descending order. Otherwise, the output will be 'YES' followed by the string sorted in ascending order. The value of `n` will be unchanged. The stdin will be empty.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string has all unique characters, and outputs 'NO' if all characters are the same. If all characters are different, it outputs 'YES' followed by the string sorted in ascending order. If the string is already sorted in ascending order, it outputs 'YES' followed by the string sorted in descending order. Otherwise, it outputs 'YES' followed by the string sorted in ascending order. The function processes a number of strings specified by the first input integer and leaves the input integer unchanged.

