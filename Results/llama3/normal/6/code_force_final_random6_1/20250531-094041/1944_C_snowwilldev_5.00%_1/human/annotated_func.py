#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 2 * 10^4) and then a list of integers (0 <= integer < 2 * 10^5). The sum of the lengths of the lists over all test cases does not exceed 2 * 10^5.
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
        
    #State: `tc` is equal to the number of test cases, `N` is an integer greater than or equal to 0, `a` is a list of integers, `cnt` is a dictionary with default value 0 and `cnt[a[i]]` is increased by 1 for all `i` in range `N`, `i` is `N`, `t` is the number of unique elements in `a`, stdin contains no test cases.

#Overall this is what the function does:The function processes multiple test cases from standard input. Each test case consists of an integer N and a list of integers. It counts the occurrences of each integer in the list and then finds the first integer that appears only once or does not appear at all in the list. If such an integer is found, it prints the integer and moves on to the next test case. The function continues this process until all test cases have been processed, at which point the standard input is empty.

