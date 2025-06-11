#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (0 <= a_i < n) representing the trace of the lost string.
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
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 integers where the value at index x is equal to the number of times x appears in s, n is an integer greater than 0, s is a list of integers that must have at least n elements, i is the nth integer in the list s, r is a string containing the character at the index of the nth integer in the list s in the string 'abcdefghijklmnopqrstuvwxyz' plus the character at the index of the (n-1)th integer in the list s in the string 'abcdefghijklmnopqrstuvwxyz' plus the character at the index of the (n-2)th integer in the list s in the string 'abcdefghijklmnopqrstuvwxyz' plus ... plus the character at the index of the 1st integer in the list s in the string 'abcdefghijklmnopqrstuvwxyz', t is n, stdin is empty, and the string r is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers representing a trace of a lost string. It then reconstructs the original string by mapping each integer to its corresponding character in the alphabet, based on the frequency of each integer in the list. The reconstructed string is then printed to the console. The function processes all test cases and empties the standard input.

