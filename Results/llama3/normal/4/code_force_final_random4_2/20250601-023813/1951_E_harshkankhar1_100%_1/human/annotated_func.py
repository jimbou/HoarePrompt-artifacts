#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward) and False otherwise.

#Overall this is what the function does:Determines whether a given string of lowercase Latin characters is a palindrome, returning True if it reads the same backward as forward and False otherwise.

#State of the program right berfore the function call: s is a string of lowercase Latin characters.
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: a string of lowercase Latin characters
        return
        #The program returns None, 'YES' has been printed, the number 1 has been printed, and the string s has been printed. The value of x is still -1, and the value of n is still the length of the string s. The value of func_1(s[0:]) is still False.
    #State: *s is a string of lowercase Latin characters, n is the length of s, x is -1, and func_1(s[0:]) is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is a string of lowercase Latin characters, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`, and `x` is the index of the first character in `s` that is different from the first character of `s`, or `-1` if no such character exists.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as there is no explicit return statement. The value of x remains -1, indicating that there is no character in string s that is different from the first character of s, and 'NO' is printed.
    #State: *`s` is a string of lowercase Latin characters, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`, and `x` is the index of the first character in `s` that is different from the first character of `s`, and `x` is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: the first substring of `s` containing all characters that are the same as the first character of `s`, followed by a space, and then the second substring of `s` containing all characters that are different from the first character of `s`
    else :
        if (x == 1 or x == n // 2) :
            print('NO')
            #This is printed: NO
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: 2
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: s[:x + 2] (which is the substring of s from the beginning to the index x + 2), s[x + 2:] (which is the substring of s from the index x + 2 to the end)
        #State: *`s` is a string of lowercase Latin characters, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`, and `x` is the index of the first character in `s` that is different from the first character of `s`, and `x` is not equal to -1, and `func_1(s[x + 1:])` is True. If `x` is either 1 or `n // 2`, 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the string `s` is split into two substrings at index `x + 2` and these two substrings are printed.
    #State: *`s` is a string of lowercase Latin characters, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`, and `x` is the index of the first character in `s` that is different from the first character of `s`, and `x` is not equal to -1. If `func_1(s[x + 1:])` is False, 'YES' is printed, 2 is printed, and the first x+1 characters of the string s which are the same as the first character of s and the rest of the string s starting from index x+1 are printed. If `func_1(s[x + 1:])` is True, if `x` is either 1 or `n // 2`, 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the string `s` is split into two substrings at index `x + 2` and these two substrings are printed.

#Overall this is what the function does:This function takes a string of lowercase Latin characters as input and checks if it meets certain conditions. If the string does not meet the conditions, it prints 'YES' and the number 1, followed by the original string. If the string meets the conditions but does not contain any characters different from the first character, it prints 'NO'. If the string meets the conditions and contains characters different from the first character, it prints 'YES' and the number 2, followed by the string split into two substrings at the index of the first different character. If the index of the first different character is 1 or half the length of the string, it prints 'NO' instead. The function does not return any value.

