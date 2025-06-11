#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n / 2
        else:
            pk = n / 2
        
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
            zero_perc = zero * 100 // (i + 1)
            one_perc = (o - one) * 100 // (n - i - 1)
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
        
    #State: `t` is 0, `_` is `t`, `n` is an integer between 3 and 3*10^5 inclusive, `s` is a string of length `n` consisting only of 0 and 1, `o` is an integer equal to the number of '1' in `s`, `z` is an integer equal to the number of '0' in `s`, `zero` is equal to `z`, `one` is equal to `o`, `lst` is a list containing all indices `i` where `zero_perc` >= 50 and `one_perc` >= 50, `mini` is the minimum of 10^8 and the absolute difference between `n / 2` and all elements in `lst`, `sl` is a list of characters of `s`, `pk` is a float equal to `n / 2` if `n` is even, or an integer equal to `n / 2` if `n` is odd, `i` is -1, `ele` is the last element in `lst`, `zero_perc` is an integer equal to `z * 100 // n`, `one_perc` is an integer equal to `o * 100 // n`, stdin is empty, `elem` is the last element in the list, `final` is a sorted list containing all elements in `lst` where `abs(pk - elem)` is equal to `mini`. If `c1` is greater than or equal to 50, `final` also contains 0. Otherwise, `final` also contains `n` and `c1` is less than 50, and the first element of the final list is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string a of length n containing only 0s and 1s. It calculates the percentage of 0s and 1s in the string and finds the indices where the percentage of 0s and 1s is greater than or equal to 50%. It then finds the index that is closest to the middle of the string and prints the smallest such index. If no such index is found, it prints 0 if the percentage of 1s is greater than or equal to 50%, otherwise it prints the length of the string.

