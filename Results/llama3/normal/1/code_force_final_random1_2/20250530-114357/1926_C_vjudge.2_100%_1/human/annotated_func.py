#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the largest number Vladislav writes for each test case). Each integer is between 1 and 2*10^5 inclusive.
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: N is greater than 200000, i is a string of length at least 0, t is an integer, pd is a list of 200001 integers where the first element is 0 and the rest are zeros except for the element at index equal to the ASCII value of each character of string i which is increased by the integer value of each character of string i, and pd[2] is increased by pd[1], and pd[i] is increased by the integer value of character j, j is not present in the string i, and pd[i] is increased by pd[i - 1], and pd[i] is increased by the integer value of each character of string i, stdin contains 1 input: a list of integers, j is the last character of string i.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `N` is greater than 200000, `i` is a string of length at least 0, `t` is 0, `pd` is a list of 200001 integers where the first element is 0 and the rest are zeros except for the element at index equal to the ASCII value of each character of string `i` which is increased by the integer value of each character of string `i`, and `pd[2]` is increased by `pd[1]`, and `pd[i]` is increased by the integer value of character `j`, `j` is not present in the string `i`, and `pd[i]` is increased by `pd[i - 1]`, and `pd[i]` is increased by the integer value of each character of string `i`, `j` is the last character of string `i`, `_` is `t`, `n` is a list of integers, and the element at index `n` of the list `pd` is being printed, and `n` is assigned the value `int(stdin input)` where `stdin input` accepts an integer and `int` converts it to an integer, and the element at index `n` of the list `pd` is printed, and stdin is empty.

#Overall this is what the function does:This function reads a list of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents a test case. For each test case, the function prints the sum of the digits of all integers from 1 to the given integer. The function uses a precomputed list `pd` to store the cumulative sum of digits for all integers from 1 to 200001, and uses this list to efficiently compute the sum of digits for each test case.

