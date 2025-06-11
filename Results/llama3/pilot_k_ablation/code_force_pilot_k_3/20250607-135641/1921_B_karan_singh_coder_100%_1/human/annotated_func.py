#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise. The sum of n over all test cases does not exceed 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: n is greater than or equal to 0, s is a string, t is a string, a is equal to its original value plus the number of times the character at index i in s is greater than the character at index i in t, b is equal to its original value plus the number of times the character at index i in s is less than the character at index i in t, i is equal to n, stdin contains multiple test cases minus all inputs: n, s, t, and the maximum of a and b is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an integer n, a string s, and a string t. It then compares the characters in s and t, counting the number of times a character in s is greater than or less than the corresponding character in t. Finally, it prints the maximum of these two counts for each test case.

