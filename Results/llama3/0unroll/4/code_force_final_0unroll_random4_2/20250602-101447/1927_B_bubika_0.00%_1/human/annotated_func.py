#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list consists of non-negative integers. The sum of the lengths of all lists does not exceed 2 * 10^5.
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 non-negative integers, stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a list of n non-negative integers. It then maps each integer in the list to a corresponding character in the alphabet (a-z), where the mapping is determined by the current value of the integer in a list (b). The function prints the resulting string of characters for each test case, effectively decoding the input integers into a string. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

