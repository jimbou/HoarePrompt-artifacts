#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to min(n, 2*10^5), and y is 0. The second line contains x distinct integers from 1 to n.
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
        
    #State: T is 0, _ is T, n is an integer, x is an integer, y is an integer, list0 is a sorted list of integers, i is x - 1, and count is the number of consecutive pairs of elements in list0 that have a difference of 2. If n - list0[-1] is 1, then count is increased by 1. Otherwise, no changes are made.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to min(n, 2*10^5), and y is 0. The second line contains x distinct integers from 1 to n. The function then sorts the list of integers, counts the number of consecutive pairs of elements that have a difference of 2, and increments the count if the difference between n and the last element in the list is 1. Finally, it prints the count plus x minus 2 for each test case.

