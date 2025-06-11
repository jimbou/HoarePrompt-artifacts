#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters with a length of at most 10.
    t = int(input().strip(' '))
    for i in range(t):
        s = input().strip(' ')
        
        a = set()
        
        for i in s:
            a.add(i)
        
        if len(a) > 1:
            print('YES')
            newstr = s[len(s) // 2:] + s[:len(s) // 2]
            isreverse = s[::-1]
            if newstr != s:
                print(s[len(s) // 2:] + s[:len(s) // 2])
            elif isreverse != s:
                print(isreverse)
            else:
                print(s[len(s) // 2:] + s[0:len(s) // 2])
        else:
            print('NO')
        
    #State: t is equal to 0, i is equal to t, s is an empty string, a is an empty set, stdin is empty.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string has more than one unique character, and if so, prints 'YES' followed by a modified version of the string. The modified string is either the original string rotated by half its length or its reverse, whichever is different from the original string. If the string has only one unique character, it prints 'NO'. The function processes all input strings and then terminates, leaving the input stream empty.

