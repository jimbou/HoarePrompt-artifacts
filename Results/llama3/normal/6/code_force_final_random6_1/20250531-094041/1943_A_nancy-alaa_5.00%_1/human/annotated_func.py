#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the array) and then a space-separated list of integers (the elements of the array). The integer is a positive integer (1 <= n <= 2 * 10^5) and the elements of the array are non-negative integers (0 <= a_i < n). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: n is an integer, arr is a list of integers, mpp is a dictionary containing the frequency of each integer in arr, _ is equal to the number of test cases, stdin is empty, i is equal to n, first is True if there exists a key i in mpp such that mpp[i] is 1, otherwise first is False.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (n) and a space-separated list of integers (arr). It then finds the first integer that appears only once in the array, or the smallest missing integer in the range [0, n-1] if no such integer exists, and prints it. The function processes all test cases and leaves the input stream empty.

