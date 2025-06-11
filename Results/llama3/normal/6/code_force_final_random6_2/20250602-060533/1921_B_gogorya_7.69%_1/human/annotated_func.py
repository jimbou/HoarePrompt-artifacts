#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains an integer n (1 <= n <= 10^5), the second line contains a string s of n characters ('0' or '1'), and the third line contains a string f of n characters ('0' or '1').
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: t is an integer between 1 and 10^4 (inclusive), _ is t, n is an integer, s1 is a string, s2 is a string, a1 is an integer equal to the number of '1' in s1, a2 is an integer equal to the number of '1' in s2, res is an integer equal to the absolute difference between a1 and a2 plus the number of iterations where s1[i] is '1' and s2[i] is '0', i is n-1, stdin is empty, and res is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It calculates the absolute difference between the number of '1's in two input strings and then increments this difference by the number of positions where the first string has '1' and the second string has '0', but only if the difference is not already positive. The function repeats this process for each test case and prints the final result for each case.

