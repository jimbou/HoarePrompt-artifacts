#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings s, each consisting of lowercase English letters and having a length of at most 10.
    cnt_test_cases = int(input())
    for i in range(cnt_test_cases):
        string = input().strip()
        
        if len(string) == 1:
            print('No')
        
        m = string[0]
        
        k = 0
        
        for i in range(len(string)):
            if string[i] == m:
                k += 1
        
        if k == len(string):
            print('No')
        else:
            print('Yes')
            print(''.join(sorted(string)))
        
    #State: cnt_test_cases is equal to 0, i is equal to cnt_test_cases, string is an empty string, m is an empty string, k is equal to 0, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case is a string of lowercase English letters. For each test case, it checks if all characters in the string are the same. If they are, it prints 'No'. If not, it prints 'Yes' followed by the sorted string. The function processes all test cases and then terminates, leaving the input stream empty.

