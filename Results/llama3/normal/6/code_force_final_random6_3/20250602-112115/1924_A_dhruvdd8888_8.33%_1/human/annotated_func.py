#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000) followed by a string s of length m consisting only of the first k lowercase English alphabets.
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
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, us is a set of the first k lowercase English alphabets, win is an empty set, ans is a list containing all the characters in s that are in the set us and appear in the string after the previous k characters in the list have appeared, ps is the number of times k characters in the set us have appeared in the string, and i is the last character in the string.
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: *stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string, us is a set of the first k lowercase English alphabets, win is a set, ans is a list containing all the characters in s that are in the set us and appear in the string after the previous k characters in the list have appeared, ps is the number of times k characters in the set us have appeared in the string, and i is the last character in the string. The number of times k characters in the set us have appeared in the string is less than n.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: `stdin` contains t-1 test cases, `n` is an integer between 1 and 26, `k` is an integer between 1 and 26, `m` is an integer between 1 and 1000, `s` is a string, `us` is an empty set, `win` is a set, `ans` is a list containing all the characters in `s` that are in the set `us` and appear in the string after the previous `k` characters in the list have appeared, `ps` is the number of times `k` characters in the set `us` have appeared in the string, and `i` is the last element in `us`. If `i` is not in `win`, a string that is a combination of the characters in the list `ans` and the character `i` followed by `n - len(ans) - 1` 'a's is printed.

#Overall this is what the function does:This function determines whether a given string can be rearranged to contain a specified number of substrings, each consisting of a set of unique characters. If possible, it returns 'YES'. Otherwise, it generates and prints all possible combinations of characters that can be appended to the original string to meet the requirement.

