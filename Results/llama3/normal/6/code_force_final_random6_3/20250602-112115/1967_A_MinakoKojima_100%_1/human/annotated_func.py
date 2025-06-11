#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: ans_list contains the updated values of ans after all test cases have been processed, _ is the number of test cases minus 1, n is an integer, a is a sorted list of integers, stdin is empty, ans is the updated value after adding (ans - 1) * (n - 1) and res for the last test case, res is n - 1 minus the number of differences between consecutive elements in a that are not equal to 0 and are less than or equal to k divided by the index of the element plus 1 plus k modulo n if k is not equal to 0, otherwise no changes are made for the last test case.
    for a in ans_list:
        print(a)
        
    #State: ans_list contains the updated values of ans after all test cases have been processed and must have at least as many elements as the number of test cases, _ is the number of test cases minus 1, n is an integer, a is the last element in the list, stdin is empty, ans is the updated value after adding (ans - 1) * (n - 1) and res for the last test case, res is n - 1 minus the number of differences between consecutive elements in a that are not equal to 0 and are less than or equal to k divided by the index of the element plus 1 plus k modulo n if k is not equal to 0, otherwise no changes are made for the last test case, and the last element of the list which is a is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function processes each test case by sorting the integers, calculating a value 'ans' based on the differences between consecutive integers and the value of k, and appending this value to a list. After processing all test cases, the function prints the calculated values for each test case.

