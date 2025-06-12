#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a list of integers (the elements of the array). The integer is a positive integer between 2 and 50 (inclusive). The list contains integers between 1 and 10^6 (inclusive).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] < a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all = all([(a[0] > new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: `t` is 0, `n` is undefined, `a` is undefined, `check_all` is undefined, `new` is undefined, `new_all` is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (array length) followed by a list of integers (array elements). It checks if the array is sorted in ascending order. If the array is sorted, it prints 'YES'. If the array is not sorted, it checks if the array can be sorted by removing the first element and then printing 'YES' if the remaining array is sorted in ascending order, otherwise it prints 'NO'. The function processes all test cases and does not return any value.

