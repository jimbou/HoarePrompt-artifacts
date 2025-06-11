#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    return s == s[::-1]
    #The program returns a boolean value indicating whether the string s is a palindrome or not.

#Overall this is what the function does:Determines whether a given string of lowercase Latin characters is a palindrome, returning a boolean value indicating whether the string reads the same backward as forward.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: the sequence of lowercase Latin characters in the string s
        return
        #The program returns nothing because the return statement is empty. The value of s remains a string consisting of lowercase Latin characters, the value of n remains the length of s, and the value of x remains -1. The function func_1(s[0:]) remains False, 'YES' has been printed, 1 has been printed, and the string s has been printed.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is -1, and func_1(s[0:]) returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) returns True
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, 'NO' is printed, and the value of x remains -1, indicating that no character in string s is different from the first character of s.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, func_1(s[0:]) returns True, and x is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: the substring of s from the beginning to the index x + 1 (inclusive), followed by a space, and then the substring of s from the index x + 1 to the end
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
            #This is printed: a substring of s from the start to the index x + 2 (inclusive), followed by a space, and then a substring of s from the index x + 2 to the end of the string (where x is the index of the first character in s that is different from the first character of s)
        #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, func_1(s[0:]) returns True, x is not equal to -1, and func_1(s[x + 1:]) returns True. If x is either 1 or n divided by 2, 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the first x + 2 characters of the string s and the rest of the string s are printed.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is the index of the first character in s that is different from the first character of s, func_1(s[0:]) returns True, and x is not equal to -1. If func_1(s[x + 1:]) is False, 'YES' is printed, the number 2 is printed, and the string s is printed in two parts: the first part is from the start of the string to the index x (inclusive), and the second part is from the index x + 1 to the end of the string. If func_1(s[x + 1:]) is True, then if x is either 1 or n divided by 2, 'NO' is printed. Otherwise, 'YES' is printed, 2 is printed, and the first x + 2 characters of the string s and the rest of the string s are printed.

#Overall this is what the function does:This function takes a string of lowercase Latin characters as input and checks if it can be divided into two parts based on certain conditions. If the string consists of the same character repeated, it prints 'NO'. If the string can be divided into two parts, it prints 'YES', the number 2, and the two parts of the string. If the string cannot be divided into two parts, it prints 'YES', the number 1, and the original string. The function does not return any value.

