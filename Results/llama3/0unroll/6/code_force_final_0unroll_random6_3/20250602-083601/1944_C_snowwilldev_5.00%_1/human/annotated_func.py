#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the array) and then a space-separated list of integers (the elements of the array). The integers in the array are non-negative and less than the number of elements in the array.
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: The output will be the smallest number that appears only once in the array, or the smallest number that does not appear in the array. If no such number exists, the output will be the smallest number that appears more than once in the array.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case contains an array of non-negative integers. It then identifies and prints the smallest number that appears only once in the array, or the smallest number that does not appear in the array. If no such number exists, it prints the smallest number that appears more than once in the array.

