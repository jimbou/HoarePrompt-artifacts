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
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: The output state after the loop executes all the iterations is a series of counts, each representing the number of pairs of consecutive integers in the sorted list, plus the number of integers in the list minus 2. The counts are printed for each test case. The initial state variables T, n, x, y, and the input lists remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of distinct integers. It calculates and prints the number of pairs of consecutive integers in the sorted list, plus the number of integers in the list minus 2, for each test case. The function does not modify the input variables and only produces output for each test case.

