#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters of length at most 10.
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
        
    #State: n is an integer between 1 and 1000, i is n-1, stdin is empty, s is a string consisting of lowercase English letters of length at most 10, a is a set of unique lowercase English letters. If a contains exactly one unique lowercase English letter, 'NO' is printed. If a contains more than one unique lowercase English letter, 'YES' is printed. If the characters in s are in ascending order, the string c which is the characters of s in descending order is printed. Otherwise, the string b which is the characters of s in ascending order is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string contains more than one unique character, and prints 'YES' if it does, followed by the string sorted in ascending order unless it's already sorted, in which case it prints the string sorted in descending order. If a string contains only one unique character, it prints 'NO'. The function processes a number of strings specified by an initial integer input.

