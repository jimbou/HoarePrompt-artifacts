#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters with a maximum length of 10.
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
        
    #State: The output will contain n lines. For each string s in the input, if s has more than two distinct characters, the output will contain 'YES' followed by the string s in sorted order if s is already sorted, otherwise it will be followed by the string s in reverse sorted order. If s has exactly two distinct characters, the output will contain 'NO'. The value of n remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings. It then checks each string to determine if it contains more than two distinct characters. If a string has more than two distinct characters, the function prints 'YES' followed by the string in sorted order if it is already sorted, otherwise it prints the string in reverse sorted order. If a string has exactly two distinct characters, the function prints 'NO'. The function repeats this process for all t strings, leaving the input integer t unchanged.

