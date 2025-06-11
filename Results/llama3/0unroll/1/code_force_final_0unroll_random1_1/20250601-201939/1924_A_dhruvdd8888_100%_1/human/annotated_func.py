#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case consists of two lines. The first line contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000). The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: Output State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string of length m, us is a set of k lowercase English alphabets starting from 'a', win is an empty set, ans is a list of characters from s that are in us and appear at least k times, ps is the number of times a character from us appears at least k times in s.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES' and returns None, indicating that the number of times a character from the set of k lowercase English alphabets (us) appears at least k times in the string s is greater than or equal to n.
    #State: *stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string of length m, us is a set of k lowercase English alphabets starting from 'a', win is an empty set, ans is a list of characters from s that are in us and appear at least k times, ps is the number of times a character from us appears at least k times in s. ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The loop will print a string consisting of the characters in ans, followed by the first character in us that is not in win, and then 'a' repeated (n - len(ans) - 1) times. The loop will terminate after the first iteration, as it encounters a return statement. The values of other variables remain unchanged.

#Overall this is what the function does:This function determines if a given string contains at least 'n' characters from a set of 'k' lowercase English alphabets, each appearing at least 'k' times. If the condition is met, it prints 'YES' and returns None. Otherwise, it prints 'NO' and constructs a new string by appending a character from the set that appears less than 'k' times and filling the remaining positions with 'a's, then prints this new string.

