#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t strings s, each consisting of lowercase English letters and of length at most 10.
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
        
    #State: `t` is 0, `i` is the last character in the string `s`, `s` is an empty string, `a` is a set containing all unique characters from the input string `s`. If the number of unique characters in `s` is more than 1, then if newstr is not equal to s, the second half of the string s concatenated with the first half of the string s is printed. If newstr is equal to s, the string s is rearranged by swapping its first and second halves, and if isreverse is equal to s, 'YES' is printed. Otherwise, the value of isreverse is printed. If the number of unique characters in `s` is less than or equal to 1, 'NO' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string has more than one unique character, and if so, prints 'YES' followed by a modified version of the string. The modification is either a rotation of the string (swapping its first and second halves) or its reverse, depending on whether the original string is equal to its rotation or reverse. If a string has only one unique character, it prints 'NO'. The function processes multiple strings based on an initial input specifying the number of strings to process.

