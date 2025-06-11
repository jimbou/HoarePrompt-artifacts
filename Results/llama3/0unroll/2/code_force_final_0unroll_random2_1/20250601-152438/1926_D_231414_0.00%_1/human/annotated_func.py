#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n space-separated integers (0 <= a_j < 2^31). The sum of n over all test cases does not exceed 2 * 10^5.
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: stdin is empty, times is 0, check is 2147483647.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It then processes each test case by iterating through the integers, performing bitwise XOR operations with a predefined constant (2^31 - 1), and maintaining a dictionary to keep track of the count of each integer and its XOR result. The function prints the updated count of integers that do not have a pair with the same XOR result after each iteration. After processing all test cases, the function leaves the standard input empty and sets the variable 'times' to 0.

