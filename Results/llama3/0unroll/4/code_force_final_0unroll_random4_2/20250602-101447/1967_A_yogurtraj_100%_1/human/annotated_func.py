#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the first line contains two integers n and k (1 ≤ n ≤ 2 × 10^5, 0 ≤ k ≤ 10^12) separated by a space, where n is the number of distinct types of cards and k is the number of coins. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12) separated by a space, representing the number of cards of type i.
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The output state is a series of integers, each representing the number of cards of a specific type, printed on separate lines. The number of lines is equal to the number of test cases (t). For each test case, the output is calculated based on the number of distinct types of cards (n), the number of coins (k), and the sorted list of card types (a). The output is either (r - 1) * n + 1 + k % n or (r - 1) * n + 1 + rem + y, depending on whether k is 0 or not, where r is the maximum number of cards of a specific type that can be bought with the available coins, and rem and y are intermediate calculations.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of the number of distinct types of cards (n), the number of coins (k), and a list of card types (a). It calculates the maximum number of cards of a specific type that can be bought with the available coins, considering the sorted list of card types, and prints the result for each test case. The output is either the number of cards of the most expensive type that can be bought with the remaining coins or the number of cards of the most expensive type that can be bought with the available coins plus the remaining coins, depending on whether there are remaining coins or not.

