#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (t) and then a list of t integers (a_1, a_2, ..., a_t) where 1 <= t <= 10^4 and 0 <= a_j < 2^31.
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = 0
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            else:
                if s not in dic:
                    dic[s] = 0
                dic[s] += 1
                ans += 1
        
        print(ans)
        
    #State: stdin is empty, times is 0, check is 2147483647

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (t) followed by a list of t integers. It then processes each test case by iterating through the list of integers, performing bitwise XOR operations with a predefined constant (2^31 - 1), and maintaining a dictionary to keep track of the occurrences of each integer and its XOR complement. The function outputs the total count of integers that have a corresponding XOR complement in the dictionary, effectively counting the number of pairs of integers that XOR to the predefined constant. After processing all test cases, the function leaves the standard input empty.

