#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains an integer n (1 <= n <= 10^5), the second line contains a string s of n characters ('0' or '1'), and the third line contains a string f of n characters ('0' or '1').
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: The output state will contain t lines, each containing the maximum of a and b, where a is the number of positions where the character in string s is greater than the character in string t, and b is the number of positions where the character in string s is less than the character in string t.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the maximum difference between the number of positions where the character in string s is greater than the character in string t and the number of positions where the character in string s is less than the character in string t for each test case.

