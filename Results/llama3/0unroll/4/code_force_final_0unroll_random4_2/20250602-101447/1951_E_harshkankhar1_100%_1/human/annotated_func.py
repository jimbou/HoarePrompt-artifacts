#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    return s == s[::-1]
    #The program returns a boolean value indicating whether the string 's' is a palindrome or not.

#Overall this is what the function does:Determines whether a given string of lowercase Latin characters is a palindrome, returning True if it reads the same backward as forward and False otherwise.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: a string consisting of lowercase Latin characters
        return
        #The program returns nothing, as the return statement is empty. The current state of the program remains unchanged, with 'YES' printed, 1 printed, and the string s printed. The value of x remains -1, and the value of func_1(s[0:]) remains False. The length of string s is still n.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is -1, and func_1(s[0:]) is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True, and x is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: a string consisting of a sequence of the same character (the first character of s) repeated x + 1 times, followed by a space, followed by the remaining characters of s after the character at index x
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
            #This is printed: The substring of s from the beginning to the index of the first character that is different from the first character of s plus 2, followed by a space, followed by the substring of s from the index of the first character that is different from the first character of s plus 2 to the end of the string
        #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True, and x is not equal to -1, and func_1(s[x + 1:]) is True. If x is either 1 or n // 2, then 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the first x + 2 characters of s and the rest of the string s are printed.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True, and x is not equal to -1. If func_1(s[x + 1:]) is False, then 'YES' is printed, 2 is printed, and the string s is split into two parts at index x + 1 and both parts are being printed. If func_1(s[x + 1:]) is True, then if x is either 1 or n // 2, 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the first x + 2 characters of s and the rest of the string s are printed.

#Overall this is what the function does:This function takes a string of lowercase Latin characters as input and checks if it meets certain conditions. If the string consists of the same character repeated throughout, it prints 'YES' and '1' and returns the original string. If the string does not meet this condition, it finds the index of the first character that is different from the first character of the string. If no such character is found, it prints 'NO'. If the index is found, it checks if the substring after this index meets the same condition as the original string. If it does not, it prints 'YES', '2', and splits the string into two parts at the index. If the substring meets the condition and the index is not 1 or half the length of the string, it prints 'YES', '2', and splits the string into two parts at the index plus 2. If the index is 1 or half the length of the string, it prints 'NO'. The function does not return any value.

