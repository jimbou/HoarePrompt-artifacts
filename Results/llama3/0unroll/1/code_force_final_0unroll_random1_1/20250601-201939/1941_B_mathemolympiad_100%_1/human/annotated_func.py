#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (3 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    numTest = int(input())
    for _ in range(0, numTest):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        stop = False
        
        for i in range(0, n - 2):
            if a[i] < 0:
                print('NO')
                stop = True
                break
            opNum = a[i]
            a[i] -= opNum
            a[i + 1] -= 2 * opNum
            a[i + 2] -= opNum
        
        if stop == True:
            continue
        
        if a[len(a) - 1] != 0 or a[len(a) - 2] != 0:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will contain the results of the loop's execution for each test case. For each test case, if the loop finds a negative number in the array a, it will print 'NO' and move on to the next test case. If the loop successfully iterates through the array without finding a negative number, it will check if the last two elements of the array are zero. If they are, it will print 'YES', otherwise it will print 'NO'. The output state will contain these 'YES' or 'NO' results for each test case, separated by newline characters. The value of numTest will be unchanged, as it is not modified within the loop.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs 'YES' or 'NO' for each case. It takes an integer t (number of test cases) followed by t test cases, each consisting of an integer n (number of elements) and n integers. The function checks if the integers in each test case can be transformed into zeros by a series of operations, printing 'YES' if possible and 'NO' otherwise. If a negative number is encountered during the transformation, it immediately prints 'NO' and moves on to the next test case. The output is a series of 'YES' or 'NO' results, one for each test case, separated by newline characters.

