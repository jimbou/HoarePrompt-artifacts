#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 1:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: n is an integer between 1 and 1000 (inclusive), stdin contains n strings, each consisting of lowercase English letters and having a length of at most 10. i is n-1, s is a string of length n, a is a set containing the unique characters in s, b is a string containing the characters of s in ascending order, and c is a string containing the characters of s in descending order. If the set a contains only one unique character, 'NO' is being printed. Otherwise, 'YES' is being printed. If the string s is equal to the string b containing the characters of s in ascending order, then the string c containing the characters of s in descending order is being printed. Otherwise, the string b containing the characters of s in ascending order is being printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string is composed of unique characters, and prints 'YES' if it is, followed by the string in either ascending or descending order depending on whether the original string was already sorted in ascending order. If the string contains duplicate characters, it prints 'NO'.

