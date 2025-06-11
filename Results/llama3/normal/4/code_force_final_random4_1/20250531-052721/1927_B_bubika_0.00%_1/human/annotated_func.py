#State of the program right berfore the function call: stdin contains a number of test cases t, where 1 <= t <= 10^4. For each test case, stdin contains a single integer n, where 1 <= n <= 2 * 10^5, followed by n integers a_1, a_2, ..., a_n, where 0 <= a_i < n.
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
        
    #State: a is 'abcdefghijklmnopqrstuvwxyz', b is a list of 26 integers where the value at index x is equal to the sum of the number of times x appears in s for all test cases, t is equal to the number of test cases, n is an integer equal to the last input, s is an empty list, i is the last integer in the last list, r is a string containing a sequence of characters where each character is the x-th letter of the alphabet and the number of times each character appears is equal to the sum of the number of times x appears in s for all test cases, stdin is empty, and r is printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, where each test case consists of an integer n followed by n integers. It then generates a string r by mapping each integer to its corresponding alphabet letter (0 -> 'a', 1 -> 'b', ..., 25 -> 'z') and increments a counter for each letter. The function prints the resulting string r for each test case.

