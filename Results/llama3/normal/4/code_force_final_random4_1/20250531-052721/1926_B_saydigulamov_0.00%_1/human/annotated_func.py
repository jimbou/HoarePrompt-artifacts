#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (2 <= n <= 10) followed by n lines each containing n characters 0 or 1.
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: `a` is an integer between 1 and 100 (inclusive), `i` is `a - 1`, `k` is a list containing the count of '1' in each input string that contains '1'. If the first and second counts of '1' in the input strings are equal, the list of counts of '1' in each input string that contains '1' is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case contains a square matrix of 0s and 1s. It counts the number of 1s in each row of the matrix, but only if the row contains at least one 1. If the first and second rows have the same count of 1s, it prints the list of counts of 1s for all rows that contain 1s. The function repeats this process for multiple test cases.

