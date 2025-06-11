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
        
    #State: The output state after the loop executes all the iterations is a series of 'Sasha' or 'Anna' printed to the console, depending on whether the reversed and sorted number is greater than 10 to the power of max_power for each test case. The input state remains unchanged, with stdin containing the same integer t followed by t test cases.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers (n and m) and the second line contains n integers. It then processes each test case by reversing and sorting the integers, and prints 'Sasha' if the resulting number is greater than 10 to the power of m, and 'Anna' otherwise. The function does not modify the input state.

