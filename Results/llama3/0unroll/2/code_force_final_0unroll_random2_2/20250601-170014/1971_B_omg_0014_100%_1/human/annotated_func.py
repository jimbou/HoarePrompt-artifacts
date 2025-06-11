#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters of length at most 10.
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
        
    #State: The output state will be a series of strings, where each string is either 'NO', 'YES' followed by a string of sorted characters, or 'YES' followed by a string of reverse sorted characters. The number of strings in the output state will be equal to the value of `n`. The strings will be in the same order as the input strings.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string has all unique characters, and prints 'NO' if it does not. If a string has unique characters, it prints 'YES' followed by the string sorted in ascending order if it was already sorted, otherwise it prints the string sorted in descending order. The function processes a number of strings specified by the first input integer.

