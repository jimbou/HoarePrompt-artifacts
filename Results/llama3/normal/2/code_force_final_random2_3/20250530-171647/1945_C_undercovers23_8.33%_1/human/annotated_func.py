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
        
    #State: t is 0, n is an integer and must be greater than i, s is a string, stdin contains no test cases, sl is a list of characters in s, o is the count of '1' in s, z is the count of '0' in s, zero is the count of '0' in s, one is the count of '1' in s, lst is a list containing the values i + 1 where zero_perc >= 50 and one_perc >= 50, mini is the minimum of 100000000 and the absolute difference between pk and all elements in lst, i is n, ele is the last element in lst, final is a sorted list containing all elements in lst where the absolute difference between pk and the element equals mini. If c1 is greater than or equal to 50, final is a list containing 0. Otherwise, final is a list containing the value n. The first element of the final list is not being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing only 0s and 1s. It calculates the percentage of 0s and 1s in the string and finds the indices where the percentage of 0s is at least 50% and the percentage of 1s is at least 50% in the remaining string. If such indices exist, it finds the index that is closest to the middle of the string and prints it. If no such indices exist, it prints 0 if the percentage of 1s in the entire string is at least 50%, and n otherwise. The function processes all test cases and prints the results.

