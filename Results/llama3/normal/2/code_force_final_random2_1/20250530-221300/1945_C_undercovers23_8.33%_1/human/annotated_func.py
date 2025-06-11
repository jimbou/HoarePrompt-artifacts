#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (greater than or equal to 3) and then a string of 0s and 1s of the same length as the integer.
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
        
    #State: Output State: `_` is equal to `t`, `stdin` is empty, `n` is an integer greater than or equal to 3, `s` is a string of 0s and 1s of the same length as `n`, `pk` is an integer equal to `n // 2` if `n` is even, or `n // 2 - 1` if `n` is odd, `sl` is a list of characters in `s`, `o` is the number of '1's in `s`, `z` is the number of '0's in `s`, `zero` is the number of '0's in the first `n-1` characters of `s`, `one` is the number of '1's in the first `n-1` characters of `s`, `lst` is a list that must have at least `len(lst)` elements, `mini` is the minimum of `pow(10, 8)` and the absolute difference between `pk` and the last element in the list, `i` is `n-1`, `ele` is the last element in the list, `final` is a sorted list containing all elements in the list if the absolute difference between `pk` and the element in the list is equal to `mini`, `zero_perc` is the ceiling of `(zero * 100 / (n-1))`, `one_perc` is the ceiling of `((o - one) * 100 / 1)`, `elem` is the last element in the list, `c1` is the integer part of `o * 100 / n`. If `c1` is greater than or equal to 50, `final` contains an additional element 0. Otherwise, `final` contains `n`, and the first element of the `final` list is printed.
    #
    #In natural language, the output state after the loop executes all the iterations is as follows:
    #
    #The loop has finished executing all the iterations. The variable `_` is equal to the initial value of `t`, indicating that the loop has completed all the iterations. The standard input `stdin` is empty, as all the test cases have been processed. The variables `n`, `s`, `pk`, `sl`, `o`, `z`, `zero`, `one`, `lst`, `mini`, `i`, `ele`, `final`, `zero_perc`, `one_perc`, `elem`, and `c1` have the same values as in the output state after the loop executes 3 times. The first element of the `final` list is printed, which is either 0 or `n` depending on whether `c1` is greater than or equal to 50 or not.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (n) and a string (s) of 0s and 1s of the same length as n. It then calculates the percentage of 0s and 1s in the first n-1 characters of the string and checks if the percentage of 0s is greater than or equal to 50 and the percentage of 1s is also greater than or equal to 50. If this condition is met, it adds the current index to a list. After processing the entire string, it finds the minimum absolute difference between the middle index of the string (pk) and the indices in the list. If no such indices are found, it checks if the percentage of 1s in the entire string is greater than or equal to 50 and adds 0 or n to the list accordingly. Finally, it prints the smallest index in the list.

