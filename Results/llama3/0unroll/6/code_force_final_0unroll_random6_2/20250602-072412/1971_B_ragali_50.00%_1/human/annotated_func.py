#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings s, each consisting of lowercase English letters and having a length of at most 10.
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
        
    #State: The output state is a series of strings, each of which is either the original string, its reverse, or a rotation of the original string by half its length, depending on whether the string has more than one unique character and whether it is a palindrome or not. If a string has only one unique character, the output is 'NO'. The number of strings in the output state is equal to the value of `t`.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings. For each string, it checks if the string has more than one unique character. If it does, the function prints 'YES' and then prints a modified version of the string: either the string rotated by half its length, its reverse, or the original string if it's a palindrome. If the string has only one unique character, the function prints 'NO'. The function repeats this process t times, resulting in a series of strings as output, where each string is either the original, its reverse, or a rotation of the original, or 'NO' if the string has only one unique character.

