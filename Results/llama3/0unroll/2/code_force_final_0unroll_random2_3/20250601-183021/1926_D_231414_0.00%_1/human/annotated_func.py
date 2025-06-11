#State of the program right berfore the function call: stdin contains a series of test cases. Each test case consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n space-separated integers a_1, ..., a_n (0 ≤ a_j < 2^31). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: The value of times is 0, check is 2147483647, and stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a single integer n followed by n space-separated integers. For each test case, it calculates the number of pairs of integers that are complementary (i.e., their bitwise XOR is equal to 2^31-1) and prints the number of non-complementary integers. The function processes all test cases and leaves the input stream empty.

