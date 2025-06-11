#State of the program right berfore the function call: stdin contains a sequence of test cases. Each test case consists of two lines. The first line contains two integers n and m. The second line contains n integers. n is a positive integer, m is a non-negative integer.
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
        
    #State: stdin contains an empty sequence of test cases, y is equal to the number of test cases, list_len is a string representing an integer greater than or equal to 0, max_power is a string representing the second space-separated input, operational_list is a sorted list of strings, x is equal to the integer value of list_len, rev_res is a string that is the concatenation of the strings in operational_list with all trailing zeros removed if the index is even, and the original string if the index is odd. If the length of rev_res is at least int(max_power) + 1, 'Sasha' is printed. Otherwise, 'Anna' is printed.

#Overall this is what the function does:This function processes a sequence of test cases from standard input. Each test case consists of two lines: the first line contains two integers (n and m), and the second line contains n integers. The function sorts the integers based on their length and trailing zeros, then concatenates them in a specific order (removing trailing zeros from even-indexed integers). If the length of the concatenated string is greater than or equal to m + 1, it prints 'Sasha'; otherwise, it prints 'Anna'. The function repeats this process for each test case in the input sequence.

