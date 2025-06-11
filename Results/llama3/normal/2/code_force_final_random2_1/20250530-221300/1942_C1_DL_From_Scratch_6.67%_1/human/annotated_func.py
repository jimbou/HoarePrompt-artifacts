#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to min(n, 2 * 10^5), and y is 0. The second line contains x distinct integers from 1 to n.
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
        
    #State: T is a positive integer greater than or equal to 1, n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to min(n, 2 * 10^5), y is a positive integer, list0 is a sorted list of x distinct integers from 1 to n, stdin contains 0 test cases, i is -1, count is the number of times n - list0[-1] equals 1 and x is the number of distinct integers in list0, and count + x - 2 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, where n is a positive integer greater than or equal to 4, x is a positive integer greater than or equal to 2 and less than or equal to min(n, 2 * 10^5), and y is 0. The second line contains x distinct integers from 1 to n. The function then sorts these integers, counts the number of times the difference between consecutive integers is 1, and adds the number of distinct integers minus 2. Finally, it prints this count for each test case.

