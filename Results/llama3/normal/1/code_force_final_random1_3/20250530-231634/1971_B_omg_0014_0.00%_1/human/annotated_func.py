#State of the program right berfore the function call: stdin contains a positive integer t (1 <= t <= 1000) followed by t strings of lowercase English letters of length at most 10.
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
        
    #State: n is a positive integer between 1 and 1000 (inclusive), i is n-1, s is a string of lowercase English letters of length at most 10, a is a set of unique lowercase English letters, stdin is empty. If the size of set a is 2, 'NO' is printed. Otherwise, 'YES' is printed. If b is equal to s, then c (a string of reverse sorted lowercase English letters) is printed. Otherwise, b (a string of sorted lowercase English letters) is printed.

#Overall this is what the function does:This function reads a positive integer t from standard input, followed by t strings of lowercase English letters. For each string, it checks if the string contains exactly two unique letters. If it does, the function prints 'NO'. Otherwise, it prints 'YES' and then prints the string in either sorted or reverse sorted order, depending on whether the original string was already sorted. The function processes all input strings and then terminates, leaving the standard input empty.

