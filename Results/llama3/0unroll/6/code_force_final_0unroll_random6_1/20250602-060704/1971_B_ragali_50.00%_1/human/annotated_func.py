#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t strings s consisting of lowercase English letters.
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
        
    #State: The output state will be a series of strings, each representing the modified input string or the original string if it's a palindrome. If the input string has only one unique character, it will print 'NO'. The number of strings in the output state will be equal to the value of 't'.

#Overall this is what the function does:The function accepts a series of strings as input and returns a modified version of each string. If a string has more than one unique character, it attempts to create a new string by rearranging the characters. If the rearranged string is different from the original, it returns the rearranged string. If the rearranged string is the same as the original, it checks if the original string is a palindrome. If it's not a palindrome, it returns the reversed string. If the string is a palindrome, it returns the original string with the first half and second half swapped. If a string has only one unique character, it returns 'NO'. The function processes multiple input strings and returns the modified strings or 'NO' for each input string.

