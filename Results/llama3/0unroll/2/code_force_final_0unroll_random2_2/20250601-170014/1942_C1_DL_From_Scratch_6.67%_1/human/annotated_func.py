#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n.
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
        
    #State: The number of test cases T has been executed, and for each test case, the number of pairs of consecutive integers in the sorted list of x distinct integers from 1 to n, plus x - 2, has been printed. The initial state remains unchanged except for the printed output.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, and the second line contains x distinct integers from 1 to n. For each test case, it sorts the list of integers, counts the number of pairs of consecutive integers, and prints the count plus x - 2. The function executes this process for the specified number of test cases T, without modifying the initial state except for the printed output.

