#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three space-separated integers: n, k, and m, where n, k, and m are non-negative integers. The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: n, k, m are non-negative integers, s is a string of length m, us is a set of the first k lowercase English alphabets, stdin contains multiple test cases - 1, win is an empty set, ans contains all characters in the string s that are part of the set us and are the kth character in a substring of s that consists only of characters in us, ps is the number of times a character in the string s is the kth character in a substring of s that consists only of characters in us.
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: *n, k, m are non-negative integers, s is a string of length m, us is a set of the first k lowercase English alphabets, stdin contains multiple test cases - 1, win is an empty set, ans contains all characters in the string s that are part of the set us and are the kth character in a substring of s that consists only of characters in us, ps is the number of times a character in the string s is the kth character in a substring of s that consists only of characters in us, and ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The program returns a string that starts with all characters in the string `s` that are part of the set `us` and are the `k`th character in a substring of `s` that consists only of characters in `us`, followed by the character `i` that is another element in the set `us` and is not in the set `win`, and then followed by `n - len(ans) - 1` 'a's, where `n` is a non-negative integer, `len(ans)` is the number of characters in the string `ans`, and `ans` contains all characters in the string `s` that are part of the set `us` and are the `k`th character in a substring of `s` that consists only of characters in `us`, if `i` is not in the set `win`. Otherwise, the program does not return any value.

#Overall this is what the function does:This function determines if a given string `s` contains at least `n` substrings of length `k` consisting only of the first `k` lowercase English alphabets. If it does, the function returns 'YES'. If not, it returns a string that starts with all characters in `s` that are part of the first `k` lowercase English alphabets and are the `k`th character in a substring of `s` that consists only of characters in the first `k` lowercase English alphabets, followed by a character that is another element in the first `k` lowercase English alphabets and is not in the set of characters already found, and then followed by `n - len(ans) - 1` 'a's, where `n` is a non-negative integer, `len(ans)` is the number of characters in the string `ans`, and `ans` contains all characters in the string `s` that are part of the first `k` lowercase English alphabets and are the `k`th character in a substring of `s` that consists only of characters in the first `k` lowercase English alphabets.

