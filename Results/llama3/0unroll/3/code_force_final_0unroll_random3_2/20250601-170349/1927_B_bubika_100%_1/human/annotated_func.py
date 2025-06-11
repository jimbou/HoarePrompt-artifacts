#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: Output State: The variable `a` still contains the string 'abcdefghijklmnopqrstuvwxyz', and the variable `b` and `r` are not defined in the output state because they are local to the loop and are destroyed after each iteration. The stdin is empty because all the test cases have been read and processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then maps each integer to a corresponding character in the alphabet (0 -> 'a', 1 -> 'b', ..., 25 -> 'z') and prints the resulting string for each test case. The function processes all test cases and leaves the standard input empty.

