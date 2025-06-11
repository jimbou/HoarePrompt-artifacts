#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains two lines: the first line contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6), and the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: stdin is empty, y is equal to the integer value of t, rev_val is an empty list, rev_res is an empty string, list_len and max_power are strings representing the first and second input values respectively, operational_list is an empty list, x is equal to the length of rev_val. If 10 raised to the power of the integer value of max_power is less than the integer value of rev_res, then 'Sasha' is printed. Otherwise, 'Anna' is printed.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and determines the winner ('Sasha' or 'Anna') based on the processed data. It accepts no parameters and returns no value, instead printing the result for each test case. The function iterates over the test cases, reverses and sorts certain numbers, and compares the result to a given power of 10 to decide the winner. After processing all test cases, stdin is left empty.

