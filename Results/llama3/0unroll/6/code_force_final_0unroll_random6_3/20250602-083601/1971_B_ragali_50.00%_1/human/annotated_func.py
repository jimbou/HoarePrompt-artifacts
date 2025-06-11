#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
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
        
    #State: The output state is a series of strings, where each string is either 'NO' or a modified version of the input string. If the input string has more than one unique character, the output is 'YES' followed by a modified string. The modified string is either the input string rotated by half its length, its reverse, or the input string with the first half and second half swapped, depending on which modification results in a different string. If the input string has only one unique character, the output is 'NO'. The number of output strings is equal to the value of 't', which is between 1 and 1000 inclusive.

#Overall this is what the function does:The function reads an integer 't' from standard input, representing the number of strings to process. It then reads 't' strings, each consisting of lowercase English letters. For each string, if it contains more than one unique character, the function prints 'YES' followed by a modified version of the string. The modification is either a rotation of the string by half its length, its reverse, or the string with its first and second halves swapped, depending on which modification results in a different string. If the string has only one unique character, the function prints 'NO'. The function processes 't' strings in this manner, where 't' is between 1 and 1000 inclusive.

