#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: Output State: The variable `a` remains unchanged and is still assigned the string 'abcdefghijklmnopqrstuvwxyz'. The variable `b` is reinitialized to `[0] * 26` in each iteration of the loop, and its final value is `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]` after the last iteration of the loop. The variable `n` is reassigned the value of the last test case, which is an integer between 1 and 2 * 10^5. The variable `s` is reassigned the list of integers of the last test case. The variable `r` is reassigned the string that is the concatenation of the characters of `a` at the indices specified by the elements of `s`, with each index incremented by 1 after each use. The variable `t` is reassigned the value of the number of test cases minus 1. The variable `x` is reassigned the index of the last element of `s` in `b`. The variable `i` is reassigned the last element of `s`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then generates a string by mapping each integer to a character in the alphabet (with 'a' corresponding to 0, 'b' to 1, and so on), incrementing the corresponding index in the alphabet for each occurrence. The function prints the resulting string for each test case.

