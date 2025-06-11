#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers (the elements of array a). The length of the list is equal to the integer. All integers are positive and less than or equal to 10^6.
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
        
    #State: t is 0, n is an integer, a is a list of integers, check_all is a boolean value indicating whether all elements in a are in increasing order, stdin contains no input. If check_all is True, 'YES' is printed. If check_all is False, then if a[i - 1] > a[i], a subset of a starting from index n - 1 is checked. If all elements in this subset are less than a[0] and the subset is sorted in ascending order, 'YES' is printed. Otherwise, 'NO' is printed. If a[i - 1] <= a[i], no action is taken.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the length of the array) and a space-separated list of integers (the elements of array a). It checks if the array is in increasing order. If it is, the function prints 'YES'. If not, it checks a subset of the array starting from the first decreasing element. If all elements in this subset are less than the first element of the original array and the subset is sorted in ascending order, the function prints 'YES'. Otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the input stream empty.

