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
        
    #State: Output State: The loop has iterated over the string s, and for each character i, it has checked if i is in the set us. If i is in us, it has added i to the set win. If the length of win is equal to k, it has appended i to the list ans, incremented ps by 1, and cleared the set win. The final state is: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string of length m, us is a set of k lowercase English alphabets, win is an empty set, ans is a list of characters, ps is an integer greater than or equal to 0.
    if (ps >= n) :
        return print('YES')
        #The program returns and prints the string 'YES'
    #State: stdin contains t-1 test cases, n is an integer between 1 and 26, k is an integer between 1 and 26, m is an integer between 1 and 1000, s is a string of length m, us is a set of k lowercase English alphabets, win is an empty set, ans is a list of characters, ps is an integer less than n.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: The loop will print the string formed by joining the characters in the list 'ans', followed by the first character in the set 'us' that is not in the set 'win', and then 'a' repeated (n - len(ans) - 1) times. The loop will terminate after the first iteration because of the return statement. The value of 'ps' remains unchanged as it is not affected by the loop. The output will not be 'NO' because the loop will print a string before it can reach the print statement outside the loop.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints a string. It accepts three integers (n, k, m) and a string s as input. The function checks if a certain condition is met based on the input values and the string s. If the condition is met, it prints 'YES'. If not, it prints 'NO' and then constructs a new string by appending a character from the set of lowercase English alphabets (us) that is not in the set win, followed by 'a' repeated (n - len(ans) - 1) times, where ans is a list of characters. The function returns after printing the constructed string.

