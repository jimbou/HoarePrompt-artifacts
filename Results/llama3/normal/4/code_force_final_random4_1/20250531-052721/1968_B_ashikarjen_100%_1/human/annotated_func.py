#State of the program right berfore the function call: stdin contains t test cases. Each test case contains three lines. The first line contains two integers n and m. The second line contains a binary string a of length n. The third line contains a binary string b of length m. 1 <= t <= 10^4, 1 <= n, m <= 2 * 10^5.
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: t is reduced by 1, stdin contains t-1 test cases, n is an integer, m is an integer, a is a binary string of length n, b is a binary string of length m, k is the number of times a character in a matches a character in b, i is equal to n, j is equal to m.
    print(k)
    #This is printed: k (the number of times a character in string a matches a character in string b)
    return
    #The program returns nothing, as the return statement is empty. The program has finished processing the test cases, and the value of k, which represents the number of times a character in string a matches a character in string b, has been printed for each test case. The values of i and j, which were equal to n and m respectively, remain unchanged. The program has also reduced the value of t by 1, indicating that one test case has been processed.

#Overall this is what the function does:This function processes a series of test cases from standard input, where each test case consists of two binary strings a and b. It compares the characters in string a with those in string b, and prints the number of matching characters. The function does not return any value, but instead prints the count of matching characters for each test case. It processes all test cases provided in the input, one at a time, until all cases have been handled.

