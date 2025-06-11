#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for y in range(int(input())):
        rev_val = []
        
        rev_res = ''
        
        list_len, max_power = input().split()
        
        operational_list = input().split()
        
        for x in operational_list:
            x_rev = int(x[::-1])
            if len(str(x_rev)) == len(x):
                rev_res = rev_res + x
            else:
                rev_val.append(x[::-1])
        
        rev_val.sort()
        
        for x in range(len(rev_val)):
            if x % 2 == 0:
                val_in = int(rev_val[x])
                rev_res += str(val_in)
            else:
                val_in = rev_val[x]
                rev_res += val_in[::-1]
        
        if 10 ** int(max_power) < int(rev_res):
            print('Sasha')
        else:
            print('Anna')
        
    #State: stdin is empty, y is equal to the integer value of the input t, list_len and max_power are strings representing the last two input values respectively, operational_list is an empty list, rev_val is an empty list, rev_res is a string containing all strings in the last operational_list that have the same length as their reverse plus the string representation of the integer value of the reverse of all strings in the last operational_list that have a different length than their reverse and are at even indices in rev_val plus the reverse of all strings in the last operational_list that have a different length than their reverse and are at odd indices in rev_val, x is the length of rev_val, x_rev is the integer value of the reverse of the last string in the last operational_list. If 10 raised to the power of max_power is less than the integer value of rev_res, 'Sasha' is printed. Otherwise, 'Anna' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and m, and the second line contains n integers. The function processes these integers by reversing them and checking if the reversed integer has the same length as the original. If it does, the original integer is appended to the result string. If it doesn't, the reversed integer is appended to a separate list. The list is then sorted, and the integers at even indices are appended to the result string as integers, while the integers at odd indices are appended as strings. Finally, the function compares the result string to 10 raised to the power of m and prints 'Sasha' if the result string is greater, and 'Anna' otherwise. The function repeats this process for each test case and empties the standard input.

