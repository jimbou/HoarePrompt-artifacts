#State of the program right berfore the function call: stdin contains a sequence of lines. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6). Each of the following t lines contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: stdin contains a sequence of lines minus 2t lines, y is t, rev_res is a string that is a combination of strings from operational_list, where even-indexed strings have trailing zeros removed, list_len and max_power are strings, operational_list is a list of strings sorted by the difference between the length of each string and the length of the string without trailing zeros. Either 'Sasha' or 'Anna' is printed t times.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts no parameters and returns no value. The function reads a sequence of lines from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads two lines: the first line contains two integers n and m, and the second line contains n integers. The function processes these integers, combines them into a string, removes trailing zeros from even-indexed strings, and checks if the length of the resulting string is greater than or equal to m + 1. Based on this check, it prints either 'Sasha' or 'Anna' for each test case. After processing all test cases, the function concludes, leaving stdin with a reduced number of lines and printing the results of the comparisons.

