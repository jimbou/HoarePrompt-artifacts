#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then t pairs of inputs, each pair consisting of an integer n and a list of n non-negative integers.
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 integers where each element is the number of times the corresponding character appears in the string r, n is an integer, s is a list of n non-negative integers, r is a string consisting of the characters in 'abcdefghijklmnopqrstuvwxyz' in the order they appear in s, stdin is empty, i is the last element in s, and x is the index of the last element in s in b, and the string r is printed which is a string consisting of the characters in 'abcdefghijklmnopqrstuvwxyz' in the order they appear in s.

#Overall this is what the function does:The function reads multiple pairs of inputs from standard input, where each pair consists of an integer n and a list of n non-negative integers. It then constructs a string r by mapping each integer in the list to a character in the alphabet (a-z) based on its frequency of appearance, and prints the resulting string. The function repeats this process for each pair of inputs, until all input pairs have been processed and standard input is empty.

