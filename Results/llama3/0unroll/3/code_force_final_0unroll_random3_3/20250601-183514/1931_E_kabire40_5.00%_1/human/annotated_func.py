#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains two lines. The first line contains two integers n and m (1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The output state will be a series of 'Sasha' or 'Anna' printed to the console, one for each test case. The output will depend on whether the reversed and sorted number is greater than 10 to the power of the given max_power. If it is, 'Sasha' will be printed, otherwise 'Anna' will be printed. The number of outputs will be equal to the initial integer t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and m, and the second line contains n integers. The function processes these integers by reversing them and sorting them in a specific way. It then compares the resulting number to 10 raised to the power of m. If the resulting number is greater, it prints 'Sasha' to the console; otherwise, it prints 'Anna'. The function repeats this process for each test case, printing one result per case.

