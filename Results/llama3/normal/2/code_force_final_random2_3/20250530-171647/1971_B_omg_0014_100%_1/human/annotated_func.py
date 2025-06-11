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
        
    #State: n is an integer between 1 and 1000, n must be greater than or equal to 0, i is n-1, s is a string consisting of lowercase English letters and having a length of at most 10, a is a set of unique lowercase English letters from s, stdin is empty. If the number of unique letters in a is exactly 1, then 'NO' is printed. If the number of unique letters in a is more than 1, then 'YES' is printed, b is a string consisting of the letters of s in ascending order, and c is a string consisting of the letters of s in descending order. If the letters in s are in ascending order, then c is printed. Otherwise, b is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string is composed of unique letters, and prints 'YES' if it is, followed by the string sorted in ascending or descending order depending on its original order. If the string contains only one unique letter, it prints 'NO'. The function processes a number of strings specified by an initial integer input, and it does not return any value.

