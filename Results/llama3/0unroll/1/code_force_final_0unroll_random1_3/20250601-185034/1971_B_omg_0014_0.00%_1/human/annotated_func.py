#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
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
        
    #State: The output state will contain n lines, where each line is either 'YES' or 'NO'. If the line is 'YES', it will be followed by either the sorted string in ascending or descending order, depending on whether the original string was already sorted in ascending order. The value of n remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings. It then checks each string to see if it contains exactly two unique characters. If a string contains exactly two unique characters, it prints 'NO'. Otherwise, it prints 'YES' and then prints the string sorted in ascending order if it was not already sorted that way, or in descending order if it was already sorted in ascending order. The function does not modify the input strings or the value of t.

