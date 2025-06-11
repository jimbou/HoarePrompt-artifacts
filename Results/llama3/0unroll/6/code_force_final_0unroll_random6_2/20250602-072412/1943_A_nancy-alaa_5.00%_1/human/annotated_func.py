#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The output state will contain the smallest missing number in each test case. If there is no missing number, it will print the smallest number that appears only once. If all numbers appear more than once, it will print the smallest number that appears only once in the second occurrence.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers. For each test case, it finds and prints the smallest missing number in the list. If no number is missing, it prints the smallest number that appears only once. If all numbers appear more than once, it prints the smallest number that appears only once in the second occurrence.

