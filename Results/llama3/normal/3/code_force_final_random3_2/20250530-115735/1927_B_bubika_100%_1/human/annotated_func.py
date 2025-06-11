#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 integers where the integer at index x is equal to the number of times the integer x appears in the list s and all other integers are 0, n is an integer between 1 and 2 * 10^5, s is an empty list, i is the last integer in the list, r is a string containing the characters at the indices of the integers in the list s in the order they appear, t is equal to the number of test cases, stdin contains 0 test cases, and the string r containing the characters at the indices of the integers in the list s in the order they appear is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then maps each integer in the list to a corresponding character in the alphabet (where 0 maps to 'a', 1 maps to 'b', and so on) and prints the resulting string for each test case. The function does not return any value, but instead prints the results directly to standard output.

