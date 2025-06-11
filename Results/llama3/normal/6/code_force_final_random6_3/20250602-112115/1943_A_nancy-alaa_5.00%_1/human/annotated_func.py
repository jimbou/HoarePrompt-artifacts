#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: n is an integer, i is n, arr is a list of integers, mpp is a dictionary where keys are elements from arr and values are their respective counts, first is True if any element in arr has a count of 1, otherwise False, stdin contains 0 inputs.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds and prints the smallest missing non-negative integer in the list, or the smallest integer that appears only once if all non-negative integers are present. The function processes all test cases and consumes all input from standard input.

