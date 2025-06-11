#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 1000), then t strings s of lowercase English letters with length at most 10.
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
        
    #State: n is an integer between 1 and 1000, i is equal to n, stdin is empty, s is a string of lowercase English letters with length at most 10, a is a set of lowercase English letters, b is a string of lowercase English letters sorted in ascending order, c is a string of lowercase English letters sorted in descending order. If the size of a is exactly 2, then 'NO' is being printed. Otherwise, 'YES' is being printed. If b is equal to s, then c is being printed. Otherwise, b is being printed.

#Overall this is what the function does:This function reads a series of strings from standard input, checks if each string contains exactly two unique characters, and prints 'YES' or 'NO' accordingly. If a string contains more than two unique characters, it prints the string sorted in ascending order unless the original string is already sorted, in which case it prints the string sorted in descending order. The function processes a number of strings specified by the first input, which is an integer between 1 and 1000.

