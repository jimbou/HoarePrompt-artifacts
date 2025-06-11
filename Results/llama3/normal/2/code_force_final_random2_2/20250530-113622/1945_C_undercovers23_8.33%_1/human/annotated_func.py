#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n // 2
        else:
            pk = n // 2
        
        sl = list(s)
        
        o = sl.count('1')
        
        z = sl.count('0')
        
        zero, one = 0, 0
        
        lst = []
        
        mini = pow(10, 8)
        
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
            zero_perc = math.ceil(zero * 100 / (i + 1))
            one_perc = math.ceil((o - one) * 100 / (n - i - 1))
            if zero_perc >= 50 and one_perc >= 50:
                lst.append(i + 1)
        
        for ele in lst:
            mini = min(mini, abs(pk - ele))
        
        final = []
        
        for elem in lst:
            if abs(pk - elem) == mini:
                final.append(elem)
        
        final.sort()
        
        if len(final) == 0:
            c1 = o * 100 // n
            if c1 >= 50:
                final.append(0)
            else:
                final.append(n)
        
        print(final[0])
        
    #State: `t` is 0, `_` is `t`, `n` is an integer between 3 and 3*10^5, `s` is a string of length `n` consisting only of 0 and 1, stdin contains no test cases, `sl` is a list of characters in `s`, `o` is the number of '1's in `s`, `z` is the number of '0's in `s`, `zero` is the number of '0's in `s`, `one` is the number of '1's in `s`, `zero_perc` is math.ceil(`zero` * 100 / `n`), `one_perc` is math.ceil((`o` - `one`) * 100 / (`n` - `n` + 1)), `lst` is a list containing values `i` + 1 if `zero_perc` >= 50 and `one_perc` >= 50 for all `i` in range(`n` - 1), `ele` is the last element in the list `lst`, `mini` is the minimum of 10^8 and the absolute difference between `pk` and all elements in `lst` and `n` // 2 if `n` is even or (`n`-1)/2 if `n` is odd, `pk` is an integer equal to `n` // 2 if `n` is even or (`n`-1)/2 if `n` is odd, `i` is `n` - 1, `c1` is `o * 100 // n`, `elem` is the last element in the list `lst`, `final` is a sorted list containing all elements in `lst` that have an absolute difference with `pk` equal to the minimum of 10^8 and the absolute difference between `pk` and all elements in `lst` and `n` // 2 if `n` is even or (`n`-1)/2 if `n` is odd. If `c1` is greater than or equal to 50, then `final` contains 0. Otherwise, `n` has been appended to `final`, and the first element of the sorted list `final` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing only 0s and 1s. For each test case, it calculates the percentage of 0s and 1s in the string and finds the indices where the percentage of 0s is greater than or equal to 50% and the percentage of 1s is also greater than or equal to 50%. If such indices exist, it finds the index with the minimum absolute difference from the middle index of the string. If no such indices exist, it checks if the percentage of 1s in the entire string is greater than or equal to 50% and prints 0 if true, otherwise prints the length of the string. The function prints the result for each test case.

