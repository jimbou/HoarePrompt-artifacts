#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n.
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = n - list0[-1]
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: The number of test cases T has been executed, and for each test case, the number of pairs of consecutive integers in the list, plus the number of integers that are one less than the next integer in the list, minus 2, has been printed to the console. The input list has been sorted in ascending order. The variables n, x, y, list0, and count have been updated for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of distinct integers. It sorts the list in ascending order, then counts the number of pairs of consecutive integers and the number of integers that are one less than the next integer in the list. Finally, it prints the total count minus 2 to the console for each test case.

