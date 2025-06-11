#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: The output state will contain the smallest missing positive integer in each test case. If there are no missing positive integers, it will print the first integer that appears only once in the array. If all integers appear more than once, it will print the smallest positive integer that is not in the array.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers. It identifies and prints the smallest missing positive integer in each list. If no positive integers are missing, it prints the first integer that appears only once in the list. If all integers appear more than once, it prints the smallest positive integer not present in the list.

