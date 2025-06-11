#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    return s == s[::-1]
    #The program returns True if the string s is the same when its characters are reversed, False otherwise.

#Overall this is what the function does:Determines whether a given string of lowercase Latin characters is a palindrome, returning True if the string is the same when reversed and False otherwise.

#State of the program right berfore the function call: s is a string of lowercase Latin characters.
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: a string of lowercase Latin characters (the exact string is not specified, but it is a string of lowercase Latin characters)
        return
        #The program returns nothing, but 'YES' is printed, 1 is printed, and the string s is printed, where s is a string of lowercase Latin characters, n is the length of s, and x is -1. The function func_1 applied to the string s returns False.
    #State: *s is a string of lowercase Latin characters, n is the length of s, x is -1, and the function func_1(s[0:]) returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: s is a string of lowercase Latin characters, n is the length of s, func_1(s[0:]) returns True, i is n, and x is the index of the first character in s that is not equal to the first character of s, or -1 if no such character exists.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The current state of the program remains unchanged, with 's' being a string of lowercase Latin characters, 'n' being the length of 's', 'func_1(s[0:])' returning True, 'i' being equal to 'n', and 'x' being -1, indicating that all characters in 's' are equal to the first character of 's', and 'NO' being printed.
    #State: *s is a string of lowercase Latin characters, n is the length of s, func_1(s[0:]) returns True, i is n, and x is the index of the first character in s that is not equal to the first character of s, or -1 if no such character exists. x is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: [substring of s containing all characters equal to the first character of s] [substring of s containing characters not equal to the first character of s]
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
            #This is printed: The substring of s from the start to the index x + 2 (where x is the index of the first character in s that is not equal to the first character of s), followed by a space, followed by the substring of s from the index x + 2 to the end (where x is the index of the first character in s that is not equal to the first character of s)
        #State: *s is a string of lowercase Latin characters, n is the length of s, func_1(s[0:]) returns True, i is n, and x is the index of the first character in s that is not equal to the first character of s, and x is not equal to -1, and func_1(s[x + 1:]) returns True. If x is either 1 or half of the length of s, 'NO' is printed. Otherwise, 'YES' is printed, the number 2 is printed, and the first x + 2 characters of the string s and the rest of the string s from index x + 2 to the end of the string s are printed.
    #State: *s is a string of lowercase Latin characters, n is the length of s, func_1(s[0:]) returns True, i is n, and x is the index of the first character in s that is not equal to the first character of s. If func_1(s[x + 1:]) is False, 'YES' is printed, the number 2 is printed, and the substring of s from the start to the index x+1 (inclusive) which is a string of the same character repeated, and the substring of s from the index x+1 to the end which is a string of lowercase Latin characters. If func_1(s[x + 1:]) is True, then if x is either 1 or half of the length of s, 'NO' is printed. Otherwise, 'YES' is printed, the number 2 is printed, and the first x + 2 characters of the string s and the rest of the string s from index x + 2 to the end of the string s are printed.

#Overall this is what the function does:This function determines whether a given string of lowercase Latin characters can be divided into two substrings, each containing the same character repeated, or two substrings where the first substring contains the same character repeated and the second substring contains a different character repeated. If the string can be divided in such a way, it prints 'YES', the number 2, and the two substrings. If the string cannot be divided in such a way, it prints 'NO'. If the entire string contains the same character repeated, it prints 'YES', the number 1, and the string itself.

