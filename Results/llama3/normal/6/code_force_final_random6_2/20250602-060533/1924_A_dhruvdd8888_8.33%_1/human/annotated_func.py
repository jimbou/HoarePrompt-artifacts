#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^5) followed by t test cases. Each test case contains three integers n (1 <= n <= 26), k (1 <= k <= 26), and m (1 <= m <= 1000) followed by a string s of length m consisting of the first k lowercase English alphabets.
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
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, us is a set of k lowercase English alphabets, win is an empty set, ans is a list containing all the characters in the string s that are in the set us and appear in the string s after every k-1 characters that are in the set us, ps is equal to the number of times k characters in the set us appear in the string s consecutively, and i is the last character in the string s.
    if (ps >= n) :
        return print('YES')
        #The program returns and prints the string 'YES'.
    #State: *stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, us is a set of k lowercase English alphabets, win is an empty set, ans is a list containing all the characters in the string s that are in the set us and appear in the string s after every k-1 characters that are in the set us, ps is equal to the number of times k characters in the set us appear in the string s consecutively, and i is the last character in the string s. The number of times k characters in the set us appear in the string s consecutively is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is an empty string, us is an empty set, win is an empty set, ans is a list containing all the characters in the string s that are in the set us and appear in the string s after every k-1 characters that are in the set us, ps is equal to the number of times k characters in the set us appear in the string s consecutively, and the number of times k characters in the set us appear in the string s consecutively is less than n. If i is not in the set win, a string is printed that starts with all the characters in the string s that are in the set us and appear in the string s after every k-1 characters that are in the set us, followed by the current value of i, and then 'a' repeated n - len(ans) - 1 times. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output based on certain conditions. It accepts no parameters and returns no value. The function reads an integer t, followed by t test cases. Each test case contains three integers n, k, and m, and a string s of length m. The function then checks if a certain condition is met, and if so, prints 'YES'. If the condition is not met, it prints 'NO' and then prints a string constructed from the input string s and the set of characters us. The function repeats this process for each test case.

