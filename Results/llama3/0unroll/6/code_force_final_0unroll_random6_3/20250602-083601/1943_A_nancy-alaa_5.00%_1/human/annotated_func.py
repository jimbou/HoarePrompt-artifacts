#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The output will be the smallest missing number in the array for each test case. If there are no missing numbers, the output will be the smallest number that appears only once in the array. If there are no such numbers, the output will be the smallest number that appears more than once in the array.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. For each test case, it finds and prints the smallest missing number in the list. If no number is missing, it prints the smallest number that appears only once in the list. If no such number exists, it prints the smallest number that appears more than once in the list.

