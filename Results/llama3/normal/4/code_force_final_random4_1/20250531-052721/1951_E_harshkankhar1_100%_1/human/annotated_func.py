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
        #This is printed: the string s (which is a sequence of lowercase Latin characters)
        return
        #The program returns nothing, 'YES' has been printed, 1 has been printed, and the string s has been printed, and the function func_1(s[0:]) is still False, and the variable x is still -1, and the variable n is still the length of the string s, and the string s is still consisting of lowercase Latin characters.
    #State: *s is a string consisting of lowercase Latin characters, n is the length of s, x is -1, and the function func_1(s[0:]) returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is a string consisting of lowercase Latin characters, `n` is the length of `s`, `x` is the index of the first character in `s` that is not equal to the first character of `s`, or -1 if no such character exists, and the function func_1(s[0:]) returns True.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as there is no explicit return statement. The value of x remains -1, indicating that there is no character in s that is not equal to the first character of s, and 'NO' is still being printed. The function func_1(s[0:]) remains True, and the length of s, denoted by n, remains unchanged.
    #State: *`s` is a string consisting of lowercase Latin characters, `n` is the length of `s`, `x` is the index of the first character in `s` that is not equal to the first character of `s`, and `x` is not equal to -1, and the function func_1(s[0:]) returns True.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: [first character of s] repeated (x + 1) times, followed by a space, followed by the substring of s starting from index x + 1
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
            #This is printed: the first character of s repeated x + 1 times, followed by the character at index x + 1, a space, and the rest of the string s from index x + 2 to the end
        #State: *`s` is a string consisting of lowercase Latin characters, `n` is the length of `s`, `x` is the index of the first character in `s` that is not equal to the first character of `s`, and `x` is not equal to -1, the function func_1(s[0:]) returns True, and the function func_1(s[x + 1:]) returns True. If `x` is either 1 or half of the length of `s`, 'NO' is printed. Otherwise, 'YES' is printed, the number 2 is printed, and the first `x+2` characters of the string `s` and the rest of the string `s` are printed.
    #State: *`s` is a string consisting of lowercase Latin characters, `n` is the length of `s`, `x` is the index of the first character in `s` that is not equal to the first character of `s`, and `x` is not equal to -1, and the function func_1(s[0:]) returns True. If func_1(s[x + 1:]) is False, 'YES' is printed, the number 2 is printed, and the string `s` is split into two substrings at index `x + 1` and both substrings are being printed. If func_1(s[x + 1:]) is True, if `x` is either 1 or half of the length of `s`, 'NO' is printed. Otherwise, 'YES' is printed, the number 2 is printed, and the first `x+2` characters of the string `s` and the rest of the string `s` are printed.

#Overall this is what the function does:This function takes a string `s` consisting of lowercase Latin characters as input and performs the following actions:

