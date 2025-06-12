#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 ≤ n ≤ 10^5). The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: `n` is an integer, `s` is a string, `t` is a string, `a` is 0, `b` is 0, `_` is the number of test cases, stdin is empty, and the maximum difference between the number of positions where `s` is greater than `t` and the number of positions where `s` is less than `t` for each test case has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two strings s and t of length n. It calculates the maximum difference between the number of positions where s is greater than t and the number of positions where s is less than t for each test case, and prints this maximum difference. The function processes all test cases and leaves the standard input empty after execution.

