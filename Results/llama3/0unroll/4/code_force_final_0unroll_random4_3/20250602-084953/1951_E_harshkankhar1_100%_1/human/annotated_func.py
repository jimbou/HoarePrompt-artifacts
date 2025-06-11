#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    return s == s[::-1]
    #The program returns a boolean value indicating whether the string 's' is a palindrome or not.

#Overall this is what the function does:Determines whether a given string of lowercase Latin characters is a palindrome, returning a boolean value indicating the result.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the string consisting of lowercase Latin characters)
        return
        #The program returns nothing and prints 'YES', 1, and the string s, and the current value of func_1(s[0:]) is False, and x is -1, and n is the length of s, and s is a string consisting of lowercase Latin characters.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is -1, and the result of func_1(s[0:]) is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and the result of func_1(s[0:]) is True
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The value of x remains -1, and the string s still consists of lowercase Latin characters with a length of n. The result of func_1(s[0:]) is still True, and 'NO' is still printed.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, the result of func_1(s[0:]) is True, and x is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: The first substring of s that contains all characters that are the same as the first character of s, plus the first character that is different, followed by a space, followed by the substring of s that contains all characters that are different from the first character of s, starting from the second character that is different.
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
            #This is printed: The substring of s from the start to the index x + 2 (inclusive), a space, and the substring of s from the index x + 2 to the end
        #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, the result of func_1(s[0:]) is True, x is not equal to -1, and func_1(s[x + 1:]) is True. If x is equal to 1 or n divided by 2, then 'NO' is being printed. Otherwise, 'YES' is being printed, the number 2 is being printed, and the following is being printed: the substring of s from the start to the index x + 2, and the substring of s from the index x + 2 to the end.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, the result of func_1(s[0:]) is True, and x is not equal to -1. If func_1(s[x + 1:]) is False, 'YES' is printed, the number 2 is printed, and the first x+1 characters of the string s and the rest of the string s are printed. If func_1(s[x + 1:]) is True, then if x is equal to 1 or n divided by 2, 'NO' is printed. Otherwise, 'YES' is printed, the number 2 is printed, and the substring of s from the start to the index x + 2 and the substring of s from the index x + 2 to the end are printed.

#Overall this is what the function does:This function takes a string of lowercase Latin characters as input and performs the following actions:

