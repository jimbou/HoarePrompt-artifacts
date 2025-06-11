#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three space-separated integers: n, k, and m, where n, k, and m are positive integers and k <= 26. The second line contains a string s of length m, comprising only of the first k lowercase English alphabets.
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
        
    #State: Output State: The loop has iterated over the string s, and the set win contains the last k unique characters encountered in s. The list ans contains the kth unique character encountered in s, and the integer ps is the number of times k unique characters have been encountered in s. The set us remains unchanged, containing the first k lowercase English alphabets.
    if (ps >= n) :
        return print('YES')
        #The program returns and prints the string 'YES'
    #State: *The loop has iterated over the string s, and the set win contains the last k unique characters encountered in s. The list ans contains the kth unique character encountered in s, and the integer ps is the number of times k unique characters have been encountered in s. The set us remains unchanged, containing the first k lowercase English alphabets. ps is less than n.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The loop has iterated over the set us, and the set win contains the last k unique characters encountered in s. The list ans contains the kth unique character encountered in s, and the integer ps is the number of times k unique characters have been encountered in s. The set us remains unchanged, containing the first k lowercase English alphabets. ps is less than n, and 'NO' is printed. The loop has terminated and returned the string ''.join(ans) + i + 'a' * (n - len(ans) - 1), where i is the first character in us that is not in win.

#Overall this is what the function does:This function determines if a given string can be transformed into a sequence of k unique characters repeated n times by appending characters from a set of the first k lowercase English alphabets. If the string already meets this condition, it prints 'YES'. Otherwise, it prints 'NO' and returns the modified string by appending the first missing character from the set and filling the rest with 'a's to meet the required length.

