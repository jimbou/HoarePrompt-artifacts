#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the list) and then a list of integers (the elements of the list). The integers in the list are non-negative and less than the number of elements in the list.
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
        
    #State: `_` is the number of test cases, `n` is an integer, `i` is `n`, `arr` is a list of integers, `mpp` is a dictionary where keys are elements from `arr` and values are their respective frequencies, `first` is True if `mpp[i]` is 1 for any `i` in the range of `n`, otherwise `first` remains False, stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer (n) followed by a list of n integers. It then finds and prints the smallest integer that appears only once in the list, or the smallest missing integer in the range [0, n) if no such integer exists. The function processes all test cases and leaves the standard input empty.

