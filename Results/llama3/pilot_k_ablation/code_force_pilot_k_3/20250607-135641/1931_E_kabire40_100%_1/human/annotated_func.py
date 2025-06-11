#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: stdin contains 0 test cases, y is equal to the initial value of t, list_len is an integer that must be greater than or equal to 0, max_power is an integer, operational_list is a sorted list of strings, x is equal to list_len, rev_res is a string that is the concatenation of all the strings in operational_list with trailing zeros removed if the index of the string is even. If the length of rev_res is greater than or equal to max_power + 1, then 'Sasha' is being printed. Otherwise, 'Anna' is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers: the length of a list and a maximum power. The second line contains a list of integers as strings. The function sorts the list based on the length of the strings after removing trailing zeros, then concatenates the sorted strings, removing trailing zeros from even-indexed strings. It compares the length of the concatenated string to the maximum power and prints 'Sasha' if the length is greater than or equal to the maximum power plus one, and 'Anna' otherwise. The function repeats this process for all test cases provided in the input.

