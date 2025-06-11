#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings s of length at most 10 consisting of lowercase English letters.
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
        
    #State: `cnt_test_cases` is an integer between 1 and 1000, `stdin` is empty, `i` is equal to `cnt_test_cases`, `string` is the last string of length at most 10 consisting of lowercase English letters that was read from `stdin`, `k` is the number of occurrences of the first character `m` in the last string, and the output contains 'Yes' or 'No' for each string that was read from `stdin`, along with a sorted version of the string if 'Yes' was printed.

#Overall this is what the function does:This function reads a series of strings from standard input, determines if each string contains more than one unique character, and prints 'Yes' along with the sorted string if it does, or 'No' if it doesn't. The function processes a specified number of test cases, as indicated by an initial integer input, and prints the results for each case.

