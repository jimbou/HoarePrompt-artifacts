#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length as the integer. The integer is greater or equal to 2 and less or equal to 2 * 10^5. The sum of the integers over all test cases does not exceed 2 * 10^5.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: a is a list containing two strings, n is an integer between 2 and 2 * 10^5 (inclusive), stdin contains multiple test cases - 3
    s = []
    x = 0
    y = 0
    for i in range(n - 1):
        if a[0][i + 1] == '0' and a[1][i] == '1':
            y = i
        
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: Output State: The list s contains a string that is a combination of the first i + 1 characters of the first string in list a and the ith character to the end of the second string in list a, where i is the index at which the loop broke. The integer x is equal to i. The integer y is equal to the index of the last occurrence of '0' in the first string and '1' in the second string before the loop broke. If the loop did not break, the list s contains a string that is a combination of the first string in list a and the last character of the second string in list a, and the integer x is equal to n - 1.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: The list s contains a string that is a combination of the first i + 1 characters of the first string in list a and the ith character to the end of the second string in list a, where i is the index at which the loop broke. The integer x is equal to i. The integer y is equal to the index of the last occurrence of '0' in the first string and '1' in the second string before the loop broke. The integer t is equal to x - i + 1.
    print(s, sep='')
    #This is printed: the string s (which is a combination of the first i + 1 characters of the first string in list a and the ith character to the end of the second string in list a)
    print(t)
    #This is printed: 1

#Overall this is what the function does:The function reads input from stdin, which contains multiple test cases. Each test case consists of an integer and two binary strings of the same length as the integer. The function processes each test case by finding the first occurrence of a '1' in the first string and a '0' in the second string, and then combines the first part of the first string with the second part of the second string to form a new string. If no such occurrence is found, it combines the first string with the last character of the second string. The function then finds the longest common suffix between the second string and the new string, and prints the new string and the length of the common suffix.

