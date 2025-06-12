#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase English letters and having a length of at most 10.
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
        
    #State: cnt_test_cases is an integer between 1 and 1000 (inclusive), i is equal to cnt_test_cases, string is the last string read from stdin, stdin is empty, m is the first character of the last string, k is the number of occurrences of m in the last string.

#Overall this is what the function does:This function reads a specified number of strings from standard input, checks if each string has all unique characters or not, and prints 'Yes' followed by the sorted string if it has unique characters, otherwise prints 'No'. The function processes all input strings and does not return any value.

