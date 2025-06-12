#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains two lines. The first line contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for y in range(int(input())):
        rev_res = ''
        
        list_len, max_power = input().split()
        
        operational_list = sorted(input().split(), key=lambda x: len(x.rstrip('0')) -
            len(x))
        
        for x in range(int(list_len)):
            if x % 2 == 0:
                rev_res += operational_list[x].rstrip('0')
            else:
                rev_res += operational_list[x]
        
        if len(rev_res) >= int(max_power) + 1:
            print('Sasha')
        else:
            print('Anna')
        
    #State: stdin is empty, y is equal to t, list_len and max_power are the last values read from stdin, operational_list is the last list of strings read from stdin, rev_res is a string that contains the concatenation of all the strings in operational_list, with the strings at even indices having their trailing zeros removed, for all test cases. If t is 0, stdin remains unchanged, y is 0, list_len and max_power are undefined, operational_list is undefined, and rev_res is an empty string.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers (n and m) and the second line contains n strings. The function processes each test case by concatenating the strings in a specific order (even-indexed strings have their trailing zeros removed) and then checks if the length of the resulting string is greater than or equal to m+1. Based on this comparison, the function prints either 'Sasha' or 'Anna' for each test case. If there are no test cases (i.e., the input is 0), the function does not modify the input and leaves it unchanged.

