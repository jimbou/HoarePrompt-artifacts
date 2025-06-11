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
        
    #State: The output will contain n lines, where each line is either 'NO', 'YES' followed by a string, or 'YES' followed by another string. The strings will be the sorted or reverse sorted version of the input strings. The 'NO' lines will correspond to the input strings that contain only one unique character. The 'YES' lines will correspond to the input strings that contain more than one unique character. The order of the output lines will match the order of the input strings.

#Overall this is what the function does:This function reads a series of strings from standard input, determines if each string contains more than one unique character, and prints 'NO' if it doesn't. If a string contains more than one unique character, it prints 'YES' followed by the sorted or reverse-sorted version of the string, depending on whether the original string was already sorted or not. The function processes multiple strings, with the number of strings specified by an initial integer input.

