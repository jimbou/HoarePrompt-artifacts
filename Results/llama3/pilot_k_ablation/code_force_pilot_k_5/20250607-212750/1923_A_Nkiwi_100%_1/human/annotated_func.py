#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains an integer n, and the second line contains a space-separated list of n integers. Each integer in the list is either 0 or 1.
    t = int(input())
    for _ in range(t):
        length = int(input())
        
        arrs = list(map(int, input().split()))
        
        sIdx = 0
        
        eIdx = length - 1
        
        while sIdx < length and arrs[sIdx] == 0:
            sIdx += 1
        
        while eIdx >= 0 and arrs[eIdx] == 0:
            eIdx -= 1
        
        cnt0 = 0
        
        for i in range(sIdx, eIdx + 1):
            if arrs[i] == 0:
                cnt0 += 1
        
        print(cnt0)
        
    #State: `t` is an integer that must be at least 1, `length` is an integer, `arrs` is a list of `length` integers that must have at least one non-zero element, `sIdx` is the index of the first non-zero element in `arrs`, `eIdx` is the index of the last non-zero element in `arrs` and is greater than or equal to `sIdx`, `i` is `eIdx + 1`, `cnt0` is equal to the number of zeros in the subarray of `arrs` from index `sIdx` to `eIdx` (inclusive), and the number of zeros in the subarray of `arrs` from index `sIdx` to `eIdx` (inclusive) which is equal to `cnt0` is being printed

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the count of zeros in a subarray of each test case. For each test case, it reads an integer length and a list of integers, finds the first and last non-zero elements, and counts the zeros in the subarray between these indices. The function assumes that the input is well-formed and does not perform any error checking. It processes all test cases and prints the count of zeros for each case.

