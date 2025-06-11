#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: The output state will contain the smallest missing number in each test case, or the smallest number that appears only once if no number is missing. If all numbers are present and no number appears only once, the output will be the smallest number that appears more than once.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It then finds and prints the smallest missing number in the list, or the smallest number that appears only once if no number is missing. If all numbers are present and no number appears only once, it prints the smallest number that appears more than once.

