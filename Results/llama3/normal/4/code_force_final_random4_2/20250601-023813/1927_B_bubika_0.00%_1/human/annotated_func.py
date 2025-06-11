#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 integers where the value at index x is equal to the number of times x appears in s and the value at index i is incremented by the number of times i appears in s plus the length of s, t is equal to the number of test cases, n is an integer, s is a list of integers, r is a string containing the characters at index i in 'abcdefghijklmnopqrstuvwxyz' for each i in s, i is the last element in s, and stdin contains 0 inputs, and the string r which contains the characters at index i in 'abcdefghijklmnopqrstuvwxyz' for each i in s is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then generates a string r by mapping each integer in the list to a character in the alphabet (where the mapping is determined by the frequency of each integer), and prints the resulting string. The function processes all test cases and prints the corresponding strings.

