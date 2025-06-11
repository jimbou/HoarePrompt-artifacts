#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and m. The second line contains a string s. n, k, and m are non-negative integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. s is a string of length m consisting of the first k lowercase English alphabets.
    n, k, m = tuple(map(int, input().split()))
    s = input()
    us = set(chr(i + 97) for i in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
        
    #State: n is a non-negative integer between 1 and 26, k is a non-negative integer between 1 and 26, m is a non-negative integer between 1 and 1000, s is an empty string, us is a set of the first k lowercase English alphabets, win is a set, ans is a list containing all the characters in the string s that are in the set us and appear after every k-1 characters in the string s, ps is the number of times the length of win is equal to k, stdin contains multiple test cases minus one, and i is the last character in the string s.
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: *n is a non-negative integer between 1 and 26, k is a non-negative integer between 1 and 26, m is a non-negative integer between 1 and 1000, s is an empty string, us is a set of the first k lowercase English alphabets, win is a set, ans is a list containing all the characters in the string s that are in the set us and appear after every k-1 characters in the string s, ps is the number of times the length of win is equal to k, stdin contains multiple test cases minus one, and i is the last character in the string s. ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The program returns a string that starts with the characters in the list `ans` (which contains all the characters in the string `s` that are in the set `us` and appear after every `k-1` characters in the string `s`), followed by the character `i` (which is the last element in the set `us`), and then padded with `n - len(ans) - 1` 'a' characters to make the total length of the string equal to `n`, if `i` is not in the set `win`. Otherwise, no string is returned.

#Overall this is what the function does:The function reads input from stdin, processes it, and returns either 'YES' or a constructed string. It takes no parameters and returns a value based on the input. The function's purpose is to determine if a certain condition is met in the input string and return 'YES' if it is, or construct a string based on the input and return it if the condition is not met. The final state of the program after it concludes is that it has processed one test case from stdin and returned either 'YES' or a constructed string.

