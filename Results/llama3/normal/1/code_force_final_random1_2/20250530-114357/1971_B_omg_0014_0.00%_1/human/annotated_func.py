#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters of length at most 10.
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 2:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: n is an integer between 1 and 1000 (inclusive), i is n-1, s is a string consisting of lowercase English letters of length at most 10, a is a set of unique lowercase English letters from s, stdin is empty. If the length of a is 2, 'NO' is printed. Otherwise, 'YES' is printed, b is a string consisting of the characters in s in ascending order, c is a string consisting of the characters in s in descending order. If the string s is equal to the string b, then the string c is printed. Otherwise, the string b is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks each string for uniqueness of characters, and prints 'YES' if all characters are unique or 'NO' if there are exactly two unique characters. If 'YES' is printed, it then prints the string in either ascending or descending order, depending on whether the original string was already sorted in ascending order. The function processes a number of strings specified by an initial integer input.

