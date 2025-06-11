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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum index at which the percentage of zeros and ones in the string is greater than or equal to 50%. If no such index is found, the output is either 0 or the length of the string, depending on whether the percentage of ones in the string is greater than or equal to 50% or not. The list is sorted in ascending order.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string a of length n containing only 0s and 1s. It calculates the minimum index at which the percentage of zeros and ones in the string is greater than or equal to 50%. If no such index is found, it returns either 0 or the length of the string, depending on whether the percentage of ones in the string is greater than or equal to 50% or not. The function returns a list of these minimum indices, one for each test case, sorted in ascending order.

