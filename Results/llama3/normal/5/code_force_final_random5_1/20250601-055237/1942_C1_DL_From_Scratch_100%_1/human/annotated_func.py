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
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: T is an integer greater than or equal to 0, n is an integer, x is an integer, y is an integer, list0 is a sorted list of integers, i is x - 1. If num is equal to 1, count is the number of pairs of adjacent elements in list0 that have a difference of 2 plus 1. Otherwise, count is the number of pairs of adjacent elements in list0 that have a difference of 2. The value of count plus x minus 2 is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, and the second line contains x distinct integers from 1 to n. The function then sorts the list of integers and counts the number of pairs of adjacent elements that have a difference of 2. If the first or last element in the sorted list has a difference of 1 with the start or end of the range [1, n], respectively, it increments the count by 1. Finally, the function prints the count plus x minus 2 for each test case.

