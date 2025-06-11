#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: n is an integer greater than or equal to 0, arr is a list of integers, mpp is a dictionary where keys are elements from arr and values are their respective counts, stdin contains no input, i is n, first is True if there exists an element in arr that appears only once, False otherwise.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds and prints the smallest positive integer that is either missing from the list or appears only once. If no such integer exists, it prints the smallest positive integer greater than n. The function processes all test cases and does not return any value.

