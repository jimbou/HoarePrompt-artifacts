#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5), followed by t test cases. Each test case contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000), followed by a string s of length m consisting only of the first k lowercase English alphabets.
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
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, us is a set of k lowercase English alphabets starting from 'a', win is an empty set, ans is a list containing all the characters in the string s that are members of the set us and appear after every k-1 characters that are members of the set us, ps is the number of times k characters that are members of the set us appear in the string s, and i is the last character in the string s.
    if (ps >= n) :
        return print('YES')
        #The program returns and prints the string 'YES'
    #State: *stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string, us is a set of k lowercase English alphabets starting from 'a', win is a set, ans is a list containing all the characters in the string s that are members of the set us and appear after every k-1 characters that are members of the set us, ps is the number of times k characters that are members of the set us appear in the string s, and i is the last character in the string s. ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The program returns a string that consists of all characters in string 's' that are members of the set 'us' and appear after every k-1 characters that are members of the set 'us', followed by the last element in the set 'us', and then 'a' repeated (n - length of the string - 1) times, if the last element in the set 'us' is not in the set 'win'. Otherwise, the program does not return anything.

#Overall this is what the function does:This function determines whether a given string contains a certain pattern of characters and returns a corresponding result. It accepts three integers (n, k, m) and a string s as input, where n is the minimum number of times a pattern should appear, k is the number of unique characters in the pattern, and m is the length of the string. The function then checks if the string contains at least n occurrences of the pattern, where the pattern consists of k unique characters that appear in a specific order. If the pattern appears at least n times, the function returns 'YES'. If the pattern appears less than n times, the function returns a string that completes the pattern to meet the minimum requirement of n occurrences. If the last character in the set of unique characters is already present in the current window, the function returns 'NO'.

