#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then for each test case, first an integer n, then n integers.
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
        
    #State: Output State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 ones, stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then maps each integer to a corresponding character in the alphabet (a-z), increments the count of the mapped character, and prints the resulting string. The function repeats this process for all test cases, ultimately consuming all input from standard input and producing a series of strings as output.

