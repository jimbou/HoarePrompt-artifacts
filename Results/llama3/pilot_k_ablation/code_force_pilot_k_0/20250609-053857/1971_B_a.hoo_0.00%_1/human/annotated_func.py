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
        
    #State: The loop will print 'No' for each string of length 1 or each string consisting of the same character repeated one or more times, and 'Yes' followed by the sorted string for all other strings. The value of `cnt_test_cases` remains unchanged.

#Overall this is what the function does:This function reads a specified number of strings from standard input, checks each string for uniqueness of characters, and prints 'No' if the string has only one character or all characters are the same, otherwise prints 'Yes' followed by the sorted string. The function does not modify the input count of test cases.

