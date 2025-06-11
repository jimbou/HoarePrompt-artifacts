#State of the program right berfore the function call: stdin contains t+2t lines, where t is an integer (1 <= t <= 1000). The first line contains t. Each of the following t blocks of two lines contains an integer n (2 <= n <= 50) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1). In each block, at least one a_i is 1.
    """
     
    0 과 1로 이루어진 배열을 받고 난 후 
    0으로만 연속되고 1으로만 연속된 하나의 블록으로 만드는 것이 목표임
    오른쪽에 있는 1을 가장 가까운 왼쪽으로 옮겨서 독립된 0, 1 블록으로 만들어야 함
     
    그냥 중간에 비어있는 0의 갯수가 정답일 듯
     
    """
    t = int(input())
    for _ in range(t):
        length = int(input())
        
        arrs = list(map(int, input().split()))
        
        cnt0 = 0
        
        for idx in range(len(arrs)):
            if arrs[0] == 0 and idx != 0:
                if arrs[idx] == 0:
                    cnt0 += 1
            elif arrs[0] == 1:
                if arrs[idx] == 0:
                    cnt0 += 1
        
        cnt1 = 0
        
        for idx in range(len(arrs)):
            if arrs[idx] == 1:
                cnt1 += 1
        
        if arrs[0] == 0:
            if arrs[len(arrs) - 1] == 0:
                cnt0 -= 1
        
        ans = 0
        
        if cnt1 == 1 or cnt1 == 0:
            ans = 0
        else:
            ans = cnt0
        
        print(ans)
        
    #State: t is an integer greater than or equal to 0, length is an integer, arrs is a list of integers, idx is len(arrs)-1, cnt0 is the number of zeros in arrs excluding the first element, cnt1 is the number of ones in arrs, ans is either 0 if cnt1 is 0 or 1, or the number of zeros in arrs excluding the first element if cnt1 is larger than 1, and stdin contains 0 lines.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts no parameters and returns no value. The function takes t, the number of test cases, as input, followed by t blocks of two lines each. Each block contains an integer n, the length of the array, and a space-separated list of n integers (0s and 1s). The function calculates the minimum number of zeros required to separate the ones into a contiguous block, excluding the first element. If there is only one or no ones, the result is 0. Otherwise, the result is the number of zeros in the array, excluding the first element. The function prints the result for each test case and consumes all input from stdin, leaving it empty.

