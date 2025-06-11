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
        
    #State: The output state contains t lines, each of which is either 'Sasha' or 'Anna'. The i-th line corresponds to the i-th test case. If the length of the string rev_res is greater than or equal to max_power + 1, the i-th line is 'Sasha'; otherwise, it is 'Anna'.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and m, representing the length of a list and a maximum power, respectively. The second line contains a list of n integers. The function then sorts the list based on the length of each integer (excluding trailing zeros) and constructs a new string by concatenating the sorted integers, with even-indexed integers having their trailing zeros removed. Finally, the function prints 'Sasha' if the length of the constructed string is greater than or equal to m + 1, and 'Anna' otherwise.

