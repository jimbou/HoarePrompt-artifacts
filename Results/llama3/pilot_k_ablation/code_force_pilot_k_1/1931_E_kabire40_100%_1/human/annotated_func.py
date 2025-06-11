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
        
    #State: stdin is empty, y is t, rev_res is an empty string, list_len is 0, operational_list is an empty list, max_power is 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and m, and the second line contains n integers. It then processes these integers by sorting them based on their length without trailing zeros, concatenating them in a specific order (alternating between removing trailing zeros and keeping them), and comparing the length of the resulting string to the value of m. Based on this comparison, it prints either 'Sasha' or 'Anna' for each test case. After processing all test cases, the function leaves the input stream empty and the variables used within the function in their initial state.

