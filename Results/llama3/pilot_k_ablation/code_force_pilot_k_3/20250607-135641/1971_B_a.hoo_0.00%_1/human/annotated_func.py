#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t strings, each consisting of lowercase English letters of length at most 10.
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
        
    #State: `cnt_test_cases` is between 1 and 1000 (inclusive), `i` is equal to `cnt_test_cases`, `string` is the last string that was inputted by the user with leading and trailing whitespaces removed, `m` is the first character of the last string, and `k` is equal to the number of occurrences of `m` in the last string. If `k` is equal to the length of the last string, 'No' is printed. Otherwise, 'Yes' is printed, and the sorted characters of the last string are printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case is a string of lowercase English letters. It then checks if the string consists of all the same characters. If the string has only one character or all characters are the same, it prints 'No'. Otherwise, it prints 'Yes' followed by the characters of the string in sorted order. The function processes multiple test cases, with the number of test cases provided as the first input.

